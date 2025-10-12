#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
@Project ：pythonProject 
@File    ：demo.py
@IDE     ：PyCharm 
@Author  ：haozaispider
@Date    ：2025/6/16 下午4:14 
'''
import execjs
import requests
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad
import json
import random
from loguru import logger

def get_session_id(paras_json):
    # 密钥和初始向量
    aQ = b'8080808080808080'
    # 创建 AES 加密器，使用 CBC 模式
    cipher = AES.new(aQ, AES.MODE_CBC, aQ)
    # 对数据进行填充并加密
    encrypted = cipher.encrypt(pad(json.dumps(paras_json).encode('utf-8'), AES.block_size)).hex()

    # 拼接字符串和随机数
    return encrypted[:50] + str(random.random())

headers = {
    "Accept": "application/json, text/plain, */*",
    "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6",
    "Cache-Control": "no-cache",
    "Connection": "keep-alive",
    "Origin": "https://greenafrica.com",
    "Pragma": "no-cache",
    "Referer": "https://greenafrica.com/",
    "Sec-Fetch-Dest": "empty",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Site": "same-site",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/137.0.0.0 Safari/537.36 Edg/137.0.0.0",
    "sec-ch-ua": "\"Microsoft Edge\";v=\"137\", \"Chromium\";v=\"137\", \"Not/A)Brand\";v=\"24\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"Windows\"",
    "signature": "C581D6C0A9DBBCFDAB9988578D87F95BTIKHQOGBVE2NH5UJSAIX"
}
url = "https://middleware.greenafrica.com/api/booking/getDeepLink"
params = {
    "from": "ABV",
    "to": "IBA",
    "start": "2025/06/16",
    "adults": "1",
    "child": "0",
    # "session_id": "gGO5rDWPDcqaAgDFMJkyurlLLGEhhqKjIZ4YC0lvPYyCLrwWmi0.8405042794070409",
    "infant": "0",
    "end": "2025/06/19",
    "currency": "NGN",
    "cabinCode": "ECO"
}
session_id = get_session_id(params)
logger.debug("生成的session_id: " + session_id)
params["session_id"] = session_id
response = requests.get(url, headers=headers, params=params)
if response.json()['success'] == True:
    logger.success("成功获取到数据: " + str(response.json()))
else:
    logger.error("获取数据失败，错误信息: " + str(response.json()['message']))

