import json
import requests
import execjs
from loguru import logger
headers = {
    "accept": "application/json, text/plain, */*",
    "accept-language": "zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6",
    "cache-control": "no-cache",
    "content-type": "application/x-www-form-urlencoded",
    "origin": "https://open.x7sy.com",
    "pragma": "no-cache",
    "priority": "u=1, i",
    "referer": "https://open.x7sy.com/",
    "sec-ch-ua": "\"Not)A;Brand\";v=\"8\", \"Chromium\";v=\"138\", \"Microsoft Edge\";v=\"138\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"Windows\"",
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "same-origin",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/138.0.0.0 Safari/537.36 Edg/138.0.0.0",
    # "web-x7sy-dev": "browserId=BjpNcdQTrPKiszwCiZRraTBj97235127&isForeign=-1&language=1&sign=fd72a67edfd64040577cc3939a51d1f8",
    "x7-debug-token;": ""
}
web_x7sy_dev  = execjs.compile(open('final.js','r',encoding='utf-8').read()).call('get_web_x7sy_dev')
logger.debug(f"web_x7sy_dev参数:{web_x7sy_dev}")
headers["web-x7sy-dev"] = web_x7sy_dev
cookies = {
    "x-hng": "lang=zh-CN&domain=open.x7sy.com",
    "x7sy_session": "f726b9c76dead978ba6a62c397fd90cae4981b45",
    "acw_tc": "0a47308c17542074848616968e15b4eef3f2c26ee8c72bc901ebb216bf974b"
}
url_data_obj = execjs.compile(open('final.js', 'r',encoding='utf-8').read()).call('get_url_data')
url = "https://open.x7sy.com" + url_data_obj['url_part']
data = {
    "c": url_data_obj['c'],
    "r": url_data_obj['r'],
    "t": url_data_obj['t'],
    "s": url_data_obj['s'],
}
logger.info(f"负载参数：{data}")
response = requests.post(url, headers=headers, cookies=cookies, data=data)
logger.warning(f"响应密文：{response.text}")
mingwen = execjs.compile(open('final.js', 'r',encoding='utf-8').read()).call('decrypt',response.text)
logger.success(f"明文数据==》》{mingwen}")