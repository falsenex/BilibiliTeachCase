#coding=utf-8
import json
import math
import random
import time
import uuid
from datetime import datetime
import cv2
import execjs
import numpy as np
# import requests
from curl_cffi import requests
from loguru import logger
from recover import recover_image_from_file
from 距离识别 import *

# https://segmentfault.com/a/1190000045577230

class SmartHotelLogin:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.headers = {
            # "csrf-token": "nZYhLcnt-zOiBmbhHaLpQqaiyPkLqkzPvh1A",
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/139.0.0.0 Safari/537.36 Edg/139.0.0.0',
        }
        self.cookies = {}
        self.user_id = str(uuid.uuid4())

    def getLoginToken(self):
        url = 'https://hotel.ocyuan.com/login'
        response = requests.get(url, headers=self.headers, cookies=self.cookies)
        self.cookies['fast-sid'] = response.cookies['fast-sid']
        self.headers['csrf-token'] = response.cookies['csrf-token']
        logger.info('获取csrf-token成功' + self.headers['csrf-token'])
        logger.info('获取fast-sid成功' + self.cookies['fast-sid'])

    def fetchGeeVerify(self):
        url = 'https://hotel.ocyuan.com/api/v2/geeVerify'
        json_data = {
            'clientType': 'web_view',
            'lang': 'zh',
            'user_id': self.user_id,
        }
        response = requests.post(url, cookies=self.cookies, headers=self.headers, json=json_data)
        logger.info('获取challenge成功' + response.json()['result']['challenge'])
        self.cookies.update(dict(response.cookies.items()))
        return response.json().get('result')

    def fetchGetQuestion(self, challenge,verifyId):
        url = 'https://captcha.tuyacn.com/verify/v1/getQuestion'
        json_data = {
            'type': 1,
            'verifyId': verifyId,
            'challenge': challenge,
            'callback': f'verify_{int(time.time())}',
        }
        response = requests.post(url, cookies=self.cookies, headers=self.headers, json=json_data)
        return response.json()

    def getBgImage(self, bgUrl, recoverArray):
        response = requests.get(bgUrl, headers=self.headers, cookies=self.cookies)
        with open('bg.webp', 'wb') as f:
            f.write(response.content)
        recover_image_from_file("bg.webp", recoverArray, "recoveredBgImage.png")
        logger.info('recoveredBgImage.png 下载完成')

    def getSliceImage(self, sliceUrl):
        response = requests.get(sliceUrl, headers=self.headers, cookies=self.cookies)
        with open('slice.webp', 'wb') as f:
            f.write(response.content)
        logger.info('slice.webp 下载完成')

    def generate_slide_track(self,end_x, end_y, start_x=0, start_y=None):
        """
        生成整数化的滑块验证码轨迹

        参数:
        end_x (int): 目标点的X坐标
        end_y (int): 目标点的Y坐标
        start_x (int): 起始点的X坐标，默认为0
        start_y (int): 起始点的Y坐标

        返回:
        list: 轨迹数组，每个元素为[x_offset, y_absolute, time_elapsed]三元组（均为整数）
        """
        # 确保起始和结束点符合实际轨迹特征
        if start_y is None:
            y_diff = random.randint(5, 10)
            start_y = end_y - y_diff if end_y > y_diff else random.randint(200, 220)
            start_y = int(start_y)

        # 总点数和时间
        num_points = random.randint(38, 45)
        total_time = random.uniform(300, 350)

        # 轨迹数组
        track = []
        current_x = float(start_x)
        current_y = float(start_y)
        time_elapsed = 0.0

        # 添加起始点（强制取整）
        track.append([int(current_x), int(current_y), int(time_elapsed)])

        # 关键点位置
        critical_point = int(end_x * 0.75)
        slowdown_start = 100

        for i in range(1, num_points):
            # 整数时间间隔(同实际轨迹)
            if i < 10:
                interval = random.randint(6, 10)
            elif i > num_points - 10:
                interval = random.randint(12, 20)
            else:
                interval = random.randint(8, 16)

            time_elapsed += interval

            # X移动模式
            remaining_x = float(end_x - int(current_x))

            # 特殊减速区间处理
            if abs(current_x - slowdown_start) < 5:
                if current_x < slowdown_start:
                    step_x = min(1, remaining_x)
                else:
                    step_x = random.uniform(0.5, 2.5)
            elif current_x < critical_point:
                base_step = remaining_x / (num_points - i) * 1.2
                step_x = random.uniform(base_step * 0.8, base_step * 1.5)
            else:
                base_step = remaining_x / (num_points - i) * 0.5
                step_x = random.uniform(base_step * 0.7, base_step * 1.2)

            step_x = min(step_x, remaining_x)
            current_x += step_x

            # Y移动模式(强制整数变化)
            if random.random() > 0.3 and abs(current_y - end_y) > 1:
                y_adjust = (end_y - current_y) * 0.05 + random.uniform(-0.3, 0.3)
                current_y += y_adjust

            # 添加微小抖动，但保持整数
            current_y += random.uniform(-0.5, 0.5)
            current_y = max(start_y - 1, min(end_y + 1, current_y))

            # 取整处理核心点：所有值转为整数
            int_x = int(round(current_x))
            int_y = int(round(current_y))
            int_time = int(round(time_elapsed))

            # 添加到轨迹（避免重复点）
            last_point = track[-1] if track else None
            if not last_point or (last_point[0] != int_x or last_point[1] != int_y or last_point[2] != int_time):
                track.append([int_x, int_y, int_time])

            # 结束条件：到达终点或超出点数限制
            if current_x >= end_x:
                break

        # 确保最后一点正好是终点
        if track:
            track[-1][0] = end_x
            track[-1][1] = end_y
            track[-1][2] = int(time_elapsed)  # 保持最后时间一致

        return track

    def verify(self,challenge,verifyId,para_obj):
        headers = {
            "accept": "application/json, text/plain, */*",
            "accept-language": "zh-CN,zh;q=0.9",
            "cache-control": "no-cache",
            "content-type": "application/json",
            "origin": "https://hotel.ocyuan.com",
            "pragma": "no-cache",
            "priority": "u=1, i",
            "referer": "https://hotel.ocyuan.com/",
            "sec-ch-ua": "\"Not)A;Brand\";v=\"8\", \"Chromium\";v=\"138\", \"Google Chrome\";v=\"138\"",
            "sec-ch-ua-mobile": "?0",
            "sec-ch-ua-platform": "\"Windows\"",
            "sec-fetch-dest": "empty",
            "sec-fetch-mode": "cors",
            "sec-fetch-site": "cross-site",
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/138.0.0.0 Safari/537.36"
        }
        url = "https://captcha.tuyacn.com/verify/v1/collectData"
        data = {
            "type": 1,
            "challenge": challenge,
            "verifyId": verifyId,
            "collectData": para_obj['collectData'],
            "key": para_obj['key'],
            "callback": para_obj['callback']
        }
        data = json.dumps(data, separators=(',', ':'))
        response = requests.post(url, headers=headers, data=data)
        logger.success(response.json())
        return response.json()
    def secret_key(self):
        url = "https://hotel.ocyuan.com/v2/api/hotel/secret-key"
        response = requests.post(url, headers=self.headers, cookies=self.cookies)
        logger.info(response.json())
        return response.json()['result']
    def login(self,username,password,secret_key_id,secure_key):
        url = "https://hotel.ocyuan.com/v3/api/hotel/login"
        json_data = {
            'country_code': '86',
            'username': username,
            'password': password,
            'secret_key_id': secret_key_id,
            'secure_key': json.dumps(secure_key,separators=(',', ':')),
            'current_domain': 'hotel.ocyuan.com',
        }
        response = requests.post(url, headers=self.headers, cookies=self.cookies, json=json_data)
        logger.success(response.json())
        pass
    def run(self):
        self.getLoginToken()
        obj = self.fetchGeeVerify()
        challenge = obj["challenge"]
        verifyId = obj["verifyId"]
        verifyInfo = self.fetchGetQuestion(challenge,verifyId)['result']
        logger.critical(verifyInfo)
        recoverArray = json.loads(verifyInfo['shuffle'])
        logger.info('获取verifyInfo成功' + str(verifyInfo))
        bgUrl = 'https://images.tuyacn.com/' + verifyInfo['bgUrl']
        sliceUrl = 'https://images.tuyacn.com/' + verifyInfo['sliceUrl']
        self.getBgImage(bgUrl, recoverArray)
        self.getSliceImage(sliceUrl)
        distance = get_slide_distance('./recoveredBgImage.png', './slice.webp')
        track_arr = self.generate_slide_track(distance,random.randint(222,226),0,220)
        logger.debug(track_arr)
        jiami_track = execjs.compile(open('reverse.js', 'r',encoding='utf-8').read()).call('handleTrack',track_arr)
        logger.info(f"加密轨迹：{jiami_track}")
        para_obj = execjs.compile(open('reverse.js', 'r',encoding='utf-8').read()).call('getEncryptParams',jiami_track,verifyInfo['publicKey'])
        logger.debug(para_obj)
        verify_obj = self.verify(challenge,verifyId,para_obj)
        if verify_obj['success'] == True:
            secret_obj = self.secret_key()
            user_passwd_obj = execjs.compile(open('reverse.js', 'r',encoding='utf-8').read()).call('get_user_passwd',self.username,self.password,secret_obj['secret_key'],secret_obj['iv'])
            self.login(user_passwd_obj['username'],user_passwd_obj['password'],secret_obj['secret_key_id'],verify_obj['result'])
        else:
            logger.error(verify_obj['errorMsg'])
if __name__ == '__main__':
    shl = SmartHotelLogin('dandan', 'xxoo123456')
    shl.run()
