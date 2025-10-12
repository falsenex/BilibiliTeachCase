#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
@Project ：pythonProject 
@File    ：demo.py
@IDE     ：PyCharm 
@Author  ：haozaispider
@Date    ：2025/7/2 上午10:40 
'''
import datetime
import random
import ddddocr
import re
import hashlib
import time
from captcha_recognizer.recognizer import Recognizer
import cv2
import execjs
from PIL import Image
from loguru import logger
import requests
def get_appid():
    headers = {
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
        "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6",
        "Cache-Control": "no-cache",
        "Connection": "keep-alive",
        "Pragma": "no-cache",
        "Referer": "https://jiagu.360.cn/manage/index.html",
        "Sec-Fetch-Dest": "iframe",
        "Sec-Fetch-Mode": "navigate",
        "Sec-Fetch-Site": "same-origin",
        "Sec-Fetch-User": "?1",
        "Upgrade-Insecure-Requests": "1",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/138.0.0.0 Safari/537.36 Edg/138.0.0.0",
        "sec-ch-ua": "\"Not)A;Brand\";v=\"8\", \"Chromium\";v=\"138\", \"Microsoft Edge\";v=\"138\"",
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": "\"Windows\""
    }
    cookies = {
        "UV_SOURCE": "https://spidertools.cn/",
        "UV_SEM_PARAMS": "",
        "test_cookie_enable": "null",
        "__guid": "80005644.3171715975900273000.1751423874633.322",
        "__DC_sid": "80005644.1636570557649745700.1751423875167.3955",
        "__quc_silent__": "1",
        "UV_ID": "047c83daea7680e07083e12d48855888",
        "__DC_monitor_count": "2",
        "__DC_gid": "80005644.483467489.1751423875168.1751424050056.10"
    }
    url = "https://jiagu.360.cn/manage/captcha/demo.html"
    response = requests.get(url, headers=headers, cookies=cookies)
    response.encoding = 'utf-8'
    # print(response.text)
    # 使用正则表达式匹配aid的值
    matchs = re.findall(r'"aid"\s*:\s*"([^"]+)"', response.text)
    if matchs:
        aid_value = matchs[0]
        # logger.info("aid的值是:", aid_value)
        print('appId===>>>',aid_value)
    else:
        aid_value = None
        logger.error("未找到aid的值")
    return aid_value
def get_img_data(appid):
    headers = {
        "accept": "*/*",
        "accept-language": "zh-cn",
        "cache-control": "no-cache",
        "content-type": "application/x-www-form-urlencoded",
        "origin": "https://jiagu.360.cn",
        "pragma": "no-cache",
        "priority": "u=1, i",
        "referer": "https://jiagu.360.cn/",
        "sec-ch-ua": "\"Not)A;Brand\";v=\"8\", \"Chromium\";v=\"138\", \"Microsoft Edge\";v=\"138\"",
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": "\"Windows\"",
        "sec-fetch-dest": "empty",
        "sec-fetch-mode": "cors",
        "sec-fetch-site": "same-site",
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/138.0.0.0 Safari/537.36 Edg/138.0.0.0"
    }
    url = "https://captcha.jiagu.360.cn/api/v3/auth"
    data = {
        "appId": appid,
        "type": "1",
        "version": "2.0.0",
        "pn": "com.web.tianyu",
        "os": "3",
        "sdkName": "360CaptchaSDK",
        "timestamp": str(round(datetime.datetime.now().timestamp() * 1000)),
        "nonce": str(round(datetime.datetime.now().timestamp() * 1000) + int(random.random() * 100000000)),
        "ui": "null",
        "rc": "0",
        "pc": "0",
        "ec": "0",
        "hc": "0",
        "xc": "0",
        "dc": "0",
        "phone": "10000000000",
        # "sign": "f63741b9b3705e6fc283020680212db5"
    }
    # 过滤掉值为 "0" 的字段并排序
    filtered_data = {k: v for k, v in data.items()}
    sorted_items = sorted(filtered_data.items(), key=lambda x: x[0])

    # 连接所有键值对
    result = ''.join(f"{k}{v}" for k, v in sorted_items)
    print('result===>>>',result)
    sign = hashlib.md5(result.encode('utf-8')).hexdigest()
    print('sign===>>>',sign)
    data['sign'] = sign
    response = requests.post(url, headers=headers, data=data)
    logger.info(response.json())
    return response.json()
def save_img(bg_url,front_url):
    with open('bg.png', 'wb') as f:
        f.write(requests.get(bg_url).content)
        f.close()
        logger.success(f'乱序背景图片保存成功！！！！')
    with open('front.png', 'wb') as f1:
        f1.write(requests.get(front_url).content)
        f1.close()
        logger.success(f'滑块图片保存成功！！！！')
def recover_img(img_token,input_img_path,recover_img_path):
    recover_list = execjs.compile(open('demo.js', 'r', encoding='utf-8').read()).call('get_recover_list',img_token)
    logger.debug(f'获取的还原底图的数组是==>>{recover_list}')
    bg_img = Image.open(input_img_path)
    recover_img = Image.new('RGBA', (544, 284), 'white')
    for index, item in enumerate(recover_list):
        x = index * 17
        y = 0
        l = bg_img.crop((x, y, x + 17, y + 284))
        recover_img.paste(l, (item * 17, 0))
    recover_img.save(recover_img_path)
    logger.success(f'图片还原成功并保存在{recover_img_path}！！！')
def get_distince(gap_img,sl_img):
    det = ddddocr.DdddOcr(det=True, ocr=True)
    with open(sl_img, 'rb') as f:
        target_bytes = f.read()
    with open(gap_img, 'rb') as f:
        background_bytes = f.read()
    res = det.slide_match(target_bytes, background_bytes)
    logger.debug(res)
    return int(res['target'][0] / 544 * 300)
def get_distince1(bg_img):
    recognizer = Recognizer()
    box, confidence = recognizer.identify_gap(source=bg_img, verbose=False)
    logger.debug(f'可信度：{confidence}')
    return int(box[0] / 544 * 300)
def generate_trace(slide_distance):
    traceData = {}
    x = 0
    t = int(time.time()*1000)
    y = random.randint(210, 220)
    traceData[str(x)] = {'t': t, 'y': y}
    while x < slide_distance:
        x += random.randint(1, 5)
        t += random.randint(10, 20)
        if x >= slide_distance:
            x = slide_distance
            traceData[str(x)] = {'t': t, 'y': y+random.randint(-1, 1)}
            break
        traceData[str(x)] = {'t': t, 'y': y+random.randint(-1, 1)}
    return [traceData]
def check(guiji_array,captchaId, token,k,length):
    headers = {
        "accept": "*/*",
        "accept-language": "zh-cn",
        "cache-control": "no-cache",
        "content-type": "application/x-www-form-urlencoded",
        "origin": "https://jiagu.360.cn",
        "pragma": "no-cache",
        "priority": "u=1, i",
        "referer": "https://jiagu.360.cn/",
        "sec-ch-ua": "\"Not)A;Brand\";v=\"8\", \"Chromium\";v=\"138\", \"Microsoft Edge\";v=\"138\"",
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": "\"Windows\"",
        "sec-fetch-dest": "empty",
        "sec-fetch-mode": "cors",
        "sec-fetch-site": "same-site",
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/138.0.0.0 Safari/537.36 Edg/138.0.0.0"
    }
    url = "https://captcha.jiagu.360.cn/api/v3/check"
    report = execjs.compile(open('demo.js','r',encoding='utf-8').read()).call('get_report', guiji_array, captchaId, token, k)
    data = {
        "captchaId": captchaId,
        "token": token,
        "length": str(length),
        "version": "2.0.0",
        "width": "300",
        # "report": "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",
        "tracking": "[object Object]"
    }
    data['report'] = report
    response = requests.post(url, headers=headers, data=data)
    logger.info(response.json())
    if response.json()['data']['result'] == True:
        logger.success('验证成功了，嘿嘿！！！')
    else:
        logger.error('验证失败了，呜呜？？？')
if __name__ == '__main__':
    #获取appId
    appid= get_appid()
    #获取验证码图片数据
    img_data = get_img_data(appid)
    #图片保存
    save_img(img_data['data']['bg'][0],img_data['data']['front'][0])
    #还原图片
    recover_img(img_data['data']['bg'][0].split('/')[7].split('.')[0],'bg.png','recover.png')
    #验证滑块
    # distince = get_distince('recover.png','front.png')#ddddocr识别
    distince = get_distince1('recover.png')
    get_guiji_array = generate_trace(distince)
    check(get_guiji_array,img_data['data']['captchaId'],img_data['data']['token'],img_data['data']['k'],distince)




