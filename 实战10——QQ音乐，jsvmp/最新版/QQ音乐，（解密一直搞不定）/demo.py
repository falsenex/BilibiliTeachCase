import base64
import re
from hashlib import sha1
from base64 import b64encode

import execjs
import requests
from loguru import logger

def get_sign(mingwen_str):
    arr1 = [23, 14, 6, 36, 16, 7, 19]
    arr2 = [16, 1, 32, 12, 19, 27, 8, 5]
    arr3 = [89, 39, 179, 150, 218, 82, 58, 252, 177, 52, 186, 123, 120, 64, 242, 133, 143, 161, 121, 179]
    dict_hex = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, 'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14,'F': 15}
    sha1_str = sha1(mingwen_str.encode()).hexdigest().upper()

    first_str = ''.join(map(lambda i: sha1_str[i], arr1))
    last_str = ''.join(map(lambda i: sha1_str[i], arr2))
    result = []
    # for i in range(len(arr3)):
    i = 0
    while i < len(sha1_str):
        result.append(((dict_hex[sha1_str[i]] * 16) + dict_hex[sha1_str[i+1]]) ^ arr3[i//2])
        i += 2
    medium_str = re.sub(r'[\\+/=]', '', b64encode(bytes(result)).decode())
    return ('zzc' + first_str + medium_str + last_str).lower()

import requests

cookies = {
    'ts_refer': 'cn.bing.com/',
    'ts_uid': '9834888193',
    'pgv_pvid': '4614023088',
    'fqm_pvqid': 'b0ecafa7-a2aa-4429-a8e8-4d38be610dde',
    'fqm_sessionid': '4df9817b-dc10-4902-917d-62e3cd905816',
    'pgv_info': 'ssid=s4044287357',
}
headers = {
    'accept': 'application/octet-stream',
    'accept-language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
    'cache-control': 'no-cache',
    'content-type': 'text/plain',
    'origin': 'https://y.qq.com',
    'pragma': 'no-cache',
    'priority': 'u=1, i',
    'referer': 'https://y.qq.com/',
    'sec-ch-ua': '"Not;A=Brand";v="99", "Microsoft Edge";v="139", "Chromium";v="139"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-site',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/139.0.0.0 Safari/537.36 Edg/139.0.0.0',
    # 'cookie': 'ts_refer=cn.bing.com/; ts_uid=9834888193; pgv_pvid=4614023088; fqm_pvqid=b0ecafa7-a2aa-4429-a8e8-4d38be610dde; fqm_sessionid=4df9817b-dc10-4902-917d-62e3cd905816; pgv_info=ssid=s4044287357; ts_last=y.qq.com/n/ryqq/toplist/4',
}

params = {
    '_': '1754980434299',
    'encoding': 'ag-1',
    # 'sign': 'zzc50e04d3pzb2e9lscjlyedxcq32r0ebq44e33705',
}
mw_str = '{"comm":{"cv":4747474,"ct":24,"format":"json","inCharset":"utf-8","outCharset":"utf-8","notice":0,"platform":"yqq.json","needNewCode":1,"uin":0,"g_tk_new_20200303":5381,"g_tk":5381},"req_1":{"module":"musicToplist.ToplistInfoServer","method":"GetDetail","param":{"topid":26,"offset":0,"num":20,"period":"2025-08-12"}}}'
params['sign'] = get_sign(mw_str)
logger.debug(params)
data_str = execjs.compile(open('encrypt.js', 'r',encoding='utf-8').read()).call('encryptSyncToBase64',mw_str)
data = data_str
response = requests.post('https://u6.y.qq.com/cgi-bin/musics.fcg', params=params, cookies=cookies,
                         headers=headers, data=data)
b64 = base64.b64encode(response.content).decode('utf-8')
logger.debug(b64)
# decryptData = execjs.compile(open('decrypt.js', 'r',encoding='utf-8').read()).call('decryptSyncFromBase64',b64)