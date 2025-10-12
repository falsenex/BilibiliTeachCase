#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
@Project ：pythonProject 
@File    ：final.py
@IDE     ：PyCharm 
@Author  ：haozaispider
@Date    ：2025/6/30 下午2:53 
'''
import hashlib
import random
import string
import requests
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_v1_5
import base64
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad
from loguru import logger
from userinfo import username,password
def get_encrypt_password(passwd_mingwen):
    return hashlib.md5(passwd_mingwen.encode('utf-8')).hexdigest().upper()
def get_EUI_user(t):
    # 将字典的键用逗号连接成字符串
    keys_string = ','.join(t.keys())
    # 进行 Base64 编码 (对应 JavaScript 的 btoa 函数)
    u = base64.b64encode(keys_string.encode('utf-8')).decode('ascii')
    e = ''.join(random.choices(string.ascii_letters + string.digits + '!@#$%^&*', k=16))
    """
    RSA 加密
    """
    # 公钥（从JavaScript代码中提取）
    public_key_pem = """
        -----BEGIN PUBLIC KEY-----
        MIGfMA0GCSqGSIb3DQEBAQUAA4GNADCBiQKBgQCYEVrK/4Mahiv0pUJgTybx4J9P5dUT/Y0PuwMbk+gMU+jrZnBiXGv6/hCH1avIhoBcE535F8nJQQN3UavZdFkYidsoXuEnat3+eVTp3FslyhRwIBDF09v4vDhRtxFOT+R7uH7h/mzmyA2/+lfIMWGIrffXprYizbV76+YQKhoqFQIDAQAB
        -----END PUBLIC KEY-----
        """.strip()

    # 待加密的数据（从之前生成的随机字符串e）
    # 注意：这里需要使用之前生成的e变量的值
    # 示例：e = "之前生成的随机字符串"

    # 对数据进行Base64编码（对应JavaScript中的btoa函数）
    data_base64 = base64.b64encode(e.encode('utf-8')).decode('utf-8')
    # 加载公钥并创建加密器
    public_key = RSA.import_key(public_key_pem)
    cipher = PKCS1_v1_5.new(public_key)
    # 加密数据
    encrypted_bytes = cipher.encrypt(data_base64.encode('utf-8'))
    r = base64.b64encode(encrypted_bytes).decode('utf-8')

    """
    AES加密
    """
    # 创建加密所需的 IV (从字符串 "0102030405060708" 转换而来)
    # 初始向量 IV（UTF-8 编码的 16 字节字符串）
    iv = "0102030405060708".encode('utf-8')
    key = e.encode('utf-8')
    # 初始化结果字典
    c = {}

    # 遍历字典 t 并加密每个值
    for e, i in t.items():
        # 将值转换为字节并填充到 16 字节的倍数
        data = i.encode('utf-8')
        padded_data = pad(data, AES.block_size)

        # 创建 AES 加密器
        cipher = AES.new(key, AES.MODE_CBC, iv)

        # 执行加密并转换为 Base64 字符串
        encrypted_bytes = cipher.encrypt(padded_data)
        encrypted_base64 = base64.b64encode(encrypted_bytes).decode('utf-8')

        # 存储到结果字典
        c[e] = encrypted_base64
    return {
        'EUI':r + "." + u,
        'encryptedParams': c
    }
def login(username,password):
    headers = {
        "Accept": "application/json, text/plain, */*",
        "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6",
        "Cache-Control": "no-cache",
        "Connection": "keep-alive",
        "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
        # "EUI": "eAgpuLO74fU8n+/NO8uoNiv+KcbPyi8EbcTDlFlN2+hmFsKpJXNgI/YTgLy7HVpc5z0agtQsXWXYMvNfm0sFUVo76yS8/4GB0Ajj7CsePG4076kHxC3znlwIhkhLhVT2icQKr5YLTBYdsPGhEXynzDqLs4fTVBR5vmZcLV37svk=.dXNlcg==",
        "Origin": "https://account.xiaomi.com",
        "Pragma": "no-cache",
        "Referer": "https://account.xiaomi.com/fe/service/login/password?_locale=zh_CN&sid=passport&qs=%253F_locale%253Dzh_CN&callback=https%3A%2F%2Faccount.xiaomi.com&_sign=2%26V1_passport%26x0slRayyS8cW7cG2GEXdLdeYk6A%3D&serviceParam=%7B%22checkSafePhone%22%3Afalse%2C%22checkSafeAddress%22%3Afalse%2C%22lsrp_score%22%3A0.0%7D&showActiveX=false&theme=&needTheme=false&bizDeviceType=",
        "Sec-Fetch-Dest": "empty",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Site": "same-origin",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/138.0.0.0 Safari/537.36 Edg/138.0.0.0",
        "X-Requested-With": "XMLHttpRequest",
        "sec-ch-ua": "\"Not)A;Brand\";v=\"8\", \"Chromium\";v=\"138\", \"Microsoft Edge\";v=\"138\"",
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": "\"Windows\""
    }
    cookies = {
        "deviceId": "wb_993675ec-cd35-447b-af57-9f82e32fc8c9",
        "pass_ua": "web",
        "uLocale": "zh_CN"
    }
    url = "https://account.xiaomi.com/pass/serviceLoginAuth2"
    data = {
        "bizDeviceType": "",
        "needTheme": "false",
        "theme": "",
        "showActiveX": "false",
        "serviceParam": "{\"checkSafePhone\":false,\"checkSafeAddress\":false,\"lsrp_score\":0.0}",
        "callback": "https://account.xiaomi.com",
        "qs": "%3F_locale%3Dzh_CN",
        "sid": "passport",
        # "_sign": "2&V1_passport&x0slRayyS8cW7cG2GEXdLdeYk6A=",
        # "user": "TNz53jhQANxiWH64u4M0Og==",
        "cc": "+86",
        # "hash": "CB0495E9A9B008C797261E9BA4B5228F",
        "_json": "true",
        "policyName": "miaccount",
        "captCode": ""
    }
    paras = get_EUI_user({"user": username})
    logger.debug(f'EUI&encryptedParams===>>>{paras}')
    hash = get_encrypt_password(password)
    logger.debug(f'hash===>>>{hash}')
    data["user"] = paras["encryptedParams"]["user"]
    data["hash"] = hash
    headers["EUI"] = paras["EUI"]
    response = requests.post(url, headers=headers, cookies=cookies, data=data)
    logger.success(response.text)
if __name__ == '__main__':
    login(username, password)
