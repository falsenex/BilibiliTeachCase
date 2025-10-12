from loguru import logger
from requests import Session
import json,re,execjs

proxies = {
    'https':'http://127.0.0.1:7890',
    'http':'http://127.0.0.1:7890'
}

requests = Session()
requests.headers = {
    "authority": "www.koreaf3.com",
    "accept": "application/json, text/plain, */*",
    "accept-language": "zh-CN,zh;q=0.9,en-GB;q=0.8,en;q=0.7",
    "cache-control": "no-cache",
    "content-type": "application/json",
    "origin": "https://www.koreaf3.com",
    "pragma": "no-cache",
    "referer": "https://www.koreaf3.com/result",
    "sec-ch-ua": "\"Not=A?Brand\";v=\"99\", \"Chromium\";v=\"118\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"Windows\"",
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "same-origin",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; JiSu) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.3.1.7 Safari/537.36"
}

html = requests.get("https://www.koreaf3.com/",proxies=proxies)
__NUXT__= re.findall('window.__NUXT__=(.*?);</script>',html.text)[0]
with open('./__NUXT__.js','w',encoding='utf-8') as f:
    f.write('window.__NUXT__ = '+__NUXT__)


url = "https://www.koreaf3.com/api/result_num"
data = {
    "Action": "ResultHistory",
    "Date": "2025-09-11",
    "Page": 1,
    "PageSize": 85,
    "GameCode": "KF"
}
data = execjs.compile(open('./koreaf3.js','r',encoding='utf-8').read()).call('get_data',data)
logger.debug(f"data加密参数：{data}")
data = json.dumps(data, separators=(',', ':'))
response = requests.post(url, data=data,proxies=proxies)
datastr = response.json()['data']
data = execjs.compile(open('./koreaf3.js','r',encoding='utf-8').read()).call('decrypt_data',datastr)
logger.success(f"明文：{data}")