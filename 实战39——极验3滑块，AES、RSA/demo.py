# https://www.52pojie.cn/thread-2055730-1-1.html
import base64
import binascii
import hashlib
import json
import math
import random
import ddddocr
import execjs
from Crypto.Cipher import PKCS1_OAEP, PKCS1_v1_5
from Crypto.PublicKey import RSA
from PIL import Image
import requests
import time
import secrets
from loguru import logger
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad
# from 轨迹生成 import get_slide_track
headers = {
    "Accept": "*/*",
    "Accept-Language": "zh-CN,zh;q=0.9",
    "Cache-Control": "no-cache",
    "Connection": "keep-alive",
    "Pragma": "no-cache",
    "Referer": "https://demos.geetest.com/",
    "Sec-Fetch-Dest": "script",
    "Sec-Fetch-Mode": "no-cors",
    "Sec-Fetch-Site": "cross-site",
    "Sec-Fetch-Storage-Access": "active",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/138.0.0.0 Safari/537.36",
    "sec-ch-ua": "\"Not)A;Brand\";v=\"8\", \"Chromium\";v=\"138\", \"Google Chrome\";v=\"138\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"Windows\""
}
cookies = {
        "sensorsdata2015jssdkcross": "%7B%22distinct_id%22%3A%22197f9b515f2723-01bb97c620ba8a1-26011151-1327104-197f9b515f41c6%22%2C%22first_id%22%3A%22%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E7%9B%B4%E6%8E%A5%E6%B5%81%E9%87%8F%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC_%E7%9B%B4%E6%8E%A5%E6%89%93%E5%BC%80%22%2C%22%24latest_referrer%22%3A%22%22%2C%22%24latest_landing_page%22%3A%22https%3A%2F%2Fwww.geetest.com%2F%22%7D%2C%22%24device_id%22%3A%22197f9b515f2723-01bb97c620ba8a1-26011151-1327104-197f9b515f41c6%22%7D",
        "Hm_lvt_25b04a5e7a64668b9b88e2711fb5f0c4": "1752241086",
        "_uetvid": "46c6e7a05e5c11f0b3636bbf95cbb9c3"
    }
'''
RSA加密部分
'''
# 从PEM格式或模数/指数对加载RSA公钥
def load_public_key(pem_key=None, modulus=None, exponent=None):
    if pem_key:
        # 清理PEM格式，移除换行和空格，并提取实际密钥部分
        cleaned = pem_key.replace("\n", "").replace(" ", "")
        if "-----" in cleaned:
            cleaned = [part for part in cleaned.split("-----") if len(part) > 25][0]
        key_bytes = base64.b64decode(cleaned)
        return RSA.importKey(key_bytes)

    elif modulus and exponent:
        # 从16进制字符串或整数形式的模数和指数构造RSA公钥
        n = int(modulus, 16) if isinstance(modulus, str) else modulus
        e = int(exponent, 16) if isinstance(exponent, str) else exponent
        return RSA.construct((n, e))

    raise ValueError("必须提供 PEM 公钥或 modulus + exponent")
# 根据指定的填充模式获取加密器对象
def get_cipher(key_obj, padding_mode: int):
    scheme = {
        1: PKCS1_OAEP.new,  # OAEP填充（推荐）
        2: PKCS1_v1_5.new   # 传统的PKCS#1 v1.5填充
    }
    if padding_mode not in scheme:
        raise ValueError("padding_mode 只支持 1（OAEP）或 2（v1_5）")
    return scheme[padding_mode](key_obj)
# 加密字节数据
def encrypt_bytes(plaintext: str, *, pem_key=None, modulus="00C1E3934D1614465B33053E7F48EE4EC87B14B95EF88947713D25EECBFF7E74C7977D02DC1D9451F79DD5D1C10C29ACB6A9B4D6FB7D0A0279B6719E1772565F09AF627715919221AEF91899CAE08C0D686D748B20A3603BE2318CA6BC2B59706592A9219D0BF05C9F65023A21D2330807252AE0066D59CEEFA5F2748EA80BAB81", exponent="10001", padding_mode=2) -> bytes:
    key_obj = load_public_key(pem_key=pem_key, modulus=modulus, exponent=exponent)
    cipher = get_cipher(key_obj, padding_mode)
    encrypted_data = cipher.encrypt(plaintext.encode())
    return encrypted_data
# 将加密结果转换为16进制字符串
def rsaencrypt_to_hex(plaintext: str, **kwargs) -> str:
    return binascii.hexlify(encrypt_bytes(plaintext, **kwargs)).decode()
'''
AES加密部分
'''
js = '''
        var i = {
            '_BIGCu': function (e, t) {
                return e >> t & 1;
            },
            '_BIFIK': function (e) {
                var t = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789()"
                return e < 0 || e >= t["length"] ? "." : t["charAt"](e);
            }
        }

        function get_w(e) {
            for (var t = function(e, t) {
                for (var n = 0, r = 23; 0 <= r; r -= 1)
                    1 === i['_BIGCu'](t, r) && (n = (n << 1) + i['_BIGCu'](e, r));
                return n;
            }, n = '', r = '', s = e['length'], a = 0; a < s; a += 3) {
                var _;
                if (a + 2 < s)
                    _ = (e[a] << 16) + (e[a + 1] << 8) + e[a + 2],
                    n += i['_BIFIK'](t(_, 7274496)) + i['_BIFIK'](t(_, 9483264)) + i['_BIFIK'](t(_, 19220)) + i['_BIFIK'](t(_, 235));
                else {
                    var c = s % 3;
                    2 == c ? (_ = (e[a] << 16) + (e[a + 1] << 8),
                    n += i['_BIFIK'](t(_, 7274496)) + i['_BIFIK'](t(_, 9483264)) + i['_BIFIK'](t(_, 19220)),
                    r = '.') : 1 == c && (_ = e[a] << 16,
                    n += i['_BIFIK'](t(_, 7274496)) + i['_BIFIK'](t(_, 9483264)),
                    r = '..');
                }
            }
            return n + r;
        }
    '''
def get_aes_key():
    part = hex(int(65536 * (1 + secrets.SystemRandom().random())))[2:-1]
    part1 = hex(int(65536 * (1 + secrets.SystemRandom().random())))[2:-1]
    part2 = hex(int(65536 * (1 + secrets.SystemRandom().random())))[2:-1]
    part3 = hex(int(65536 * (1 + secrets.SystemRandom().random())))[2:-1]
    return part + part1 + part2 + part3
def encrypt_aes_cbc(plaintext: str, key_str: str, iv_str: str = "0000000000000000") -> list:
    """
    使用 AES-CBC 模式对字符串加密，并返回 hex 字符串。

    :param plaintext: 原始明文字符串
    :param key_str: 16 字节长度的密钥字符串
    :param iv_str: 16 字节长度的初始向量（默认全0）
    :return: 加密后的十六进制字符串
    """
    key = key_str.encode('utf-8')
    iv = iv_str.encode('utf-8')
    # 初始化加密器
    cipher = AES.new(key, AES.MODE_CBC, iv)
    # 对明文进行 PKCS7 填充
    # 对输入进行填充
    padded_data = pad(plaintext.encode('utf-8'), AES.block_size)

    # 加密数据
    encrypted_data = cipher.encrypt(padded_data)

    # 将加密后的数据转换为字节列表
    byte_list = list(encrypted_data)

    return byte_list
def get_w1(mingwen_str,aes_key):
    aes_encrypt_list = encrypt_aes_cbc(mingwen_str, aes_key)
    aes_part = execjs.compile(js).call('get_w', aes_encrypt_list)
    rsa_part = rsaencrypt_to_hex(aes_key)
    return aes_part + rsa_part
def get_w2(mingwen_str,aes_key):
    aes_encrypt_list = encrypt_aes_cbc(mingwen_str, aes_key)
    return execjs.compile(js).call('get_w', aes_encrypt_list)
def get_w3(mingwen_str,aes_key):
    aes_encrypt_list = encrypt_aes_cbc(mingwen_str, aes_key)
    # aes_encrypt_list = encrypt_aes_cbc(mingwen_str, "85300d392711e07a")
    aes_part = execjs.compile(js).call('get_w', aes_encrypt_list)
    rsa_part = rsaencrypt_to_hex(aes_key)
    return aes_part + rsa_part
def get_rp(plaintext: str):
    return hashlib.md5(plaintext.encode('utf-8')).hexdigest()
'''
流程
'''
def get_gt_challenge():
    url = "https://demos.geetest.com/gt/register-slide"
    params = {
        "t": str(int(time.time() * 1000))
    }
    response = requests.get(url, headers=headers, cookies=cookies, params=params)
    return response.json()
def gettype(gt_challenge_obj):
    url = "https://apiv6.geetest.com/gettype.php"
    params = {
        "gt": gt_challenge_obj['gt'],
        "callback": f"geetest_{int(time.time() * 1000)}"
    }
    response = requests.get(url, headers=headers, cookies=cookies, params=params)
    logger.debug(response.text)
def get(gt_challenge_obj,aes_key):
    url = "https://apiv6.geetest.com/get.php"
    cookies = {
        "sensorsdata2015jssdkcross": "%7B%22distinct_id%22%3A%22197f9b515f2723-01bb97c620ba8a1-26011151-1327104-197f9b515f41c6%22%2C%22first_id%22%3A%22%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E7%9B%B4%E6%8E%A5%E6%B5%81%E9%87%8F%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC_%E7%9B%B4%E6%8E%A5%E6%89%93%E5%BC%80%22%2C%22%24latest_referrer%22%3A%22%22%2C%22%24latest_landing_page%22%3A%22https%3A%2F%2Fwww.geetest.com%2F%22%7D%2C%22%24device_id%22%3A%22197f9b515f2723-01bb97c620ba8a1-26011151-1327104-197f9b515f41c6%22%7D",
        "Hm_lvt_25b04a5e7a64668b9b88e2711fb5f0c4": "1752241086",
        "_uetvid": "46c6e7a05e5c11f0b3636bbf95cbb9c3",
        "GeeTestUser": "11a608721ed648e63ae491e27ae91e2e"
    }
    config = {
        "gt": gt_challenge_obj['gt'],
        "challenge": gt_challenge_obj['challenge'],
        "offline": False,
        "new_captcha": True,
        "product": "float",
        "width": "300px",
        "https": True,
        "api_server": "apiv6.geetest.com",
        "protocol": "https://",
        "type": "fullpage",
        "static_servers": [
            "static.geetest.com/",
            "static.geevisit.com/"
        ],
        "beeline": "/static/js/beeline.1.0.1.js",
        "voice": "/static/js/voice.1.2.6.js",
        "click": "/static/js/click.3.1.2.js",
        "fullpage": "/static/js/fullpage.9.2.0-guwyxh.js",
        "slide": "/static/js/slide.7.9.3.js",
        "geetest": "/static/js/geetest.6.0.9.js",
        "aspect_radio": {
            "slide": 103,
            "click": 128,
            "voice": 128,
            "beeline": 50
        },
        "cc": 8,
        "ww": True,
        "i": "-1!!-1!!-1!!-1!!-1!!-1!!-1!!-1!!-1!!-1!!-1!!-1!!-1!!-1!!-1!!-1!!-1!!-1!!-1!!-1!!-1!!-1!!-1!!-1!!-1!!-1!!-1!!-1!!-1!!-1!!-1!!-1!!-1!!-1!!-1!!-1!!-1!!-1!!-1!!-1!!-1!!-1!!-1!!-1!!-1!!-1!!-1!!-1!!-1!!-1!!-1!!-1!!-1!!-1!!-1!!-1!!-1!!-1!!-1!!-1!!-1!!-1!!-1!!-1!!-1!!-1!!-1!!-1!!-1!!-1!!-1!!-1!!-1!!-1"
    }
    # w = execjs.compile(open('demo.js','r',encoding='utf-8').read()).call('get_w',config)
    w1 = get_w1(json.dumps(config),aes_key)
    logger.warning(w1)
    params = {
        "gt": gt_challenge_obj['gt'],
        "challenge": gt_challenge_obj['challenge'],
        "lang": "zh-cn",
        "pt": "0",
        "client_type": "web",
        "w": w1,
        "callback": f"geetest_{int(time.time() * 1000)}"
    }
    response = requests.get(url, headers=headers, cookies=cookies, params=params)
    logger.debug(response.text)
def ajax(gt_challenge_obj,aes_key):
    url = "https://api.geevisit.com/ajax.php"
    passtime = random.randint(4450,4500)
    rp = get_rp(gt_challenge_obj['gt'] + gt_challenge_obj['challenge'] + str(passtime))
    w2_plaintext_obj = {
        "lang": "zh-cn",
        "type": "fullpage",
        "tt": "M,38PjV)9U(U(bz((,5n-((((M9Rj-1VFOSZEK)*DMbNj-2MENkG0OEpTRXCD-/9-l(04q((8b,5(5b8*NY-,b9@*(f1g:Ob9@A)(I/*(7M3*M*M9(M1*ME)qqM*.,n5(,b855(7)9Y/-b94)(d@)(P9f6I/-PbM1?0)(Y-)4)(94)(@-M3)(0qqn",
        "light": "SPAN_0",
        "s": "c7c3e21112fe4f741921cb3e4ff9f7cb",
        "h": "321f9af1e098233dbd03f250fd2b5e21",
        "hh": "39bd9cad9e425c3a8f51610fd506e3b3",
        "hi": "09eb21b3ae9542a9bc1e8b63b3d9a467",
        "vip_order": -1,
        "ct": -1,
        "ep": {
            "v": "9.2.0-guwyxh",
            "te": False,
            "$_BBn": True,
            "ven": "Google Inc. (Intel)",
            "ren": "ANGLE (Intel, Intel(R) UHD Graphics (0x0000A7A8) Direct3D11 vs_5_0 ps_5_0, D3D11)",
            "fp": [
                "move",
                771,
                129,
                1756377305525,
                "pointermove"
            ],
            "lp": [
                "up",
                661,
                23,
                1756377306333,
                "pointerup"
            ],
            "em": {
                "ph": 0,
                "cp": 0,
                "ek": "11",
                "wd": 1,
                "nt": 0,
                "si": 0,
                "sc": 0
            },
            "tm": {
                "a": 1756377301494,
                "b": 1756377301549,
                "c": 1756377301549,
                "d": 0,
                "e": 0,
                "f": 1756377301496,
                "g": 1756377301496,
                "h": 1756377301496,
                "i": 1756377301496,
                "j": 1756377301496,
                "k": 0,
                "l": 1756377301498,
                "m": 1756377301542,
                "n": 1756377301543,
                "o": 1756377301551,
                "p": 1756377301646,
                "q": 1756377301646,
                "r": 1756377301647,
                "s": 1756377301647,
                "t": 1756377301647,
                "u": 1756377301647
            },
            "dnf": "dnf",
            "by": 0
        },
        "passtime": passtime,
        "rp": rp,
        "captcha_token": "112439067",
        "tsfq": "xovrayel"
    }
    w2 = get_w2(json.dumps(w2_plaintext_obj,separators=(',',':')),aes_key)
    params = {
        "gt": gt_challenge_obj['gt'],
        "challenge": gt_challenge_obj['challenge'],
        "lang": "zh-cn",
        "pt": "0",
        "client_type": "web",
        "w": w2,
        "callback": f"geetest_{int(time.time() * 1000)}"
    }
    response = requests.get(url, headers=headers, params=params)
    logger.debug(response.text)
def get_img_obj(gt_challenge_obj):
    headers = {
        "Accept": "*/*",
        "Accept-Language": "zh-CN,zh;q=0.9",
        "Cache-Control": "no-cache",
        "Connection": "keep-alive",
        "Pragma": "no-cache",
        "Referer": "https://demos.geetest.com/",
        "Sec-Fetch-Dest": "script",
        "Sec-Fetch-Mode": "no-cors",
        "Sec-Fetch-Site": "cross-site",
        "Sec-Fetch-Storage-Access": "active",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/138.0.0.0 Safari/537.36",
        "sec-ch-ua": "\"Not)A;Brand\";v=\"8\", \"Chromium\";v=\"138\", \"Google Chrome\";v=\"138\"",
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": "\"Windows\""
    }
    url = "https://api.geevisit.com/get.php"
    params = {
        "is_next": "true",
        "type": "slide3",
        "gt": gt_challenge_obj['gt'],
        "challenge": gt_challenge_obj["challenge"],
        "lang": "zh-cn",
        "https": "true",
        "protocol": "https://",
        "offline": "false",
        "product": "embed",
        "api_server": "api.geevisit.com",
        "isPC": "true",
        "autoReset": "true",
        "width": "100%",
        "callback": f"geetest_{int(time.time() * 1000)}"
    }
    response = requests.get(url, headers=headers, params=params)
    json_str = response.text[22:-1]
    return json.loads(json_str)
def save_img(bg_url,bg_full_url,slice_url):
    with open('bg.jpg','wb') as f:
        f.write(requests.get(bg_url,headers=headers).content)
        f.close()
    with open('bg_full.jpg','wb') as f1:
        f1.write(requests.get(bg_full_url,headers=headers).content)
        f1.close()
    with open('slice.png','wb') as f2:
        f2.write(requests.get(slice_url,headers=headers).content)
        f2.close()
    logger.success('乱序图片保存完毕！！！')
def restore_img():
    img_list = ['bg.jpg','bg_full.jpg']
    for index, img in enumerate(img_list):
        im = Image.open(img)
        new_img = Image.new("RGB", (260,160))
        r = 160
        Ut = [39, 38, 48, 49, 41, 40, 46, 47, 35, 34, 50, 51, 33, 32, 28, 29, 27, 26, 36, 37, 31, 30, 44, 45, 43, 42,12, 13,
              23, 22, 14, 15, 21, 20, 8, 9, 25, 24, 6, 7, 3, 2, 0, 1, 11, 10, 4, 5, 19, 18, 16, 17]
        for _ in range(len(Ut)):
            a = r / 2
            c = Ut[_] % 26 * 12 + 1
            u = 80 if Ut[_] > 25 else 0
            l = im.crop(box=(c, u, c + 10, u + 80))
            new_img.paste(l, box=(_ % 26 * 10,80 if _ > 25 else 0))
            if index == 0:
                new_img.save("restore_bg.jpg")
            else:
                new_img.save("restore_bg_full.jpg")

'''
获取识别距离,生成轨迹
'''
def get_distance(bg_img, slice_img):
    det = ddddocr.DdddOcr(det=True, ocr=True)
    try:
        with open(slice_img, 'rb') as f:
            target_bytes = f.read()
        with open(bg_img, 'rb') as f:
            background_bytes = f.read()
    except:
        logger.error('图片打开失败')
    res = det.slide_match(target_bytes, background_bytes)
    logger.warning(f'ddddocr识别结果为：{res}')
    return int(res['target'][0])

# https://blog.csdn.net/qq_29091459/article/details/144331149  轨迹参考这位大佬的
def __ease_out_expo(sep):
    '''
        轨迹相关操作
    '''
    if sep == 1:
        return 1
    else:
        return 1 - pow(2, -10 * sep)
def get_slide_track(distance):
    """
    根据滑动距离生成滑动轨迹
    :param distance: 需要滑动的距离
    :return: 滑动轨迹<type 'list'>: [[x,y,t], ...]
        x: 已滑动的横向距离
        y: 已滑动的纵向距离, 除起点外, 均为0
        t: 滑动过程消耗的时间, 单位: 毫秒
    """

    if not isinstance(distance, int) or distance < 0:
        raise ValueError(f"distance类型必须是大于等于0的整数: distance: {distance}, type: {type(distance)}")
    # 初始化轨迹列表
    slide_track = [
        [random.randint(-50, -10), random.randint(-50, -10), 0],
        [0, 0, 0],
    ]
    # 共记录count次滑块位置信息
    count = 10 + int(distance / 2)
    # 初始化滑动时间
    t = random.randint(50, 100)
    # 记录上一次滑动的距离
    _x = 0
    _y = 0
    for i in range(count):
        # 已滑动的横向距离
        x = round(__ease_out_expo(i / count) * distance)
        # y = round(__ease_out_expo(i / count) * 14)
        # 滑动过程消耗的时间
        t += random.randint(10, 50)
        if x == _x:
            continue
        slide_track.append([x, _y, t])
        _x = x
    slide_track.append(slide_track[-1])
    return slide_track, slide_track[-1][-1]

'''
最终验证
'''
def verify(image_object,distance,aes_key):
    ###待完成
    track_list,passtime = get_slide_track(distance)
    logger.debug(f'轨迹数组：{track_list}')
    rp = get_rp(image_object['gt'] + image_object['challenge'][:32] + str(passtime))
    userresponse = execjs.compile(open('final.js','r',encoding='utf-8').read()).call('get_user_response',distance,image_object['challenge'])
    aa = execjs.compile(open('final.js','r',encoding='utf-8').read()).call('get_aa',track_list,image_object['c'],image_object['s'])
    _timestamp = int(time.time() * 1000)
    w3_mingwen_obj = {
        "lang": "zh-cn",
        "userresponse": userresponse,
        "passtime": passtime,
        "imgload": 109,
        "aa": aa,
        "ep": {
            "v": "7.9.3",
            "$_BIT": False,
            "me": True,
            "tm": {
                "a": _timestamp,#_timestamp
                "b": _timestamp + random.randint(60,63),#_timestamp + random.randint(60,63)
                "c": _timestamp + random.randint(60,63),#_timestamp + random.randint(60,63)
                "d": 0,
                "e": 0,
                "f": _timestamp + random.randint(2,4),#_timestamp + random.randint(2,4)
                "g": _timestamp + random.randint(2,4),#_timestamp + random.randint(2,4)
                "h": _timestamp + random.randint(2,4),#_timestamp + random.randint(2,4)
                "i": _timestamp + random.randint(2,4),#_timestamp + random.randint(2,4)
                "j": _timestamp + random.randint(2,4),#_timestamp + random.randint(2,4)
                "k": 0,
                "l": _timestamp + random.randint(5,7),#_timestamp + random.randint(5,7)
                "m": _timestamp + random.randint(51,55),#_timestamp + random.randint(51,55)
                "n": _timestamp + random.randint(53,55),#_timestamp + random.randint(53,55)
                "o": _timestamp + random.randint(62,65),#_timestamp + random.randint(62,65)
                "p": _timestamp + random.randint(202,205),#_timestamp + random.randint(202,205)
                "q": _timestamp + random.randint(202,205),#_timestamp + random.randint(202,205)
                "r": _timestamp + random.randint(204,206),#_timestamp + random.randint(204,206)
                "s": _timestamp + random.randint(204,206),#_timestamp + random.randint(204,206)
                "t": _timestamp + random.randint(204,206),#_timestamp + random.randint(204,206)
                "u": _timestamp + random.randint(204,206)#_timestamp + random.randint(204,206)
            },
            "td": -1
        },
        "h9s9": "1816378497",
        "rp": rp
    }
    w3 = get_w3(json.dumps(w3_mingwen_obj,separators=(',',':')),aes_key)
    logger.debug(w3)
    headers = {
        "Accept": "*/*",
        "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6",
        "Cache-Control": "no-cache",
        "Connection": "keep-alive",
        "Pragma": "no-cache",
        "Referer": "https://demos.geetest.com/",
        "Sec-Fetch-Dest": "script",
        "Sec-Fetch-Mode": "no-cors",
        "Sec-Fetch-Site": "cross-site",
        "Sec-Fetch-Storage-Access": "active",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/139.0.0.0 Safari/537.36 Edg/139.0.0.0",
        "sec-ch-ua": "\"Not;A=Brand\";v=\"99\", \"Microsoft Edge\";v=\"139\", \"Chromium\";v=\"139\"",
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": "\"Windows\""
    }
    url = "https://api.geevisit.com/ajax.php"
    params = {
        "gt": image_object['gt'],
        "challenge": image_object['challenge'],
        "lang": "zh-cn",
        "%24_BCm": "0",
        "client_type": "web",
        "w": w3,
        "callback": f"geetest_{int(time.time() * 1000)}"
    }
    response = requests.get(url, headers=headers, params=params)
    logger.debug(response.text)
    Json_data = json.loads(response.text[22:-1])
    if Json_data['message'] == 'success':
        logger.success('成功了呀，嘿嘿嘿！！！')
    else:
        logger.error('没有通过，呜呜呜')

if __name__ == '__main__':
    baseurl = 'https://static.geetest.com/'
    gt_challenge_obj = get_gt_challenge()
    logger.debug(gt_challenge_obj)
    gettype(gt_challenge_obj)
    aes_key = get_aes_key()
    get(gt_challenge_obj,aes_key)
    ajax(gt_challenge_obj,aes_key)
    img_obj = get_img_obj(gt_challenge_obj)
    logger.info(img_obj)
    save_img(baseurl + img_obj['bg'],baseurl + img_obj['fullbg'],baseurl + img_obj['slice'])
    restore_img()
    distance = get_distance('restore_bg.jpg','slice.png')
    verify(img_obj,distance,aes_key)

