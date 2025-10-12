'''
查看initiators，发现有Promise对象，且出现了async关键字，是异步加载。
大概率采用的是axios，加密过程很有可能是在拦截器中实现的，所以直接全局搜索"interceptors"。
'''
import urllib.parse
import execjs
import requests
from loguru import logger
headers = {
    "Accept": "application/json, text/plain, */*",
    "Accept-Language": "zh-CN,zh;q=0.9",
    "Cache-Control": "no-cache",
    "Connection": "keep-alive",
    "Pragma": "no-cache",
    "Referer": "https://ctbpsp.com/",
    "Sec-Fetch-Dest": "empty",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Site": "same-origin",
    "Server": "https://0.vaptcha.com/verify",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/138.0.0.0 Safari/537.36",
    "V-Token": "1755520698E0kqPbf554e",
    "sec-ch-ua": "\"Not)A;Brand\";v=\"8\", \"Chromium\";v=\"138\", \"Google Chrome\";v=\"138\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"Windows\""
}
cookies = {
    "acw_tc": "1a0c66d517560428770327387efa693b03b7304a54e67c429e896f4a03d836",
    "Hm_lvt_b966fe201514832da03dcf6cbf25b8a2": "1756042891",
    "Hm_lpvt_b966fe201514832da03dcf6cbf25b8a2": "1756042891",
    "HMACCOUNT": "25ACB4D055C35DBA",
    "ssxmod_itna": "QqAODKD50KYvqYu4eKYIF4iK7Qi=vqGR+Dl4BUiD2DIdq7=GFGDCO7U43wj4BIUpqeGmBhN4Mtj75D/fnheDZDGKQDqx0ob0YmB0UPltn2OpIiBcARUtqFjmxhI1KUebvedNmH/DlQS0vkoWhbqi4DHxi8DB9Diib4mDiiHx0rD0eDPxDYDG4Do6YDnP4DjxDdkK3Ep9oDbxi3k4iaDGeDe6OpDYyeDDvWoU23kUD4zzDDBx4YqmOqDYmjyIBUhjhAqCkPajoD964DscrB5jEX+T/xEzL9CqMba40kRq0OpK+fdU2QzUfE0+eiYtqmezOYmDia7DaGYeBD6gYtExw25KTo4gq9gx4O5KnwzxDihecAeXiD4r+gONlEN/xomlISQTXQDzYx2jGeGK79wseeYnDen0YchKnGPiGktvNKWxD",
    "ssxmod_itna2": "QqAODKD50KYvqYu4eKYIF4iK7Qi=vqGR+Dl4BUiD2DIdq7=GFGDCO7U43wj4BIUpqeGmBhN4MtjGeDA92kDNb1BcD031GDE3hKVD05j3apa6Rh3Gc3z0D0effp=7ukLF7U9P9kNB8g3oBaPSch1x8FsilKx1Bc5apG1iBPNSxThaQiqz=G70eoxeBciwPg1alKQZ1vpLc9k5WF5ApO1qQof96yA2UfABALCXgSCaPLO5BFshOvAf8PuR1g72gjvaMajQv0m8v5Ntt98=Rqc9rLFf9jGpqukyxhvS1fvLhL2a6iG2bpzBnrwfHgUwyzymbHvFHmWcf8TPU9Dkqn+ySDKqu58bPe+YvAFqPmBIvAnK1mw8Gu4DvIKKwGqNDmHBR700UbYQARUU07SGamq1WP9fHhmqo5fu3mQK8kYT7KAubyG9pS4u5v8UmFSeO9Ku5Z9UlS1STh80IeTo5O0ePWNy4+gQuEBFq8VnSnIEF3iSqNGijI+/CkjG05+OMQfk4R7Y04nbl+DXe55w87K36bcqpmGF9pMmGiSI1Yb=cZCGabGNIqxFBPDaHDTh+umGhzzHkXoC0QQj4jvwO26e4FjrD/UP7l5YigI4qEm67YdB7SfSIgYU9Sqi93Ob=9Pw9NI1/kX0jaU3eYr4Ki4tDoetKt9xBrjtsSgWuTsOzsjF0XtKxz4me+1lbGuph3/H4DGWhGe7e02GP/TN0OHI+nGV94WxmDoAz8AggeViiDx=D4DYoiKF+qDoWz5GDD"
}
url = "https://ctbpsp.com/cutominfoapi/recommand/type/5/pagesize/10/currentpage/1"

params = {
    "province": "",
    "industry": ""
}
para = url + '?' + urllib.parse.urlencode(params)
type_1017 = execjs.compile(open("./demo.js", mode="r", encoding="utf-8").read()).call('get_para',para)
logger.debug('加密参数type_1017 ===》》》 ' + type_1017)
params['type__1017'] = type_1017
resp = requests.get(url, headers=headers, cookies=cookies, params=params)
logger.info('密文数据 ===》》》 ' + resp.text)
result = execjs.compile(open("./demo.js", mode="r", encoding="utf-8").read()).call('decrypt_data', resp.text.strip('"'))
logger.success('明文数据 ===》》》 ' + str(result["data"]))







