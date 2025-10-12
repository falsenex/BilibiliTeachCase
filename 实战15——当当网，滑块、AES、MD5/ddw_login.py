# -*-coding: Utf-8 -*-
import cv2
import time
import json
import random
import base64
import ddddocr
from PIL import Image
import hashlib
import requests
from loguru import logger
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad
from captcha_recognizer.recognizer import Recognizer
session = requests.Session()

headers = {
    "Accept": "application/json, text/plain, */*",
    "Accept-Language": "zh-CN,zh;q=0.9",
    "Cache-Control": "no-cache",
    "Connection": "keep-alive",
    "Content-Type": "application/x-www-form-urlencoded",
    "Origin": "https://login.dangdang.com",
    "Pragma": "no-cache",
    "Referer": "https://login.dangdang.com/?returnurl=https%3A%2F%2Fwww.dangdang.com%2F",
    "Sec-Fetch-Dest": "empty",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Site": "same-origin",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36",
    "sec-ch-ua": "\"Chromium\";v=\"130\", \"Google Chrome\";v=\"130\", \"Not?A_Brand\";v=\"99\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"Windows\""
}


def j(data: str) -> str:
    """ 模拟 JavaScript J() 函数，使用 MD5 计算哈希值 """
    return hashlib.md5(data.encode()).hexdigest()


def h(hash_str: str) -> str:
    """ 计算 hash_str 的前 8 个字符转换为整数后取前 6 位 """
    num = int(hash_str[:8], 16)
    a = str(num)[:6]
    return a.ljust(6, '0')  # 确保长度至少为 6

def g() -> str:
    t = "DDClick521"
    now = time.localtime()

    n = str(now.tm_year)
    a = f"{now.tm_mon:02d}"
    r = f"{now.tm_mday:02d}"
    s = f"{now.tm_hour:02d}"
    i = f"{now.tm_min:02d}"
    o = f"{now.tm_sec:02d}"
    c = f"{int(time.time() * 1000) % 1000:03d}"

    l = random.randint(100000, 999999)
    u = random.randint(100000, 999999)

    d = n + a + r + s + i + o + c + str(l) + str(u) + t
    p = j(d)
    p = h(p)

    return n + a + r + s + i + o + c + p + str(l) + str(u)

def get_time_stamp():
    return int(time.time()) * 1000


def md5_encrypt(post_data):
    return hashlib.md5((post_data).encode('utf-8')).hexdigest()

def aes_encrypt(md5_post_data, ran_key):
    iv = b'0102030405060708'
    # 创建 AES 加密器
    key = ran_key.encode() if isinstance(ran_key, str) else ran_key
    if not key:  # 如果 key 为空, 填充 16 字节的 0
        key = b"\x00" * 16
    cipher = AES.new(key, AES.MODE_CBC, iv=iv)

    # 加密（需要填充）
    ciphertext = cipher.encrypt(pad(md5_post_data.encode(), AES.block_size))

    # 转成 Base64 以便存储或传输
    return base64.b64encode(ciphertext).decode()

def get_sign(post_data_get_ran_key, ran_key):
    # 定义键的顺序
    ordered_keys = [
        "ct", "need_new_verifydata", "permanent_id", "point_json", "requestId",
        "situation", "slide_cost_time", "t", "verifyToken"
    ]
    post_data = "&".join(
        f"{key}={post_data_get_ran_key[key]}"
        for key in ordered_keys if key in post_data_get_ran_key
    )
    # logger.info(post_data)
    md5_result = md5_encrypt(post_data)
    # logger.info(md5_result)
    aes_sign = aes_encrypt(md5_result, ran_key)
    # logger.info(aes_sign)
    return aes_sign

def get_ran_key():
    data = {
        "t": get_time_stamp(),
        "permanent_id": permanent_id,
    }
    url = "https://login.dangdang.com/api/customer/loginapi/getRankey"
    # 校验 t -> {"statusCode":"1","errorCode":"1","errorMsg":"时间戳过期","requestId":null,"rankey":null}
    response = session.post(url, headers=headers,
                            data=data
                            ).json()
    request_id = response['requestId']
    ran_key = response['rankey']
    return request_id, ran_key

def get_sliding_verify_code(request_id, ran_key):
    url = "https://login.dangdang.com/api/customer/loginapi/getSlidingVerifyCode"
    data = {
        "ct": "pc",
        "permanent_id": permanent_id,
        "requestId": request_id,
        "situation": "login",
        "t": get_time_stamp(),
    }
    sign = get_sign(data, ran_key)
    data.update({
        "sign": sign
    })
    # requestId、sign、t 不能为空
    # sign 不对 -> {"errorCode":"1","errorMsg":"检查签名失败","data":null,"status":"-22"}
    response = session.post(url, headers=headers, data=data).json()
    # logger.debug(response)

    slide_img = response['data']['slideImg']
    bg_img = response['data']['bgImg']
    y = response['data']['y']
    height_ratio = response['data']['heightRatio']
    encrypt_key = response['data']['encryptKey']
    verify_token = response['data']['token']

    return {
        'slideImg': slide_img,
        'bgImg': bg_img,
        'y': y,
        'heightRatio': height_ratio,
        'encryptKey': encrypt_key,
        'verifyToken': verify_token,
    }

def check_captcha(request_id, ran_key, img_data):
    # 识别距离
    fg_content = requests.get(img_data['slideImg']).content
    bg_content = requests.get(img_data['bgImg']).content
    with open('slide.jpg', 'wb') as f:
        f.write(fg_content)
    with  open('bg.jpg', 'wb') as f:
        f.write(bg_content)
    ###不太行   30%
    # det = ddddocr.DdddOcr(det=False, ocr=False, show_ad=False)
    # res = det.slide_match(fg_content, bg_content)["target"][0]

    ###也不太行  30%
    # recognizer = Recognizer()
    # box, confidence = recognizer.identify_gap(source='bg.jpg', verbose=False)
    # res = box[0]


    ###方法三opencv识别，基本识别成功100%
    # 读取背景图片和缺口图片
    gap_img = cv2.imread('bg.jpg')  # 背景图片
    with Image.open('bg.jpg') as img:
        width, height = img.size
    logger.info(str(width) + 'X' + str(height))
    slide_img = cv2.imread('slide.jpg')  # 缺口图片
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


    # x_left = res / 408
    x_left = int(res * 350 / 408)
    # 408 x 204（保存图片的大小） | 350 x 175(网页的大小)
    distance_data = {
        'x': x_left / 350,
        # 'x': x_left,
        'y': img_data['y']
    }
    distance_data_str = json.dumps(distance_data, separators=(',', ':'))
    logger.info(distance_data_str)
    point_json = aes_encrypt(distance_data_str, img_data['encryptKey'])
    # 校验 slide_cost_time
    data = {
        "ct": "pc",
        "need_new_verifydata": 0,
        "permanent_id": permanent_id,  # 未校验
        "point_json": point_json,
        "requestId": request_id,
        "situation": "login",
        "slide_cost_time": 300,  # 时间长 -> {"errorCode":"1","errorMsg":"错误","status":"6"}
        "t": get_time_stamp(),
        "verifyToken": img_data['verifyToken']
    }

    sign = get_sign(data, ran_key)
    # logger.info(sign)
    data.update({
        "sign": sign
    })
    url = "https://login.dangdang.com/api/customer/loginapi/checkSlidingVerifyCode"
    cookies = {
        '__permanent_id': permanent_id
    }
    response = session.post(url, headers=headers, data=data, cookies=cookies)
    logger.info(response.text)

    # x_left error -> {"errorCode":"1","errorMsg":"错误","data":null,"status":"3"}
    # slide_cost_time error -> {"errorCode":"1","errorMsg":"错误","status":"6"}
    # post_data error -> {"errorCode":"1","errorMsg":"检查签名失败","data":null,"status":"-22"}


def main():
    request_id, ran_key = get_ran_key()
    # logger.info(f'requestId: {request_id}, rankey: {ran_key}')

    img_data = get_sliding_verify_code(request_id, ran_key)
    logger.info(img_data)

    check_captcha(request_id, ran_key, img_data)


if __name__ == '__main__':
    for _ in range(20):
        permanent_id = g()
        logger.info(f"permanent_id: {permanent_id}")
        main()
        logger.success('----------------------------------------------------------------------------------------------')
