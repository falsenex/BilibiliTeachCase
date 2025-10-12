#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
@Project ：pythonProject 
@File    ：yzm.py
@IDE     ：PyCharm 
@Author  ：haozaispider
@Date    ：2025/6/23 下午5:44 
'''
import base64
import io
import cv2
import ddddocr
import requests
from PIL import Image
from loguru import logger
def getPic():
    headers = {
        "Accept": "application/json, text/javascript, */*; q=0.01",
        "Accept-Language": "zh-CN,zh;q=0.9",
        "Cache-Control": "no-cache",
        "Connection": "keep-alive",
        "Content-Length": "0",
        "Origin": "https://login.189.cn",
        "Pragma": "no-cache",
        "Referer": "https://login.189.cn/web/login",
        "Sec-Fetch-Dest": "empty",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Site": "same-origin",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/137.0.0.0 Safari/537.36",
        "X-Requested-With": "XMLHttpRequest",
        "sec-ch-ua": "\"Google Chrome\";v=\"137\", \"Chromium\";v=\"137\", \"Not/A)Brand\";v=\"24\"",
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": "\"Windows\""
    }
    cookies = {
        "JSESSIONID": "D491050C496251088D4655289E348725",
        "U4r4xthJCQN5O": "60HZt5Kfa8uuXCgGHg88k2HVeU1crTZDRIsFzzyYMQtM2kZsuRhkjoCFIV8T.KjWEDpr0105lBgaCpiePOaHV_1A",
        "sajssdk_2015_cross_new_user": "1",
        "zhizhendata2015jssdkcross": "%7B%22distinct_id%22%3A%22MTk3OWJiMTc1ZmU4OWEtMDg4Yzc3NjU3Y2E5ZjctMjYwMTFlNTEtMjA3MzYwMC0xOTc5YmIxNzVmZjIzNWY%3D%22%2C%22first_id%22%3A%22%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E7%9B%B4%E6%8E%A5%E6%B5%81%E9%87%8F%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC_%E7%9B%B4%E6%8E%A5%E6%89%93%E5%BC%80%22%2C%22%24latest_referrer%22%3A%22%22%7D%2C%22login_type%22%3A%22%22%2C%22utms%22%3A%7B%7D%2C%22%24device_id%22%3A%221979bb175fe89a-088c77657ca9f7-26011e51-2073600-1979bb175ff235f%22%7D",
        "ECS_ReqInfo_login1": "U2FsdGVkX1%2Bt3I5YYHHrlovJR8OWCUf73WRe8IzV%2Bs6UTOOteyr4bM8YIst%2B2%2BJgWDiqQKojyOBwgbI8UnTKBQ%3D%3D",
        "EcsCaptchaKey": "4rOaQgq1uOY9GB24jRRbR3vcN1XKpJroJzsoQykafYbXe8QHyt6v1A%3D%3D",
        "U4r4xthJCQN5P": "06rkBGOs3zn_dgMtz6YJVj0HNsNCYaC80W4hwtqz002RRPxb.2D3mI_pwNgvNdJaY0hSgW7P4yUdQHVZSW3RSu9rhFV7751lM0anQKCMYa.P88w86l9OpSQ6lztI90mWtXMM49SKoZItVSKiiWqSISFcVxysBoCVS5GOqkfB5dLNHz9Xc7ydnjM..tJusVSw9aKwAd0nzxhJkOH4G1nj83HxPlhsOkge7F_yUaHzX6jxm4bKp0AVGmMGt0XEUbrbpyGr8BDSh1gWFa_IkmIiXrSuNH2eqRjGAhGV8Cq31DGiBiOaT35J3FA.KRbkeDrIw.7wr25d190jb8szGABmjhhdDmvqw8vrfn6_2qWukFaifq3SZW.VNeed8eqpVTonLVu4YfWyYmBKB5.F.N05359HPfbDYUva3lNw1PwHV9.a_COGVouW8EIDBiUU9moebd0scmF6_cATahd3ciEvRjG"
    }
    url = "https://login.189.cn/web/getPic"
    response = requests.post(url, headers=headers, cookies=cookies)
    return response.json()
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
    if small_img.size != (60, 60):
        logger.warning(f"警告: 小图片尺寸不是61×61，当前尺寸为{small_img.size}，将尝试调整大小。")
        small_img = small_img.resize((60, 60), Image.Resampling.LANCZOS)

    # 创建新的带透明通道的背景图
    background = Image.new('RGBA', (60, 150), background_color)

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
def ddddocr_slider1(gap_img,sl_img):
    det = ddddocr.DdddOcr(det=True, ocr=True)
    with open(sl_img, 'rb') as f:
        target_bytes = f.read()
    with open(gap_img, 'rb') as f:
        background_bytes = f.read()
    res = det.slide_match(target_bytes, background_bytes)
    # print(res)
    return res['target'][0]
def get_distance(img_json):
    original_image_data = base64.b64decode(img_json["backImage"])
    original_image = Image.open(io.BytesIO(original_image_data))
    original_image.save("bg.png")
    # 还原拼图图片
    jigsaw_image_data = base64.b64decode(img_json["slidingImage"])
    jigsaw_image = Image.open(io.BytesIO(jigsaw_image_data))
    jigsaw_image.save("slide.png")
    paste_image_on_background("slide.png", "new_slide.png", int(img_json["yHeight"]))
    # 读取背景图片和缺口图片
    gap_img = cv2.imread('bg.png')  # 背景图片
    slide_img = cv2.imread('new_slide.png')  # 缺口图片
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
    # res = max_loc[0]
    res = ddddocr_slider1('bg.png','new_slide.png')#ddocr识别验证
    logger.debug(f"缺口位置: {res}")
    return res

def check():
    img_json = getPic()
    res = get_distance(img_json)
    headers = {
        "Accept": "application/json, text/javascript, */*; q=0.01",
        "Accept-Language": "zh-CN,zh;q=0.9",
        "Cache-Control": "no-cache",
        "Connection": "keep-alive",
        "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
        "Origin": "https://login.189.cn",
        "Pragma": "no-cache",
        "Referer": "https://login.189.cn/web/login",
        "Sec-Fetch-Dest": "empty",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Site": "same-origin",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/137.0.0.0 Safari/537.36",
        "X-Requested-With": "XMLHttpRequest",
        "sec-ch-ua": "\"Google Chrome\";v=\"137\", \"Chromium\";v=\"137\", \"Not/A)Brand\";v=\"24\"",
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": "\"Windows\""
    }
    cookies = {
        "JSESSIONID": "D491050C496251088D4655289E348725",
        "U4r4xthJCQN5O": "60HZt5Kfa8uuXCgGHg88k2HVeU1crTZDRIsFzzyYMQtM2kZsuRhkjoCFIV8T.KjWEDpr0105lBgaCpiePOaHV_1A",
        "sajssdk_2015_cross_new_user": "1",
        "zhizhendata2015jssdkcross": "%7B%22distinct_id%22%3A%22MTk3OWJiMTc1ZmU4OWEtMDg4Yzc3NjU3Y2E5ZjctMjYwMTFlNTEtMjA3MzYwMC0xOTc5YmIxNzVmZjIzNWY%3D%22%2C%22first_id%22%3A%22%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E7%9B%B4%E6%8E%A5%E6%B5%81%E9%87%8F%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC_%E7%9B%B4%E6%8E%A5%E6%89%93%E5%BC%80%22%2C%22%24latest_referrer%22%3A%22%22%7D%2C%22login_type%22%3A%22%22%2C%22utms%22%3A%7B%7D%2C%22%24device_id%22%3A%221979bb175fe89a-088c77657ca9f7-26011e51-2073600-1979bb175ff235f%22%7D",
        "ECS_ReqInfo_login1": "U2FsdGVkX1%2Bt3I5YYHHrlovJR8OWCUf73WRe8IzV%2Bs6UTOOteyr4bM8YIst%2B2%2BJgWDiqQKojyOBwgbI8UnTKBQ%3D%3D",
        "EcsCaptchaKey": "4rOaQgq1uOY9GB24jRRbR3vcN1XKpJroJzsoQykafYbXe8QHyt6v1A%3D%3D",
        "U4r4xthJCQN5P": "06rkBGOs3zn_dgMtz6YJVj0HNsNCYaC80W4hwtqz002RRPxb.2D3mI_pwNgvNdJaY0hSgW7P4yUdQHVZSW3RSu9rhFV7751lM0anQKCMYa.P88w86l9OpSQ6lztI90mWtXMM49SKoZItVSKiiWqSISFcVxysBoCVS5GOqkfB5dLNHz9Xc7ydnjM..tJusVSw9aKwAd0nzxhJkOH4G1nj83HxPlhsOkge7F_yUaHzX6jxm4bKp0AVGmMGt0XEUbrbpyGr8BDSh1gWFa_IkmIiXrSuNH2eqRjGAhGV8Cq31DGiBiOaT35J3FA.KRbkeDrIw.7wr25d190jb8szGABmjhhdDmvqw8vrfn6_2qWukFaifq3SZW.VNeed8eqpVTonLVu4YfWyYmBKB5.F.N05359HPfbDYUva3lNw1PwHV9.a_COGVouW8EIDBiUU9moebd0scmF6_cATahd3ciEvRjG"
    }
    url = "https://login.189.cn/web/checkcapcode"
    data = {
        "xpos": str(res),
        "capcode": img_json['capcode'],
        "phonekey": "12140545349",
        "slidingType": "login_sliding"
    }
    response = requests.post(url, headers=headers, cookies=cookies, data=data)
    if response.json()["code"] == 2:
        logger.success("验证成功")
    else:
        logger.error("验证失败")
if __name__ == '__main__':
    check()

