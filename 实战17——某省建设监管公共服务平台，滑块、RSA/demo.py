#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
@Project ：pythonProject 
@File    ：demo.py
@IDE     ：PyCharm 
@Author  ：haozaispider
@Date    ：2025/4/15 下午6:50 
'''
import base64
import io
import ddddocr
import cv2
import execjs
import requests
import json
from PIL import Image
from loguru import logger
from captcha_recognizer.recognizer import Recognizer
headers = {
    "Accept": "application/json, text/plain, */*",
    "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6",
    "Cache-Control": "no-cache",
    "Connection": "keep-alive",
    "Content-Type": "application/json;charset=UTF-8",
    "Origin": "https://www.ynjzjgcx.com",
    "Pragma": "no-cache",
    "Referer": "https://www.ynjzjgcx.com/dataPub/enterprise",
    "Sec-Fetch-Dest": "empty",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Site": "same-origin",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/136.0.0.0 Safari/537.36 Edg/136.0.0.0",
    "appId": "84ded2cd478642b2",
    "isToken": "false",
    "sec-ch-ua": "\"Chromium\";v=\"136\", \"Microsoft Edge\";v=\"136\", \"Not.A/Brand\";v=\"99\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"Windows\""
}
def slider(gap_img):
    recognizer = Recognizer()
    box, confidence = recognizer.identify_gap(source=gap_img, verbose=False)
    logger.debug(f'可信度：{confidence}')
    return int(box[0])
def slider1(gap_img,sl_img):
    det = ddddocr.DdddOcr(det=True, ocr=True)
    with open(sl_img, 'rb') as f:
        target_bytes = f.read()
    with open(gap_img, 'rb') as f:
        background_bytes = f.read()
    res = det.slide_match(target_bytes, background_bytes)
    logger.debug(res)
    return res['target'][0]
# 410X200
def get_yzm():
    url = "https://www.ynjzjgcx.com/prod-api/mohurd-pub/vcode/genVcode"
    data = {
        # "params": "E4JujelupeAMqZpY0MNqjEF05KAIozpxQ8FSpGbtKfO50Wjci49T7tGyvf73lvIZayA14/sy681PGL4jF+gizCNL1EZzbxV0/zC3BJLf3zSBPLrVvtoUfOTTdPlatJzz8i4J98CIT2kI5CDG22vRCTK2m5+lssA8tDo4UdWOXzk="
    }

    params = execjs.compile(open("demo.js", "r", encoding="utf-8").read()).call("getParams",{"key":"query"})
    # params = execjs.compile(open("test.js", "r", encoding="utf-8").read()).call("getParams", {"key": "query"})
    data["params"] = params
    data = json.dumps(data, separators=(',', ':'))
    response = requests.post(url, headers=headers, data=data)
    logger.info(response.json())
    return response.json()
def get_distance(bg_img, slide_img):
    # 读取背景图片和缺口图片
    gap_img = cv2.imread(bg_img)  # 背景图片
    slide_img = cv2.imread(slide_img)  # 缺口图片
    # 识别图片边缘
    gap_edge = cv2.Canny(gap_img, 200, 300)
    slide_edge = cv2.Canny(slide_img, 200, 300)
    # 转换图片格式,为单通道
    gap_pic = cv2.cvtColor(gap_edge, cv2.COLOR_GRAY2RGB)
    slide_pic = cv2.cvtColor(slide_edge, cv2.COLOR_GRAY2RGB)
    # 缺口匹配
    res1 = cv2.matchTemplate(gap_pic, slide_pic, cv2.TM_CCOEFF_NORMED)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res1)  # 寻找最优匹配
    # 滑块缺口位置
    res = max_loc[0]
    return res

def paste_image_on_background(small_image_path, output_path, top, background_color=(0, 0, 0, 0)):
    """
    将一个61×61的PNG图片粘贴到一个61×200的背景图上，小图片距离背景图上边框67像素，保留透明通道。

    参数:
    small_image_path (str): 小图片的路径
    output_path (str): 输出图片的路径
    background_color (tuple): 背景图的颜色，默认为白色 (R, G, B, A)
    """
    # 打开小图片，确保包含Alpha通道
    try:
        small_img = Image.open(small_image_path).convert("RGBA")
    except Exception as e:
        logger.error(f"打开图片失败: {e}")
        return False

    # 确保小图片尺寸是61×61
    if small_img.size != (61, 61):
        logger.warning(f"警告: 小图片尺寸不是61×61，当前尺寸为{small_img.size}，将尝试调整大小。")
        small_img = small_img.resize((61, 61), Image.Resampling.LANCZOS)

    # 创建新的带透明通道的背景图
    background = Image.new('RGBA', (61, 200), background_color)

    # 计算粘贴位置（距离上边框XX像素）
    position = (0, top)  # (left, top)

    # 粘贴小图片到背景图上，保留透明通道
    background.paste(small_img, position, small_img)

    # 保存结果，确保保存为PNG格式以保留透明通道
    try:
        if not output_path.lower().endswith('.png'):
            output_path += '.png'
        background.save(output_path, "PNG")
        logger.success(f"图片已成功保存到: {output_path}")
        return True
    except Exception as e:
        logger.error(f"保存图片失败: {e}")
        return False

def yanzheng(slideId, width):
    url = "https://www.ynjzjgcx.com/prod-api/mohurd-pub/dataServ/findBaseEntDpPage"
    data = {
        # "params": "QFP8drGxRvB4vpXNipULPmeydpofgCXc1IiTgjwVi3QwuEBTM3lWqPBwlS1t7A1ON6kfY4c9IyMvez/tO9jp5hCi5jac8Q+cQ3ObDvFTXAnR2lUbA2+jfvswVxGRqDH+/Cyd42ZPIg3bNjcvyxvrOKtKnBvftl+2gq8q7ASG3bQ=,cylLn6pIOzy9Xznr6EVF4W/GBO9zVeQhe+3MuZ5tdolR26iAi6VtaRR9Lb3KroeegE0/YpBmI91l+AhdcgHlYLl3olQEO9/xuPSj6CEdSNAD5xW8dUZW9aTEA1T4YAqhCNuk5KQOq0D0hbkcPn87AcGKD/C7Pn83eP+OgVE45qA="
    }
    params = execjs.compile(open("demo.js", "r", encoding="utf-8").read()).call("getParams",{"pageNum": 5, "pageSize": 10, "certificateType": "", "name": "", "slideId": slideId, "key": "query","width": width})
    data["params"] = params
    data = json.dumps(data, separators=(',', ':'))
    response = requests.post(url, headers=headers, data=data)
    if response.status_code != 200:
        logger.error(response.json()['msg'])
    logger.success(response.json())
def run():
    data_str = get_yzm()['data']
    data = json.loads(data_str)
    # 还原原始图片
    original_image_data = base64.b64decode(data["bigImage"])
    original_image = Image.open(io.BytesIO(original_image_data))
    original_image.save("original_image.png")
    # 还原拼图图片
    jigsaw_image_data = base64.b64decode(data["smallImage"])
    jigsaw_image = Image.open(io.BytesIO(jigsaw_image_data))
    jigsaw_image.save("jigsaw_image.png")

    #from captcha_recognizer.recognizer import Recognizer ---->>>基本100%
    # slide_distance = slider("original_image.png")

    ###优化后ddddocr  --->>>95%以上
    paste_image_on_background("jigsaw_image.png", "jigsaw_image1.png", data["yHeight"])
    # slide_distance = slider1("original_image.png", "jigsaw_image1.png")
    slide_distance = get_distance("original_image.png", "jigsaw_image1.png")
    logger.info('滑动距离为：' + str(slide_distance))
    yanzheng(data["slideId"], slide_distance)

if __name__ == '__main__':
    run()

# '{"pageNum":1,"pageSize":10,"certificateType":"","name":"","slideId":"1375228898236694528","key":"query","width":210}'
