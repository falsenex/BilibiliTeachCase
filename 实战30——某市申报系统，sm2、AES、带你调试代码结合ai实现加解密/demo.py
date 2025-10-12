#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
@Project ：pythonProject 
@File    ：demo.py
@IDE     ：PyCharm 
@Author  ：haozaispider
@Date    ：2025/7/4 上午9:52 
'''
import json
import requests
import execjs  # 必须在修改编码后引入
from loguru import logger

headers = {
    "Accept": "application/json, text/javascript, */*; q=0.01",
    "Accept-Language": "zh-CN,zh;q=0.9",
    "Connection": "keep-alive",
    "Content-Type": "application/json;charset=UTF-8",
    "Origin": "http://120.211.111.206:8090",
    "Referer": "http://120.211.111.206:8090/xjzwdt/xjzwdt/pages/info/policy",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/137.0.0.0 Safari/537.36",
    "X-Requested-With": "XMLHttpRequest",
    "encrypt": "1"
}
url = "http://120.211.111.206:8090/xjzwdt/rest/xmzInfoDeliveryRest/getInfoDeliveryList"
params = {
    "foreSessionClusterIntercept": "true"
}
post_data = {
    "token":"Epoint_WebSerivce_**##0601",
    "params":{
        "categuids":"6d8c8eaa-c710-4b96-b26f-ce3dfc519b77,4bcbbec7-2428-403a-8eed-b0db5c0e01a5,",
        "titlename":"",
        "currpage":3,
        "pagesize":10
    }
}
logger.debug(f"encrypt data===>>>{json.dumps(post_data, separators=(',', ':'))}")
data = execjs.compile(open('demo.js', 'r', encoding='utf-8').read()).call('encrypt', json.dumps(post_data, separators=(',', ':')))
logger.warning(f'encrypt result===>>>{data}')
response = requests.post(url, headers=headers, params=params, data=data, verify=False)
logger.debug(f'request result===>>>{response.text}')
decrypt_result = execjs.compile(open('demo.js', 'r', encoding='utf-8').read()).call('aesDecrypt', response.text)
logger.success(f'decrypt result===>>>{decrypt_result}')

