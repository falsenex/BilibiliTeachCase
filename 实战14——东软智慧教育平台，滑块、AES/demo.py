import base64
import execjs
from PIL import Image
import io
import requests
import json
import ddddocr
import cv2
import numpy as np
from loguru import logger

headers = {
        "Accept": "application/json, text/plain, */*",
        "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6",
        "Cache-Control": "no-cache",
        "Connection": "keep-alive",
        "Content-Type": "application/json",
        "Origin": "https://neustudy.neumooc.com",
        "Pragma": "no-cache",
        "Referer": "https://neustudy.neumooc.com/",
        "Sec-Fetch-Dest": "empty",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Site": "same-origin",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/136.0.0.0 Safari/537.36 Edg/136.0.0.0",
        "sec-ch-ua": "\"Chromium\";v=\"136\", \"Microsoft Edge\";v=\"136\", \"Not.A/Brand\";v=\"99\"",
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": "\"Windows\"",
        "tenant-id": "1"
    }
cookies = {
    "Hm_lvt_a1ff8825baa73c3a78eb96aa40325abc": "1746778128",
    "HMACCOUNT": "012ABEC5BEE08178",
    "Hm_lpvt_a1ff8825baa73c3a78eb96aa40325abc": "1746781908"
}
# from captcha_recognizer.recognizer import Recognizer
# def slider(gap_img):
#     recognizer = Recognizer()
#     box, confidence = recognizer.identify_gap(source=gap_img, verbose=False)
#     logger.info('可信度为:' + str(confidence))
#     return int(box[0])
def slider1(gap_img,sl_img):
    det = ddddocr.DdddOcr(det=True, ocr=True)
    with open(sl_img, 'rb') as f:
        target_bytes = f.read()
    with open(gap_img, 'rb') as f:
        background_bytes = f.read()
    res = det.slide_match(target_bytes, background_bytes)
    return res['target'][0]
def slider2(gap_img,sl_img):
    # 读取背景图片和缺口图片
    gap_img = cv2.imread(gap_img)  # 背景图片
    slide_img = cv2.imread(sl_img)  # 缺口图片
    # 识别图片边缘
    gap_edge = cv2.Canny(gap_img, 200, 300)
    slide_edge = cv2.Canny(slide_img, 200, 300)
    # 转换图片格式,为单通道
    gap_pic = cv2.cvtColor(gap_edge, cv2.COLOR_GRAY2RGB)
    slide_pic = cv2.cvtColor(slide_edge, cv2.COLOR_GRAY2RGB)
    # 缺口匹配
    res = cv2.matchTemplate(gap_pic, slide_pic, cv2.TM_CCOEFF_NORMED)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)  # 寻找最优匹配
    # print(min_loc, max_loc)
    # print(min_val, max_val)
    # 滑块缺口位置
    X = max_loc[0]
    return X

def get_pointJson(X,secretKey):
    zb = json.dumps({"x": X, "y": 5},separators=(',', ':'))
    pointJson = execjs.compile(open('demo.js', 'r', encoding='utf-8').read()).call('get_pointJson',zb, secretKey)
    return pointJson

def get_hk():
    url = "https://neustudy.neumooc.com/web-api/system/captcha/get"
    data = {
        "captchaType": "blockPuzzle"
    }
    data = json.dumps(data, separators=(',', ':'))
    response = requests.post(url, headers=headers, cookies=cookies, data=data)
    return response.json()
def save_image_and_get_juli(data):
    # 还原原始图片
    original_image_data = base64.b64decode(data["repData"]["originalImageBase64"])
    original_image = Image.open(io.BytesIO(original_image_data))
    original_image.save("original_image.png")
    # 还原拼图图片
    jigsaw_image_data = base64.b64decode(data["repData"]["jigsawImageBase64"])
    jigsaw_image = Image.open(io.BytesIO(jigsaw_image_data))
    jigsaw_image.save("jigsaw_image.png")
    #captcha_recognizer识别
    # slide_distance = slider("original_image.png")
    #ddddocr识别
    slide_distance = slider1("original_image.png", "jigsaw_image.png")
    #基于opencv和gpt写的边缘检测获取距离
    # slide_distance = slider2("original_image.png", "jigsaw_image.png")
    logger.info('滑行的距离:' + str(slide_distance))
    return slide_distance

def check_captcha(data,X):
    url = "https://neustudy.neumooc.com/web-api/system/captcha/check"
    secretKey = data["repData"]["secretKey"]
    token = data["repData"]["token"]
    pointJson = get_pointJson(X,secretKey)
    logger.info('加密参数pointJson:' + str(pointJson))
    data = {
        "captchaType": "blockPuzzle",
        "pointJson": pointJson,
        "token": token
    }
    data = json.dumps(data, separators=(',', ':'))
    response = requests.post(url, headers=headers, cookies=cookies, data=data)
    if response.json()['repData']['result'] == True:
        logger.warning(response.text)
        logger.success('验证成功！！！')
    else:
        logger.error(response.text)
def run():
    data = get_hk()
    X = save_image_and_get_juli(data)
    check_captcha(data,X)
if __name__ == '__main__':
    run()
