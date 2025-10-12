import requests
import json
import execjs
from loguru import logger
from datetime import datetime
ts = int(datetime.now().timestamp() * 1000)

headers = {
    "Accept": "application/json, text/plain, */*",
    "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6",
    "Connection": "keep-alive",
    "Content-Type": "application/json;charset=UTF-8",
    "Origin": "https://ggzyfw.fujian.gov.cn",
    "Referer": "https://ggzyfw.fujian.gov.cn/business/list",
    "Sec-Fetch-Dest": "empty",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Site": "same-origin",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36 Edg/129.0.0.0",
    #"portal-sign": "18f44d7764469fa206513858d042802e",
    "sec-ch-ua": "\"Microsoft Edge\";v=\"129\", \"Not=A?Brand\";v=\"8\", \"Chromium\";v=\"129\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"Windows\""
}
url = "https://ggzyfw.fujian.gov.cn/FwPortalApi/Trade/TradeInfo"
data = {
    "pageNo": 2,
    "pageSize": 20,
    "total": 3704,
    "AREACODE": "",
    "M_PROJECT_TYPE": "",
    "KIND": "GCJS",
    "GGTYPE": "1",
    "PROTYPE": "",
    "timeType": "6",
    "BeginTime": "2024-03-29 00:00:00",
    "EndTime": "2024-09-29 23:59:59",
    "createTime": [],
    "ts": ts
}

sign = execjs.compile(open('./demo.js', 'r', encoding='utf-8').read()).call('get_sign', data)
logger.info('sign参数 === 》》》 ' + sign)
headers["portal-sign"] = sign
data = json.dumps(data, separators=(',', ':'))
response = requests.post(url, headers=headers, data=data)
logger.info('密文数据===》》》 ' + str(response.json()['Data']))

decrypt_data = execjs.compile(open('./demo.js', 'r', encoding='utf-8').read()).call('decrypt_data', response.json()['Data'])
logger.info('明文数据 === 》》》 ' + decrypt_data)


