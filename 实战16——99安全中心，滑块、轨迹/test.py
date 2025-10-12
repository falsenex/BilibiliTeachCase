#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
@Project ：pythonProject 
@File    ：test.py
@IDE     ：PyCharm 
@Author  ：haozaispider
@Date    ：2025/5/12 下午6:29 
'''
import time
from datetime import datetime, timezone, timedelta

def get_time():

    now = datetime.now(timezone(timedelta(hours=8)))
    # time_str = now.strftime('%a %b %d %Y %H:%M:%S GMT%z')

    # 手动添加中文时区名称
    return now
time1 = get_time()
time.sleep(2)
time2 = get_time()
print(time2 - time1)
