#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
@Project ：pythonProject 
@File    ：demo.py
@IDE     ：PyCharm 
@Author  ：haozaispider
@Date    ：2025/7/11 上午11:19 
'''
import hashlib
import json
import random
import re
import secrets
import time
import ddddocr
import requests
from captcha_recognizer.recognizer import Recognizer
from loguru import logger
import base64
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_v1_5, PKCS1_OAEP
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad
import binascii
import secrets
import string
import uuid
# from 距离识别 import *
'''
RSA加密部分
'''
# 从PEM格式或模数/指数对加载RSA公钥
def load_public_key(pem_key=None, modulus=None, exponent=None):
    if pem_key:
        # 清理PEM格式，移除换行和空格，并提取实际密钥部分
        cleaned = pem_key.replace("\n", "").replace(" ", "")
        if "-----" in cleaned:
            cleaned = [part for part in cleaned.split("-----") if len(part) > 25][0]
        key_bytes = base64.b64decode(cleaned)
        return RSA.importKey(key_bytes)

    elif modulus and exponent:
        # 从16进制字符串或整数形式的模数和指数构造RSA公钥
        n = int(modulus, 16) if isinstance(modulus, str) else modulus
        e = int(exponent, 16) if isinstance(exponent, str) else exponent
        return RSA.construct((n, e))

    raise ValueError("必须提供 PEM 公钥或 modulus + exponent")
# 根据指定的填充模式获取加密器对象
def get_cipher(key_obj, padding_mode: int):
    scheme = {
        1: PKCS1_OAEP.new,  # OAEP填充（推荐）
        2: PKCS1_v1_5.new   # 传统的PKCS#1 v1.5填充
    }
    if padding_mode not in scheme:
        raise ValueError("padding_mode 只支持 1（OAEP）或 2（v1_5）")
    return scheme[padding_mode](key_obj)
# 加密字节数据
def encrypt_bytes(plaintext: str, *, pem_key=None, modulus="00C1E3934D1614465B33053E7F48EE4EC87B14B95EF88947713D25EECBFF7E74C7977D02DC1D9451F79DD5D1C10C29ACB6A9B4D6FB7D0A0279B6719E1772565F09AF627715919221AEF91899CAE08C0D686D748B20A3603BE2318CA6BC2B59706592A9219D0BF05C9F65023A21D2330807252AE0066D59CEEFA5F2748EA80BAB81", exponent="10001", padding_mode=2) -> bytes:
    key_obj = load_public_key(pem_key=pem_key, modulus=modulus, exponent=exponent)
    cipher = get_cipher(key_obj, padding_mode)
    encrypted_data = cipher.encrypt(plaintext.encode())
    return encrypted_data
# 将加密结果转换为16进制字符串
def rsaencrypt_to_hex(plaintext: str, **kwargs) -> str:
    return binascii.hexlify(encrypt_bytes(plaintext, **kwargs)).decode()
'''
获取load接口返回数据
'''
def get_imgurl_and_verify_params(slide):
    # 正则匹配
    bg_re = re.compile(',"bg\"\:"(.*?)",\"ypos\"')    # 背景图片url
    slice_re = re.compile('de\"\,\"slice\"\:"(.*?)"')   # 缺口url


    lot_re = re.compile('"lot_number":"(.*?)","cap')    # 参数lot_number
    payload_re = re.compile('"payload":"(.*?)","proc')    # 参数payload
    protk_re = re.compile('"process_token":"(.*?)","pay')    # 参数process_token
    pow_detail_re = re.compile('"pow_detail":(.*?),"payload')    # pow_detail对象

    url = "https://gcaptcha4.geetest.com/load"
    params = {
        "callback": "geetest_1756906162940",
        "captcha_id":"24f56dc13c40dc4a02fd0318567caef5",###md5
        # "captcha_id": "54088bb07d2df3c46b79f80300b0abbe",###sha256
        "challenge": uuid.uuid4(),
        "client_type": "web",
        "risk_type": "slide",
        "lang": "zh"
    }
    headers = {
        "Accept": "*/*",
        "Accept-Language": "zh-CN,zh;q=0.9",
        "Cache-Control": "no-cache",
        "Connection": "keep-alive",
        "Pragma": "no-cache",
        "Referer": "https://gt4.geetest.com/",
        "Sec-Fetch-Dest": "script",
        "Sec-Fetch-Mode": "no-cors",
        "Sec-Fetch-Site": "same-site",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/138.0.0.0 Safari/537.36",
        "sec-ch-ua": "\"Not)A;Brand\";v=\"8\", \"Chromium\";v=\"138\", \"Google Chrome\";v=\"138\"",
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": "\"Windows\""
    }

    resp = requests.get(url=url,params=params,headers=headers,verify=False)

    # 验证接口请求所需参数
    verify_params = {
        'lot_number':lot_re.findall(resp.text)[0],
        'payload': payload_re.findall(resp.text)[0],
        'process_token': protk_re.findall(resp.text)[0],
        'pow_detail': json.loads(pow_detail_re.findall(resp.text)[0]),
        'captcha_id':params['captcha_id']
    }
    logger.debug(f'验证接口请求所需参数{verify_params}')

    # 拼接图片url
    base_url = 'https://static.geetest.com/'
    bg_url = base_url + bg_re.findall(resp.text)[0]
    slice_url = base_url + slice_re.findall(resp.text)[0]
    # 返回url和第二次请求所需参数
    return bg_url,slice_url,verify_params
'''
保存图片数据
'''
def save_img(bg_url,slice_url):
    bg_img = requests.get(bg_url).content
    with open('bg.png', 'wb+') as f:
        f.write(bg_img)
        f.close()
        logger.success('背景图保存成功')
    slice_img = requests.get(slice_url).content
    with open('slice.png', 'wb+') as f1:
        f1.write(slice_img)
        f1.close()
        logger.success('缺口图保存成功')
'''
获取识别距离
'''
def get_distance(bg_img, slice_img):
    det = ddddocr.DdddOcr(det=True, ocr=True)
    try:
        with open(slice_img, 'rb') as f:
            target_bytes = f.read()
        with open(bg_img, 'rb') as f:
            background_bytes = f.read()
    except:
        logger.error('图片打开失败')
    res = det.slide_match(target_bytes, background_bytes)
    logger.warning(f'ddddocr识别结果为：{res}')
    return int(res['target'][0] * 300 / 300.03)
def get_distance1(bg_img):
    recognizer = Recognizer()
    box, confidence = recognizer.identify_gap(source=bg_img, verbose=False)
    logger.warning(f'可信度为：{confidence}')
    return int((box[0] - 10) * 300 / 300.03)
'''
AES加密部分
'''
def get_aes_key():
    part = hex(int(65536 * (1.0 + random.random())))[2:].lower()[1:]
    part1 = hex(int(65536 * (1.0 + random.random())))[2:].lower()[1:]
    part2 = hex(int(65536 * (1.0 + random.random())))[2:].lower()[1:]
    part3 = hex(int(65536 * (1.0 + random.random())))[2:].lower()[1:]
    return part + part1 + part2 + part3
def encrypt_aes_cbc(plaintext: str, key_str: str, iv_str: str = "0000000000000000") -> str:
    """
    使用 AES-CBC 模式对字符串加密，并返回 hex 字符串。

    :param plaintext: 原始明文字符串
    :param key_str: 16 字节长度的密钥字符串
    :param iv_str: 16 字节长度的初始向量（默认全0）
    :return: 加密后的十六进制字符串
    """
    key = key_str.encode('utf-8')
    iv = iv_str.encode('utf-8')
    # 初始化加密器
    cipher = AES.new(key, AES.MODE_CBC, iv)
    # 对明文进行 PKCS7 填充
    padded = pad(plaintext.encode('utf-8'), AES.block_size)
    # 加密并转换为hex符串返回
    encrypted_bytes = cipher.encrypt(padded)
    # 二进制数据转换为可读的十六进制字符串表示形式
    return binascii.hexlify(encrypted_bytes).decode('utf-8')
def get_w(mingwen_str,aes_key):
    aes_part = encrypt_aes_cbc(mingwen_str, aes_key)
    logger.debug(f'aes_part为：{aes_part}')
    rsa_part = rsaencrypt_to_hex(aes_key)
    logger.debug(f'rsa_part为：{rsa_part}')
    return aes_part + rsa_part
def n_sign(e, t, s, n, i, r, o):
    a = i % 4
    _ = i // 4  # 计算需要的前缀0的数量
    u = '0' * _  # 生成前缀0字符串

    # 构建基础字符串
    c = f"{n}|{i}|{s}|{r}|{t}|{e}|{o}|"

    while True:
        # 生成GUID（UUID4）
        h = str(uuid.uuid4()).replace('-', '')

        # 构建待哈希的字符串
        p = f"{c}{h}"

        # 根据算法计算哈希值
        if s == "md5":
            hash_obj = hashlib.md5(p.encode())
        elif s == "sha1":
            hash_obj = hashlib.sha1(p.encode())
        elif s == "sha256":
            hash_obj = hashlib.sha256(p.encode())
        else:
            raise ValueError(f"不支持的哈希算法: {s}")

        l = hash_obj.hexdigest()  # 获取十六进制哈希结果

        # 检查前缀是否符合条件
        if l.startswith(u):
            # 当a为0时，只要前缀符合就返回
            if a == 0:
                return {
                    "pow_msg": f"{c}{h}",
                    "pow_sign": l
                }
            else:
                # 检查特定位置的字符是否符合条件
                if _ < len(l):
                    g = l[_]
                    # 转换为16进制数值
                    try:
                        g_val = int(g, 16)
                    except ValueError:
                        continue

                    # 根据a的值确定阈值
                    if a == 1:
                        f = 7
                    elif a == 2:
                        f = 3
                    elif a == 3:
                        f = 1
                    else:
                        continue  # 不应该发生

                    if g_val <= f:
                        return {
                            "pow_msg": f"{c}{h}",
                            "pow_sign": l
                        }
'''
最终验证部分
'''
def verify(captcha_id, lot_number, payload, process_token, pow_detail,distance,aes_key):
    headers = {
        "Accept": "*/*",
        "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6",
        "Cache-Control": "no-cache",
        "Connection": "keep-alive",
        "Pragma": "no-cache",
        "Referer": "https://gt4.geetest.com/",
        "Sec-Fetch-Dest": "script",
        "Sec-Fetch-Mode": "no-cors",
        "Sec-Fetch-Site": "same-site",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/138.0.0.0 Safari/537.36 Edg/138.0.0.0",
        "sec-ch-ua": "\"Not)A;Brand\";v=\"8\", \"Chromium\";v=\"138\", \"Microsoft Edge\";v=\"138\"",
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": "\"Windows\""
    }
    cookies = {
        "sensorsdata2015jssdkcross": "%7B%22distinct_id%22%3A%22197f9b515f2723-01bb97c620ba8a1-26011151-1327104-197f9b515f41c6%22%2C%22first_id%22%3A%22%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E7%9B%B4%E6%8E%A5%E6%B5%81%E9%87%8F%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC_%E7%9B%B4%E6%8E%A5%E6%89%93%E5%BC%80%22%2C%22%24latest_referrer%22%3A%22%22%2C%22%24latest_landing_page%22%3A%22https%3A%2F%2Fwww.geetest.com%2F%22%7D%2C%22%24device_id%22%3A%22197f9b515f2723-01bb97c620ba8a1-26011151-1327104-197f9b515f41c6%22%7D",
        "Hm_lvt_25b04a5e7a64668b9b88e2711fb5f0c4": "1752241086",
        "captcha_v4_user": "b5fd9164577840e4ac77530585fca390",
        "_uetvid": "46c6e7a05e5c11f0b3636bbf95cbb9c3"
    }
    url = "https://gcaptcha4.geetest.com/verify"

    result_obj = n_sign(lot_number, captcha_id, pow_detail['hashfunc'], pow_detail['version'],pow_detail['bits'] , pow_detail['datetime'], "")
    plaintext = {
        "setLeft": distance,
        "passtime": random.randint(1280,1900),
        "userresponse": distance / 1.0059466666666665 + 2, # 滑动距离 /1.0059466666666665 + 2,
        "device_id": "",
        "lot_number": lot_number,
        "pow_msg":result_obj['pow_msg'],
        "pow_sign":result_obj['pow_sign'],
        "geetest": "captcha",
        "lang": "zh",
        "ep": "123",
        "biht": "1426265548",
        "gee_guard": {
            "roe": {
                "aup": "3",
                "sep": "3",
                "egp": "3",
                "auh": "3",
                "rew": "3",
                "snh": "3",
                "res": "3",
                "cdc": "3"
            }
        },
        "W4Ec": "7RXi",
        # lot_number[21:25]: {
        #     lot_number[7:15]: {
        #         (lot_number[10:14] + lot_number[19:23]): lot_number[26:30]
        #     }
        # },####不校验
        "em": {
            "ph": 0,
            "cp": 0,
            "ek": "11",
            "wd": 1,
            "nt": 0,
            "si": 0,
            "sc": 0
        }
    }
    logger.warning(f"明文是==>>{plaintext}")
    w = get_w(json.dumps(plaintext,separators=(',',':'),ensure_ascii=False), aes_key)
    logger.debug(f"w值是==>>{w}")
    logger.critical(str(len(w)))
    params = {
        "callback": "geetest_" + str(int(time.time()*1000)),
        "captcha_id": captcha_id,
        "client_type": "web",
        "lot_number": lot_number,
        "risk_type": "slide",
        "payload": payload,
        "process_token": process_token,
        "payload_protocol": "1",
        "pt": "1",
        "w": w
    }
    logger.warning(params)
    response = requests.get(url, headers=headers, cookies=cookies, params=params)
    logger.success(f'验证结果是==>>{response.text}')
    result_obj = json.loads(response.text[22:-1])
    logger.debug(result_obj['data']['result'])
def run():
    bg_url,slice_url,verify_params = get_imgurl_and_verify_params('slide')
    #保存 图片
    save_img(bg_url, slice_url)
    # time.sleep(6)
    # distance = get_distance('bg.png','slice.png')
    distance = get_distance1('bg.png')
    # distance = get_slide_distance('bg.png','slice.png') - 2
    logger.warning(f'距离是==>>{distance}')
    aes_key = get_aes_key()
    logger.debug(f"aes_key是==>>{aes_key}")
    logger.debug(verify_params)
    verify(verify_params['captcha_id'], verify_params['lot_number'], verify_params['payload'], verify_params['process_token'], verify_params['pow_detail'],distance,aes_key)
if __name__ == '__main__':
    run()

