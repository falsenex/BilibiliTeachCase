import json
import time
from urllib import parse
import requests
from hashlib import md5
from loguru import logger
def get_check(arg1,ts,url):
    return md5(
        ("Wanda"+arg1+
         'FA425A3F9F5FFFC4389994548F83298776F8B46B752A83A6A798C6ED8FE8BFE1'
         +str(ts)+url).encode()
    ).hexdigest()

headers = {
    'Accept': '*/*',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/133.0.0.0 Safari/537.36',
}

params = {
    'cityId': '354',
    'cinemaId': '651',
    'day': '0',
}

part_url = "/movie/hot_show.api?"+parse.urlencode(params)
ts = int(time.time()*1000)
cCode="1_3"
headers.update({
    'MX-API':json.dumps({
        "ver":"7.0.0",
        "sCode":"Wanda",
        "_mi_":"",
        "width":1280,
        "json":True,
        "cCode":cCode,
        "check":get_check(cCode,ts,part_url),
        "ts":ts,
        "heigth":720,
        "appId":"3"
    },separators=(',',':')),
})

response = requests.get('https://cinema-api-prd-mx.wandafilm.com'+part_url,  headers=headers)
logger.info(response.text)