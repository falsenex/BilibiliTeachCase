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



def get_challenge():
    url = "https://aq.99.com/V5/Handler/Default.ashx"
    data = {
        'Action': "checkcodeinit",
        'Data': '050a9850b04fc9372cf0b7b530bec782',
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

if __name__ == '__main__':
    challenge = get_challenge()
    print(get_img_infos(challenge))