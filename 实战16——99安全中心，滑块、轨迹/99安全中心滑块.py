#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
@Project ：pythonProject 
@File    ：demo.py
@IDE     ：PyCharm 
@Author  ：haozaispider
@Date    ：2025/5/12 上午10:29 
'''
import io
import cv2
import time
import json
import base64
import random
import string
import hashlib
import requests
from PIL import Image
from Crypto.Cipher import PKCS1_v1_5,AES
from Crypto.PublicKey import RSA
from captcha_recognizer.recognizer import Recognizer
from typing import List, Dict, Tuple
from loguru import logger


# aqHost = "https://aq.99.com"
# "Action=checkcodeinit&Data=d3d133d10ea566ff4805eaba2f679dab&Business=common"
def get_challenge():
    url = "https://aq.99.com/V5/Handler/Default.ashx"
    data = {
        'Action': "checkcodeinit",
        'Data': 'd3d133d10ea566ff4805eaba2f679dab',
        'Business': "common",
    }
    resp = requests.post(url, data=data).json()
    if resp['Code'] == 10101:
        return resp['Message']
    elif resp['Code'] == 10199:
        return "服务访问超时，请稍后重试"
    else:
        return None
def get_img_infos(challenge):
    headers = {
        "accept": "application/json, text/javascript, */*; q=0.01",
        "accept-language": "zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6",
        "cache-control": "no-cache",
        "content-type": "application/x-www-form-urlencoded",
        "origin": "https://aq.99.com",
        "pragma": "no-cache",
        "priority": "u=1, i",
        "referer": "https://aq.99.com/",
        "sec-ch-ua": "\"Chromium\";v=\"136\", \"Microsoft Edge\";v=\"136\", \"Not.A/Brand\";v=\"99\"",
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": "\"Windows\"",
        "sec-fetch-dest": "empty",
        "sec-fetch-mode": "cors",
        "sec-fetch-site": "same-site",
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/136.0.0.0 Safari/537.36 Edg/136.0.0.0"
    }
    url = "https://checkcode.99.com/slide"
    data = {
        "action": "create",
        "challenge": challenge,
        "ts": int(time.time() * 1000),
    }
    data = json.dumps(data, separators=(',', ':'))
    response = requests.post(url, headers=headers, data=data)
    return response.json()
####底图还原
def restore_image(t, image_path, output_path):
    # 打开原始图片
    with Image.open(image_path) as r:
        # 确保图片尺寸有效
        if r.width == 0 or r.height == 0:
            time.sleep(0.05)
            return restore_image(t, image_path, output_path)
        # 获取配置参数
        i = t.get('imageSegLength', 0)  # 每段宽度
        o = t.get('imageRandomPos', [])  # 乱序位置列表
        a = t.get('originalImageWidth', r.width)  # 原始宽度
        s = t.get('originalImageHeight', r.height)  # 原始高度

        # 创建用于还原的画布
        c = Image.new('RGBA', (a, s))

        # 处理每个乱序片段
        d = 0
        for v in range(len(o)):
            h = o[v]
            p = h * i
            y = i if h != len(o) - 1 else a - i * (len(o) - 1)

            # 从原始图片中裁剪片段
            box = (d, 0, d + y, s)
            l = r.crop(box)

            # 将片段放置到正确位置
            c.paste(l, (p, 0))
            d += y
        # 保存还原后的图片
        c.save(output_path)
        logger.success(f"图片还原成功，已经保存在{output_path}")
        return output_path
class Bt:
    def __init__(self):
        self.public_key = None

    def setPublicKey(self, key_pem: str):
        """设置PEM格式的RSA公钥"""
        # 处理可能缺少的页眉页脚
        if "-----BEGIN PUBLIC KEY-----" not in key_pem:
            key_pem = f"-----BEGIN PUBLIC KEY-----\n{key_pem}\n-----END PUBLIC KEY-----"
        self.public_key = RSA.import_key(key_pem)
        return self  # 支持链式调用

    def encrypt(self, plaintext: str) -> str:
        """使用RSA公钥加密并返回Base64编码结果"""
        if not self.public_key:
            raise ValueError("请先设置公钥")

        cipher = PKCS1_v1_5.new(self.public_key)
        encrypted_bytes = cipher.encrypt(plaintext.encode('utf-8'))
        return base64.b64encode(encrypted_bytes).decode('ascii')
def rsaEncrypt(public_key: str, plaintext: str) -> str:
    """模拟JavaScript中的rsaEncrypt函数"""
    r = Bt()
    return r.setPublicKey(public_key).encrypt(plaintext)
def getAesKey(t):
    # 定义可用字符集，排除了容易混淆的字符（如I、l、0、O）
    characters = string.ascii_uppercase + string.ascii_lowercase + string.digits
    characters = characters.replace('I', '').replace('l', '').replace('0', '').replace('O', '')

    # 生成指定长度的随机字符串
    return ''.join(random.choice(characters) for _ in range(t))
# Aes加密
def aesEncrypt(text, key=None, iv=None):
    cipher = AES.new(key.encode('utf-8'), AES.MODE_CBC, iv.encode('utf-8'))
    pad = 16 - len(text) % 16
    text = text + pad * chr(pad)
    encrypted_text = cipher.encrypt(text.encode('utf-8'))
    return base64.b64encode(encrypted_text).decode('utf-8')
def md5Encrypt(text: str, encoding: str = 'utf-8') -> str:
    """
    对输入文本进行 MD5 加密

    参数:
        text (str): 待加密的文本
        encoding (str): 文本编码方式，默认为 'utf-8'

    返回:
        str: 加密后的 32 位小写 MD5 哈希值
    """
    # 创建 MD5 对象
    md5 = hashlib.md5()

    # 更新哈希对象内容（需先将字符串编码为字节）
    md5.update(text.encode(encoding))

    # 获取十六进制表示的哈希值
    return md5.hexdigest()
def generate_strict_increasing_track(length: int, duration: int = 2000) -> Tuple[List[Dict[str, int]], int, int]:
    """
    严格从0开始的滑块轨迹生成器，保持示例数据规律

    :param length: 滑块需要移动的总长度(像素)
    :param duration: 期望的总时间(毫秒)，实际会有波动
    :return: (轨迹点列表, 开始时间戳, 结束时间戳)
    """
    points = []
    start_time = int(time.time() * 1000)
    current_time = start_time
    # 确保第一个点是x=0
    points.append({
        "x": 0,
        "y": 0,
        "t": current_time
    })

    x = 0
    y = 0
    base_interval = max(5, duration // length)  # 根据距离和期望时长动态调整基础间隔

    # 生成前进轨迹
    while x < length:
        # 根据进度计算当前阶段
        progress = x / length

        # 确定跳跃步长
        if progress < 0.3:  # 前30%
            step = random.choices([1, 2], weights=[80, 20], k=1)[0]
        elif progress < 0.7:  # 30%-70%
            step = random.choices([1, 2, 3], weights=[60, 30, 10], k=1)[0]
        else:  # 后30%
            step = random.choices([2, 3, 4], weights=[50, 30, 20], k=1)[0]

        x = min(x + step, length)  # 确保不超过总长度

        # 时间间隔生成
        if progress > 0.8 and random.random() < 0.15:  # 后段15%概率长停顿
            interval = base_interval + random.randint(100, 300)
        else:
            interval = base_interval * random.uniform(0.8, 1.2)  # ±20%波动

        current_time += max(5, int(interval))

        # y轴抖动生成
        if progress > 0.7:
            y = -random.randint(1, 4) if random.random() < 0.4 else 0

        points.append({
            "x": x,
            "y": y,
            "t": current_time
        })

    # 添加回退部分(80%概率)
    if length > 80 and random.random() < 0.8:
        back_steps = random.randint(3, 7)
        back_start = max(length - 10, length * 0.8)

        for i in range(1, back_steps + 1):
            back_x = max(int(back_start), x - i)
            if back_x < points[-1]["x"]:  # 确保是真正的回退
                current_time += random.randint(80, 250)
                y = -random.randint(1, 3)

                points.append({
                    "x": back_x,
                    "y": y,
                    "t": current_time
                })

    # 确保最后一个点正好在终点
    if points[-1]["x"] != length:
        current_time += random.randint(50, 150)
        points.append({
            "x": length,
            "y": -random.randint(1, 3) if random.random() < 0.5 else 0,
            "t": current_time
        })

    end_time = points[-1]["t"]

    # 调整总时长在预期范围内
    actual_duration = end_time - start_time
    if abs(actual_duration - duration) > duration * 0.3:  # 如果偏差超过30%
        ratio = duration / actual_duration
        for point in points[1:]:  # 不修改第一个点的时间
            elapsed = point["t"] - start_time
            point["t"] = start_time + int(elapsed * ratio)
        end_time = points[-1]["t"]

    return points, start_time, end_time
def get_s(startTime,stopTime,trackArr,bgImageWidth,bgImageHeight,sliderImageBase64):
    result = {
        # 当前时间 new Date
        't': stopTime,
        # 滑块轨迹
        'pj': trackArr,
        # 滑动时间
        'ut': stopTime - startTime,
        # 背景图片宽度
        'iw': bgImageWidth,
        # 背景图片高度
        'ih': bgImageHeight,
        # 滑块背景图片 + new Date + '' 进行md5(大写)
        'sm': md5Encrypt(sliderImageBase64 + str(stopTime)).upper(),
         # 浏览器指纹信息
        'bi': {
            "fonts": {
                "value": [
                    "Agency FB",
                    "Arial Unicode MS",
                    "Calibri",
                    "Century",
                    "Century Gothic",
                    "Franklin Gothic",
                    "Haettenschweiler",
                    "Leelawadee",
                    "Lucida Bright",
                    "Lucida Sans",
                    "MS Mincho",
                    "MS UI Gothic",
                    "MT Extra",
                    "Marlett",
                    "Microsoft Uighur",
                    "Monotype Corsiva",
                    "Pristina",
                    "Segoe UI Light",
                    "SimHei"
                ],
                "duration": 65
            },
            "domBlockers": {
                "duration": 15
            },
            "fontPreferences": {
                "value": {
                    "default": 151.703125,
                    "apple": 151.703125,
                    "serif": 165.21875,
                    "sans": 151.703125,
                    "mono": 119,
                    "min": 9.484375,
                    "system": 161.296875
                },
                "duration": 17
            },
            "audio": {
                "value": 0.0000832115,
                "duration": 58
            },
            "screenFrame": {
                "value": [
                    0,
                    0,
                    50,
                    0
                ],
                "duration": 0
            },
            "osCpu": {
                "duration": 0
            },
            "languages": {
                "value": [
                    [
                        "zh-CN"
                    ]
                ],
                "duration": 0
            },
            "colorDepth": {
                "value": 24,
                "duration": 0
            },
            "deviceMemory": {
                "value": 8,
                "duration": 0
            },
            "screenResolution": {
                "value": [
                    1920,
                    1080
                ],
                "duration": 1
            },
            "hardwareConcurrency": {
                "value": 12,
                "duration": 0
            },
            "timezone": {
                "value": "Asia/Shanghai",
                "duration": 0
            },
            "sessionStorage": {
                "value": True,
                "duration": 0
            },
            "localStorage": {
                "value": True,
                "duration": 0
            },
            "indexedDB": {
                "value": True,
                "duration": 0
            },
            "openDatabase": {
                "value": False,
                "duration": 0
            },
            "cpuClass": {
                "duration": 0
            },
            "platform": {
                "value": "Win32",
                "duration": 0
            },
            "plugins": {
                "value": [
                    {
                        "name": "PDF Viewer",
                        "description": "Portable Document Format",
                        "mimeTypes": [
                            {
                                "type": "application/pdf",
                                "suffixes": "pdf"
                            },
                            {
                                "type": "text/pdf",
                                "suffixes": "pdf"
                            }
                        ]
                    },
                    {
                        "name": "Chrome PDF Viewer",
                        "description": "Portable Document Format",
                        "mimeTypes": [
                            {
                                "type": "application/pdf",
                                "suffixes": "pdf"
                            },
                            {
                                "type": "text/pdf",
                                "suffixes": "pdf"
                            }
                        ]
                    },
                    {
                        "name": "Chromium PDF Viewer",
                        "description": "Portable Document Format",
                        "mimeTypes": [
                            {
                                "type": "application/pdf",
                                "suffixes": "pdf"
                            },
                            {
                                "type": "text/pdf",
                                "suffixes": "pdf"
                            }
                        ]
                    },
                    {
                        "name": "Microsoft Edge PDF Viewer",
                        "description": "Portable Document Format",
                        "mimeTypes": [
                            {
                                "type": "application/pdf",
                                "suffixes": "pdf"
                            },
                            {
                                "type": "text/pdf",
                                "suffixes": "pdf"
                            }
                        ]
                    },
                    {
                        "name": "WebKit built-in PDF",
                        "description": "Portable Document Format",
                        "mimeTypes": [
                            {
                                "type": "application/pdf",
                                "suffixes": "pdf"
                            },
                            {
                                "type": "text/pdf",
                                "suffixes": "pdf"
                            }
                        ]
                    }
                ],
                "duration": 0
            },
            "touchSupport": {
                "value": {
                    "maxTouchPoints": 0,
                    "touchEvent": False,
                    "touchStart": False
                },
                "duration": 0
            },
            "vendor": {
                "value": "Google Inc.",
                "duration": 0
            },
            "vendorFlavors": {
                "value": [
                    "chrome"
                ],
                "duration": 0
            },
            "cookiesEnabled": {
                "value": True,
                "duration": 1
            },
            "colorGamut": {
                "value": "p3",
                "duration": 0
            },
            "invertedColors": {
                "duration": 0
            },
            "forcedColors": {
                "value": False,
                "duration": 0
            },
            "monochrome": {
                "value": 0,
                "duration": 0
            },
            "contrast": {
                "value": 0,
                "duration": 0
            },
            "reducedMotion": {
                "value": False,
                "duration": 0
            },
            "reducedTransparency": {
                "value": False,
                "duration": 0
            },
            "hdr": {
                "value": False,
                "duration": 0
            },
            "math": {
                "value": {
                    "acos": 1.4473588658278522,
                    "acosh": 709.889355822726,
                    "acoshPf": 355.291251501643,
                    "asin": 0.12343746096704435,
                    "asinh": 0.881373587019543,
                    "asinhPf": 0.8813735870195429,
                    "atanh": 0.5493061443340548,
                    "atanhPf": 0.5493061443340548,
                    "atan": 0.4636476090008061,
                    "sin": 0.8178819121159085,
                    "sinh": 1.1752011936438014,
                    "sinhPf": 2.534342107873324,
                    "cos": -0.8390715290095377,
                    "cosh": 1.5430806348152437,
                    "coshPf": 1.5430806348152437,
                    "tan": -1.4214488238747245,
                    "tanh": 0.7615941559557649,
                    "tanhPf": 0.7615941559557649,
                    "exp": 2.718281828459045,
                    "expm1": 1.718281828459045,
                    "expm1Pf": 1.718281828459045,
                    "log1p": 2.3978952727983707,
                    "log1pPf": 2.3978952727983707,
                    "powPI": 1.9275814160560206e-50
                },
                "duration": 0
            },
            "pdfViewerEnabled": {
                "value": True,
                "duration": 0
            },
            "architecture": {
                "value": 255,
                "duration": 0
            },
            "applePay": {
                "value": -1,
                "duration": 0
            },
            "privateClickMeasurement": {
                "duration": 0
            },
            "webGlBasics": {
                "value": {
                    "version": "WebGL 1.0 (OpenGL ES 2.0 Chromium)",
                    "vendor": "WebKit",
                    "vendorUnmasked": "Google Inc. (NVIDIA)",
                    "renderer": "WebKit WebGL",
                    "rendererUnmasked": "ANGLE (NVIDIA, NVIDIA GeForce GT 730 (0x00001287) Direct3D11 vs_5_0 ps_5_0, D3D11)",
                    "shadingLanguageVersion": "WebGL GLSL ES 1.0 (OpenGL ES GLSL ES 1.0 Chromium)"
                },
                "duration": 6
            }
        },
        #配置接口Date参数
        'bf': 'd3d133d10ea566ff4805eaba2f679dab',
        'ct': "slide"
    }
    return json.dumps(result,separators=(',',':'))
def get_distince(bg_img, slide_img):
    ###方法三opencv识别，基本识别成功100%
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
def generate_k_i_w(s,secretKey):
    a = getAesKey(16)
    b = getAesKey(16)
    k = rsaEncrypt(secretKey, a)
    i = rsaEncrypt(secretKey, b)
    w = aesEncrypt(s, key=a, iv=b)
    return {
        "k": k,
        "i": i,
        "w": w
    }
def check_captcha(challenge,k,i,w):
    headers = {
        "accept": "application/json, text/javascript, */*; q=0.01",
        "accept-language": "zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6",
        "cache-control": "no-cache",
        "content-type": "application/x-www-form-urlencoded",
        "origin": "https://aq.99.com",
        "pragma": "no-cache",
        "priority": "u=1, i",
        "referer": "https://aq.99.com/",
        "sec-ch-ua": "\"Chromium\";v=\"136\", \"Microsoft Edge\";v=\"136\", \"Not.A/Brand\";v=\"99\"",
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": "\"Windows\"",
        "sec-fetch-dest": "empty",
        "sec-fetch-mode": "cors",
        "sec-fetch-site": "same-site",
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/136.0.0.0 Safari/537.36 Edg/136.0.0.0"
    }
    url = "https://checkcode.99.com/slide"
    data = {
        "action": "verify",
        "challenge": challenge,
        "k": k,
        "w": w,
        "i": i,
    }
    data = json.dumps(data, separators=(',', ':'))
    response = requests.post(url, headers=headers, data=data)
    logger.info(response.json())
    if response.json()['message'] == '成功':
        logger.success('验证成功')
    else:
        logger.error('验证失败')

def run():
    challenge = get_challenge()
    logger.info('成功获取到 challenge 值：' + str(challenge))
    img_infos = get_img_infos(challenge)
    logger.info('成功获取到验证码详细数据：' + str(img_infos))
    original_image_data = base64.b64decode(img_infos["data"]["originalImageBase64"])
    original_image = Image.open(io.BytesIO(original_image_data))
    original_image.save("original_image.png")
    logger.info('底图保存成功到original_image.png')
    slider_image_data = base64.b64decode(img_infos["data"]["sliderImageBase64"])
    slider_image = Image.open(io.BytesIO(slider_image_data))
    slider_image.save("slider_image.png")
    logger.info('缺口图保存成功到slider_image.png')
    restore_image(img_infos['data'], 'original_image.png', 'restored_image.png')
    bgImageWidth = img_infos['data']['originalImageWidth']
    bgImageHeight = img_infos['data']['originalImageHeight']
    sliderImageBase64 = img_infos['data']['sliderImageBase64']

    # recognizer = Recognizer()
    # box, conf = recognizer.identify_gap(source='restored_image.png', show_result=False, verbose=False)
    # distince = int(box[0])
    distince = get_distince('restored_image.png', 'slider_image.png')
    logger.info('缺口滑动距离：' + str(distince))
    trackArr, start_time, stopTime = generate_strict_increasing_track(distince)
    logger.info('生成轨迹数组：' + str(trackArr))
    s = get_s(start_time, stopTime, trackArr, bgImageWidth, bgImageHeight, sliderImageBase64)
    k_i_w_obj = generate_k_i_w(s, img_infos['data']['secretKey'])
    logger.info('k,i,w值：' + str(k_i_w_obj))
    k = k_i_w_obj['k']
    i = k_i_w_obj['i']
    w = k_i_w_obj['w']
    check_captcha(challenge, k, i, w)

if __name__ == '__main__':
    run()
