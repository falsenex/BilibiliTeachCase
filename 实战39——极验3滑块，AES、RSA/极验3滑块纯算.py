#####解混淆参考
# https://www.52pojie.cn/thread-2055730-1-1.html
#####识别距离参考
# https://segmentfault.com/a/1190000045577230
######轨迹参考
# https://blog.csdn.net/qq_29091459/article/details/144331149
import base64
import binascii
import hashlib
import json
import os
import random
import cv2
import ddddocr
from Crypto.Cipher import PKCS1_OAEP, PKCS1_v1_5
from Crypto.PublicKey import RSA
from PIL import Image
import requests
import time
import secrets
from loguru import logger
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad

class Geetest3:
    """极验3验证码破解类"""
    
    def __init__(self):
        """初始化验证码破解器"""
        self.headers = {
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
        
        self.cookies = {
            "sensorsdata2015jssdkcross": "%7B%22distinct_id%22%3A%22197f9b515f2723-01bb97c620ba8a1-26011151-1327104-197f9b515f41c6%22%2C%22first_id%22%3A%22%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E7%9B%B4%E6%8E%A5%E6%B5%81%E9%87%8F%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC_%E7%9B%B4%E6%8E%A5%E6%89%93%E5%BC%80%22%2C%22%24latest_referrer%22%3A%22%22%2C%22%24latest_landing_page%22%3A%22https%3A%2F%2Fwww.geetest.com%2F%22%7D%2C%22%24device_id%22%3A%22197f9b515f2723-01bb97c620ba8a1-26011151-1327104-197f9b515f41c6%22%7D",
            "Hm_lvt_25b04a5e7a64668b9b88e2711fb5f0c4": "1752241086",
            "_uetvid": "46c6e7a05e5c11f0b3636bbf95cbb9c3"
        }
        
        self.baseurl = 'https://static.geetest.com/'
        self.gt_challenge_obj = None
        self.aes_key = None
        self.img_obj = None
        self.distance = None
        
        # 图片还原映射表
        self.restore_map = [39, 38, 48, 49, 41, 40, 46, 47, 35, 34, 50, 51, 33, 32, 28, 29, 27, 26, 36, 37, 31, 30, 44, 45, 43, 42, 12, 13,
                           23, 22, 14, 15, 21, 20, 8, 9, 25, 24, 6, 7, 3, 2, 0, 1, 11, 10, 4, 5, 19, 18, 16, 17]

    # ==================== JavaScript函数的Python实现 ====================
    
    def get_user_response(self, t, e):
        """JavaScript get_user_response函数的Python实现"""
        n = e[-2:]  # e["slice"](-2)
        r = []
        for i in range(len(n)):
            o = ord(n[i])
            r.append(o - 87 if o > 57 else o - 48)
        
        n_val = 36 * r[0] + r[1]
        a = round(t) + n_val
        _ = [[], [], [], [], []]
        c = {}
        u = 0
        
        e_slice = e[:-2]  # e["slice"](0, -2)
        for i in range(len(e_slice)):
            s = e_slice[i]
            if s not in c:
                c[s] = 1
                _[u].append(s)
                u = u + 1
                if u == 5:
                    u = 0
        
        f = a
        d = 4
        p = ""
        g = [1, 2, 5, 10, 50]
        
        while f > 0:
            if f - g[d] >= 0:
                h = int(random.random() * len(_[d]))
                p += _[d][h]
                f -= g[d]
            else:
                _.pop(d)
                g.pop(d)
                d -= 1
        
        return p

    def n_encode(self, t):
        """JavaScript n函数的Python实现"""
        e = "()*,-./0123456789:?@ABCDEFGHIJKLMNOPQRSTUVWXYZ_abcdefghijklmnopqr"
        n_len = len(e)
        r = ""
        i = abs(t)
        o = int(i / n_len)
        
        if o >= n_len:
            o = n_len - 1
        if o:
            r = e[o]
        
        s = ""
        if t < 0:
            s += "!"
        if r:
            s += "$"
        
        return s + r + e[i % n_len]

    def generate_list(self, t):
        """JavaScript generate_list函数的Python实现"""
        i = []
        o = 0
        
        for s in range(len(t) - 1):
            e = round(t[s + 1][0] - t[s][0])
            n = round(t[s + 1][1] - t[s][1])
            r = round(t[s + 1][2] - t[s][2])
            
            if e == 0 and n == 0 and r == 0:
                continue
            
            if e == 0 and n == 0:
                o += r
            else:
                i.append([e, n, r + o])
                o = 0
        
        if o != 0:
            i.append([e, n, o])
        
        return i

    def bbl_encrypt(self, t, e, n):
        """JavaScript $_BBEl函数的Python实现"""
        if not e or not n:
            return t
        
        i = 0
        o = t
        s = e[0]
        a = e[2]
        _ = e[4]
        
        while i < len(n):
            r = n[i:i+2]
            if len(r) < 2:
                break
            i += 2
            c = int(r, 16)
            u = chr(c)
            l = (s * c * c + a * c + _) % len(t)
            o = o[:l] + u + o[l:]
        
        return o

    def get_aa(self, track_list, c, s):
        """JavaScript get_aa函数的Python实现"""
        new_list = self.generate_list(track_list)
        r = []
        i = []
        o = []
        
        # 预定义的方向映射
        direction_map = [[1, 0], [2, 0], [1, -1], [1, 1], [0, 1], [0, -1], [3, 0], [2, -1], [2, 1]]
        direction_chars = "stuvwxyz~"
        
        for t in new_list:
            # 查找方向匹配
            e = None
            for n in range(len(direction_map)):
                if t[0] == direction_map[n][0] and t[1] == direction_map[n][1]:
                    e = direction_chars[n]
                    break
            
            if e:
                i.append(e)
            else:
                r.append(self.n_encode(t[0]))
                i.append(self.n_encode(t[1]))
            
            o.append(self.n_encode(t[2]))
        
        result = "".join(r) + "!!" + "".join(i) + "!!" + "".join(o)
        return self.bbl_encrypt(result, c, s)

    # ==================== 加密相关方法 ====================
    
    def load_public_key(self, pem_key=None, modulus=None, exponent=None):
        """加载RSA公钥"""
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

    def get_cipher(self, key_obj, padding_mode: int):
        """根据指定的填充模式获取加密器对象"""
        scheme = {
            1: PKCS1_OAEP.new,  # OAEP填充（推荐）
            2: PKCS1_v1_5.new   # 传统的PKCS#1 v1.5填充
        }
        if padding_mode not in scheme:
            raise ValueError("padding_mode 只支持 1（OAEP）或 2（v1_5）")
        return scheme[padding_mode](key_obj)

    def encrypt_bytes(self, plaintext: str, *, pem_key=None, modulus="00C1E3934D1614465B33053E7F48EE4EC87B14B95EF88947713D25EECBFF7E74C7977D02DC1D9451F79DD5D1C10C29ACB6A9B4D6FB7D0A0279B6719E1772565F09AF627715919221AEF91899CAE08C0D686D748B20A3603BE2318CA6BC2B59706592A9219D0BF05C9F65023A21D2330807252AE0066D59CEEFA5F2748EA80BAB81", exponent="10001", padding_mode=2) -> bytes:
        """加密字节数据"""
        key_obj = self.load_public_key(pem_key=pem_key, modulus=modulus, exponent=exponent)
        cipher = self.get_cipher(key_obj, padding_mode)
        encrypted_data = cipher.encrypt(plaintext.encode())
        return encrypted_data

    def rsaencrypt_to_hex(self, plaintext: str, **kwargs) -> str:
        """将加密结果转换为16进制字符串"""
        return binascii.hexlify(self.encrypt_bytes(plaintext, **kwargs)).decode()

    def get_w_encode(self, e):
        """JavaScript get_w函数的Python实现"""
        def _BIGCu(e, t):
            return (e >> t) & 1
        
        def _BIFIK(e):
            t = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789()"
            return "." if e < 0 or e >= len(t) else t[e]
        
        def t_func(e, t):
            n = 0
            for r in range(23, -1, -1):
                if _BIGCu(t, r) == 1:
                    n = (n << 1) + _BIGCu(e, r)
            return n
        
        n = ''
        r = ''
        s = len(e)
        a = 0
        
        while a < s:
            if a + 2 < s:
                _ = (e[a] << 16) + (e[a + 1] << 8) + e[a + 2]
                n += _BIFIK(t_func(_, 7274496)) + _BIFIK(t_func(_, 9483264)) + _BIFIK(t_func(_, 19220)) + _BIFIK(t_func(_, 235))
            else:
                c = s % 3
                if c == 2:
                    _ = (e[a] << 16) + (e[a + 1] << 8)
                    n += _BIFIK(t_func(_, 7274496)) + _BIFIK(t_func(_, 9483264)) + _BIFIK(t_func(_, 19220))
                    r = '.'
                elif c == 1:
                    _ = e[a] << 16
                    n += _BIFIK(t_func(_, 7274496)) + _BIFIK(t_func(_, 9483264))
                    r = '..'
            a += 3
        
        return n + r

    def get_aes_key(self):
        """生成AES密钥"""
        part = hex(int(65536 * (1 + secrets.SystemRandom().random())))[2:-1]
        part1 = hex(int(65536 * (1 + secrets.SystemRandom().random())))[2:-1]
        part2 = hex(int(65536 * (1 + secrets.SystemRandom().random())))[2:-1]
        part3 = hex(int(65536 * (1 + secrets.SystemRandom().random())))[2:-1]
        return part + part1 + part2 + part3

    def encrypt_aes_cbc(self, plaintext: str, key_str: str, iv_str: str = "0000000000000000") -> list:
        """使用 AES-CBC 模式对字符串加密"""
        key = key_str.encode('utf-8')
        iv = iv_str.encode('utf-8')
        # 初始化加密器
        cipher = AES.new(key, AES.MODE_CBC, iv)
        # 对明文进行 PKCS7 填充
        padded_data = pad(plaintext.encode('utf-8'), AES.block_size)
        # 加密数据
        encrypted_data = cipher.encrypt(padded_data)
        # 将加密后的数据转换为字节列表
        byte_list = list(encrypted_data)
        return byte_list

    def get_w1(self, mingwen_str, aes_key):
        """生成w1参数"""
        aes_encrypt_list = self.encrypt_aes_cbc(mingwen_str, aes_key)
        aes_part = self.get_w_encode(aes_encrypt_list)
        rsa_part = self.rsaencrypt_to_hex(aes_key)
        return aes_part + rsa_part

    def get_w2(self, mingwen_str, aes_key):
        """生成w2参数"""
        aes_encrypt_list = self.encrypt_aes_cbc(mingwen_str, aes_key)
        return self.get_w_encode(aes_encrypt_list)

    def get_w3(self, mingwen_str, aes_key):
        """生成w3参数"""
        aes_encrypt_list = self.encrypt_aes_cbc(mingwen_str, aes_key)
        aes_part = self.get_w_encode(aes_encrypt_list)
        rsa_part = self.rsaencrypt_to_hex(aes_key)
        return aes_part + rsa_part

    def get_rp(self, plaintext: str):
        """生成rp参数"""
        return hashlib.md5(plaintext.encode('utf-8')).hexdigest()

    # ==================== 网络请求方法 ====================
    
    def get_gt_challenge(self):
        """获取gt和challenge参数"""
        url = "https://demos.geetest.com/gt/register-slide"
        params = {
            "t": str(int(time.time() * 1000))
        }
        response = requests.get(url, headers=self.headers, cookies=self.cookies, params=params)
        return response.json()

    def gettype(self, gt_challenge_obj):
        """调用gettype接口"""
        url = "https://apiv6.geetest.com/gettype.php"
        params = {
            "gt": gt_challenge_obj['gt'],
            "callback": f"geetest_{int(time.time() * 1000)}"
        }
        response = requests.get(url, headers=self.headers, cookies=self.cookies, params=params)
        logger.debug(response.text)

    def get_config_request(self, gt_challenge_obj, aes_key):
        """发送get配置请求"""
        url = "https://apiv6.geetest.com/get.php"
        cookies_local = {
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
        w1 = self.get_w1(json.dumps(config), aes_key)
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
        response = requests.get(url, headers=self.headers, cookies=cookies_local, params=params)
        logger.debug(response.text)

    def ajax_request(self, gt_challenge_obj, aes_key):
        """发送ajax请求"""
        url = "https://api.geevisit.com/ajax.php"
        passtime = random.randint(4450, 4500)
        rp = self.get_rp(gt_challenge_obj['gt'] + gt_challenge_obj['challenge'] + str(passtime))
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
        w2 = self.get_w2(json.dumps(w2_plaintext_obj, separators=(',', ':')), aes_key)
        params = {
            "gt": gt_challenge_obj['gt'],
            "challenge": gt_challenge_obj['challenge'],
            "lang": "zh-cn",
            "pt": "0",
            "client_type": "web",
            "w": w2,
            "callback": f"geetest_{int(time.time() * 1000)}"
        }
        response = requests.get(url, headers=self.headers, params=params)
        logger.debug(response.text)

    def get_img_obj(self, gt_challenge_obj):
        """获取验证码图片信息"""
        headers_local = {
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
        response = requests.get(url, headers=headers_local, params=params)
        json_str = response.text[22:-1]
        return json.loads(json_str)

    # ==================== 图像处理方法 ====================
    
    def save_img(self, bg_url, bg_full_url, slice_url):
        """保存验证码图片"""
        with open('bg.jpg', 'wb') as f:
            f.write(requests.get(bg_url, headers=self.headers).content)
            f.close()
        with open('bg_full.jpg', 'wb') as f1:
            f1.write(requests.get(bg_full_url, headers=self.headers).content)
            f1.close()
        with open('slice.png', 'wb') as f2:
            f2.write(requests.get(slice_url, headers=self.headers).content)
            f2.close()
        logger.success('乱序图片保存完毕！！！')

    def restore_img(self):
        """还原乱序图片"""
        img_list = ['bg.jpg', 'bg_full.jpg']
        for index, img in enumerate(img_list):
            im = Image.open(img)
            new_img = Image.new("RGB", (260, 160))
            r = 160
            for _ in range(len(self.restore_map)):
                a = r / 2
                c = self.restore_map[_] % 26 * 12 + 1
                u = 80 if self.restore_map[_] > 25 else 0
                l = im.crop(box=(c, u, c + 10, u + 80))
                new_img.paste(l, box=(_ % 26 * 10, 80 if _ > 25 else 0))
                if index == 0:
                    new_img.save("restore_bg.jpg")
                else:
                    new_img.save("restore_bg_full.jpg")
    ###ddddocr识别
    def get_distance(self, bg_img, slice_img):
        """识别滑动距离"""
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
    #####某大佬开源的opencv 识别
    def identify_gap(self,bg, tp, out):
        '''
        bg: 背景图片
        tp: 缺口图片
        out:输出图片
        '''
        # 读取背景图片和缺口图片
        bg_img = cv2.imread(bg)  # 背景图片
        tp_img = cv2.imread(tp)  # 缺口图片

        # 识别图片边缘
        bg_edge = cv2.Canny(bg_img, 100, 200)
        tp_edge = cv2.Canny(tp_img, 100, 200)

        # 转换图片格式
        bg_pic = cv2.cvtColor(bg_edge, cv2.COLOR_GRAY2RGB)
        tp_pic = cv2.cvtColor(tp_edge, cv2.COLOR_GRAY2RGB)

        # 缺口匹配
        res = cv2.matchTemplate(bg_pic, tp_pic, cv2.TM_CCOEFF_NORMED)
        min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)  # 寻找最优匹配

        # 绘制方框
        th, tw = tp_pic.shape[:2]
        tl = max_loc  # 左上角点的坐标
        br = (tl[0] + tw, tl[1] + th)  # 右下角点的坐标
        cv2.rectangle(bg_img, tl, br, (0, 0, 255), 2)  # 绘制矩形
        cv2.imwrite(out, bg_img)  # 保存在本地

        # 返回缺口的X坐标
        return tl[0]

    def get_slide_distance(self,bg_path, slide_path):
        '''
        识别滑块具体位置，返回位置比例: 位置/图片宽度
        使用的时候再乘以实际图片宽度即可
        '''
        bg_img = cv2.imread(bg_path)
        sd_img = cv2.imread(slide_path)
        bg_gray = cv2.cvtColor(bg_img, cv2.COLOR_BGR2GRAY)
        bg_gray = cv2.GaussianBlur(bg_gray, (5, 5), 0)
        bg_edge = cv2.Canny(bg_gray, 30, 100)
        rgb_bg_gray = cv2.cvtColor(bg_edge, cv2.COLOR_GRAY2RGB)

        sd_gray = cv2.cvtColor(sd_img, cv2.COLOR_BGR2GRAY)
        sd_gray = cv2.GaussianBlur(sd_gray, (5, 5), 0)
        sd_edge = cv2.Canny(sd_gray, 30, 100)
        rgb_sd_gray = cv2.cvtColor(sd_edge, cv2.COLOR_GRAY2RGB)
        result = cv2.matchTemplate(rgb_bg_gray, rgb_sd_gray, cv2.TM_CCORR_NORMED)
        _, _, _, max_loc = cv2.minMaxLoc(result)
        cv2.rectangle(bg_img, (max_loc[0], max_loc[1]), (max_loc[0] + 110, max_loc[1] + 110),
                      (0, 255, 0), 2)
        result_path = os.path.join(os.path.dirname(bg_path), "./PictureTemp/result.png")
        cv2.imwrite(result_path, bg_img)
        return max_loc[0]

    # ==================== 轨迹生成方法 ====================
    
    def __ease_out_expo(self, sep):
        """轨迹缓动函数"""
        if sep == 1:
            return 1
        else:
            return 1 - pow(2, -10 * sep)

    def get_slide_track(self, distance):
        """根据滑动距离生成滑动轨迹"""
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
            x = round(self.__ease_out_expo(i / count) * distance)
            # 滑动过程消耗的时间
            t += random.randint(10, 50)
            if x == _x:
                continue
            slide_track.append([x, _y, t])
            _x = x
        slide_track.append(slide_track[-1])
        return slide_track, slide_track[-1][-1]

    # ==================== 验证方法 ====================
    
    def verify(self, image_object, distance, aes_key):
        """最终验证"""
        track_list, passtime = self.get_slide_track(distance)
        logger.debug(f'轨迹数组：{track_list}')
        rp = self.get_rp(image_object['gt'] + image_object['challenge'][:32] + str(passtime))
        
        # 使用Python实现替代JavaScript调用
        userresponse = self.get_user_response(distance, image_object['challenge'])
        aa = self.get_aa(track_list, image_object['c'], image_object['s'])
        
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
                    "a": _timestamp,
                    "b": _timestamp + random.randint(60, 63),
                    "c": _timestamp + random.randint(60, 63),
                    "d": 0,
                    "e": 0,
                    "f": _timestamp + random.randint(2, 4),
                    "g": _timestamp + random.randint(2, 4),
                    "h": _timestamp + random.randint(2, 4),
                    "i": _timestamp + random.randint(2, 4),
                    "j": _timestamp + random.randint(2, 4),
                    "k": 0,
                    "l": _timestamp + random.randint(5, 7),
                    "m": _timestamp + random.randint(51, 55),
                    "n": _timestamp + random.randint(53, 55),
                    "o": _timestamp + random.randint(62, 65),
                    "p": _timestamp + random.randint(202, 205),
                    "q": _timestamp + random.randint(202, 205),
                    "r": _timestamp + random.randint(204, 206),
                    "s": _timestamp + random.randint(204, 206),
                    "t": _timestamp + random.randint(204, 206),
                    "u": _timestamp + random.randint(204, 206)
                },
                "td": -1
            },
            "h9s9": "1816378497",
            "rp": rp
        }
        w3 = self.get_w3(json.dumps(w3_mingwen_obj, separators=(',', ':')), aes_key)
        logger.debug(w3)
        
        headers_verify = {
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
        response = requests.get(url, headers=headers_verify, params=params)
        logger.debug(response.text)
        Json_data = json.loads(response.text[22:-1])
        if Json_data['message'] == 'success':
            logger.success('成功了呀，嘿嘿嘿！！！')
            return True
        else:
            logger.error('没有通过，呜呜呜')
            return False

    # ==================== 主要执行流程 ====================
    
    def run(self):
        """执行完整的验证码破解流程"""
        try:
            # 1. 获取gt和challenge
            self.gt_challenge_obj = self.get_gt_challenge()
            logger.debug(f"获取到gt_challenge_obj: {self.gt_challenge_obj}")
            
            # 2. 调用gettype接口
            self.gettype(self.gt_challenge_obj)
            
            # 3. 生成AES密钥
            self.aes_key = self.get_aes_key()
            logger.debug(f"生成的AES密钥: {self.aes_key}")
            
            # 4. 发送配置请求
            self.get_config_request(self.gt_challenge_obj, self.aes_key)
            
            # 5. 发送ajax请求
            self.ajax_request(self.gt_challenge_obj, self.aes_key)
            
            # 6. 获取验证码图片信息
            self.img_obj = self.get_img_obj(self.gt_challenge_obj)
            logger.info(f"获取到图片对象: {self.img_obj}")
            
            # 7. 保存并还原图片
            self.save_img(self.baseurl + self.img_obj['bg'], 
                         self.baseurl + self.img_obj['fullbg'], 
                         self.baseurl + self.img_obj['slice'])
            self.restore_img()
            
            # 8. 识别滑动距离
            ######ddddocr识别
            # self.distance = self.get_distance('restore_bg.jpg', 'slice.png')
            ######某大佬开源的opencv识别
            self.distance = self.get_slide_distance('restore_bg.jpg', 'slice.png')
            logger.info(f"识别的滑动距离: {self.distance}")
            
            # 9. 执行验证
            result = self.verify(self.img_obj, self.distance, self.aes_key)
            return result
            
        except Exception as e:
            logger.error(f"验证码破解过程中出现错误: {str(e)}")
            return False
def main():
    """主函数 - 演示如何使用Geetest3类"""
    cracker = Geetest3()
    result = cracker.run()
    if result:
        logger.success("验证码破解成功！")
    else:
        logger.error("验证码破解失败！")


if __name__ == '__main__':
    main()
