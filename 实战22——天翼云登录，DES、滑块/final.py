#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
@Project ：pythonProject 
@File    ：final.py
@IDE     ：PyCharm 
@Author  ：haozaispider
@Date    ：2025/6/18 上午11:16 
'''
import base64
import io
import random

import cv2
import execjs
from PIL import Image
from requests import Session
from loguru import logger
import ddddocr

class TYY_Login:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.session = Session()
        self.session.headers.update({
            "Accept": "application/json, text/plain, */*",
            "Accept-Language": "zh-CN,zh;q=0.9",
            "Cache-Control": "no-cache",
            "Connection": "keep-alive",
            "Content-Type": "application/x-www-form-urlencoded",
            "Origin": "https://m.ctyun.cn",
            "Pragma": "no-cache",
            "Referer": "https://m.ctyun.cn/wap/main/auth/login?redirect=%2Fmy",
            "Sec-Fetch-Dest": "empty",
            "Sec-Fetch-Mode": "cors",
            "Sec-Fetch-Site": "same-origin",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/137.0.0.0 Safari/537.36",
            "sec-ch-ua": "\"Google Chrome\";v=\"137\", \"Chromium\";v=\"137\", \"Not/A)Brand\";v=\"24\"",
            "sec-ch-ua-mobile": "?0",
            "sec-ch-ua-platform": "\"Windows\""
        })
        self.session.cookies.update({
            "Hm_lvt_4b4ce93f1c92033213556e55cb65769f": "1750213229",
            "Hm_lpvt_4b4ce93f1c92033213556e55cb65769f": "1750213229",
            "HMACCOUNT": "FBA153B9F1F02FA3",
            "pvid": "1"
        })

    def ddddocr_slider1(self,gap_img,sl_img):
        det = ddddocr.DdddOcr(det=True, ocr=True)
        with open(sl_img, 'rb') as f:
            target_bytes = f.read()
        with open(gap_img, 'rb') as f:
            background_bytes = f.read()
        res = det.slide_match(target_bytes, background_bytes)
        # print(res)
        return res['target'][0]
    def get_loginId(self,length = 32, base = 16):
        characters = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
        available_chars = characters[:base]  # Select characters based on the base
        if length:
            return ''.join(random.choice(available_chars) for _ in range(length))
        else:
            # Emulate the GUID/UUID logic from the JavaScript code (if length is 0)
            o = [None] * 36
            o[8] = o[13] = o[18] = o[23] = "-"
            o[14] = "4"
            for e in range(36):
                if o[e] is None:
                    n = random.randint(0, 15)  # Equivalent to 0 | 16 * Math.random()
                    if e == 19:
                        n = (n & 0x3) | 0x8  # Equivalent to 3 & n | 8 (forces version to 4 and variant to RFC4122)
                    o[e] = characters[n]  # use full character set to allow hex + more
            return ''.join(o)

    def paste_image_on_background(self,small_image_path, output_path, top, background_color=(0, 0, 0, 0)):
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
        if small_img.size != (50, 50):
            logger.warning(f"警告: 小图片尺寸不是61×61，当前尺寸为{small_img.size}，将尝试调整大小。")
            small_img = small_img.resize((50, 50), Image.Resampling.LANCZOS)

        # 创建新的带透明通道的背景图
        background = Image.new('RGBA', (50, 200), background_color)

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
    def get_slide_img(self,loginId):
        url = "https://m.ctyun.cn/alogic-ctyun/user/SlideVerify"
        data = {
            "loginId": loginId
        }
        response = self.session.post(url, data=data)
        return response.json()
    def get_distance(self,img_json):
        original_image_data = base64.b64decode(img_json["data"]["shadeImage"])
        original_image = Image.open(io.BytesIO(original_image_data))
        original_image.save("bg.png")
        # 还原拼图图片
        jigsaw_image_data = base64.b64decode(img_json["data"]["cutoutImage"])
        jigsaw_image = Image.open(io.BytesIO(jigsaw_image_data))
        jigsaw_image.save("slide.png")
        self.paste_image_on_background("slide.png", "new_slide.png", int(img_json["data"]["y"]))
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
        res = max_loc[0]
        # res = self.ddddocr_slider1('bg.png','new_slide.png')#ddocr识别验证
        return res,img_json["data"]['y']
    def get_slide_img_verify_result(self, params_json,loginId,x_y_json):
        url = "https://m.ctyun.cn/alogic-ctyun/user/VerifySlideVerify"
        params = {
            "referrer": "wap",
            "mainVersion": "300031500",
            "comParam_curTime": params_json['params']['comParam_curTime'],
            "comParam_seqCode": params_json['params']['comParam_seqCode'],
            "comParam_signature": params_json['params']['comParam_signature'],
            "isCheck": "true",
            "locale": "zh-cn"
        }
        data = {
            "loginId": loginId,
            'x':x_y_json['x'],
            'y':x_y_json['y']
        }
        response = self.session.post(url, params=params, data=data)
        logger.info(f'滑块验证结果：{response.json()}')
        return response.json()
    def login(self,params_json):
        url = "https://m.ctyun.cn/account/login"
        params = {
            "referrer": "wap",
            "mainVersion": "300031500",
            "comParam_curTime": params_json['params']['comParam_curTime'],
            "comParam_seqCode": params_json['params']['comParam_seqCode'],
            "comParam_signature": params_json['params']['comParam_signature'],
            "isCheck": "true",
            "locale": "zh-cn"
        }
        data = {
            "userName": params_json['data']["userName"],
            "password": params_json['data']["password"]
        }
        response = self.session.post(url,params=params, data=data)
        return response

    def login_with_slide(self,params_json):
        loginId = self.get_loginId()
        img_json = self.get_slide_img(loginId)
        distance,y = self.get_distance(img_json)
        x_y_json = execjs.compile(open('验证码.js', 'r', encoding='utf-8').read()).call('get_x_y', loginId, distance, y)
        verify_result = self.get_slide_img_verify_result(params_json,loginId,x_y_json)
        if verify_result['data']['success'] == 'true':
            logger.success('验证码验证成功')
        else:
            logger.error('验证码验证失败！！！！')
        url = "https://m.ctyun.cn/account/login"
        params = {
            "referrer": "wap",
            "mainVersion": "300031500",
            "comParam_curTime": params_json['params']['comParam_curTime'],
            "comParam_seqCode": params_json['params']['comParam_seqCode'],
            "comParam_signature": params_json['params']['comParam_signature'],
            "isCheck": "true",
            "locale": "zh-cn"
        }
        data = {
            "userName": params_json['data']["userName"],
            "password": params_json['data']["password"],
            'x': x_y_json['x'],
            'y': x_y_json['y'],
            'loginId': loginId
        }
        response = self.session.post(url, params=params, data=data)
        logger.info(response.text)
    def run(self):
        user_infos = {
            "userName": self.username,
            "password": self.password
        }
        params_json = execjs.compile(open('demo.js', 'r', encoding='utf-8').read()).call('getParams', user_infos)
        logger.debug(f'加密参数：{params_json}')
        response = self.login(params_json)
        logger.warning(f'登录结果：{response.json()}')
        if response.json()['resultCode'] == '-990':
            self.login_with_slide(params_json)
if __name__ == '__main__':
    TYY_Login('1234567890@126.com', 'xxxooo666').run()
