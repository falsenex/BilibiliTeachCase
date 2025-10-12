#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
@Project ：pythonProject 
@File    ：轨迹生成.py
@IDE     ：PyCharm 
@Author  ：haozaispider
@Date    ：2025/7/9 下午2:15 
'''
import random
import math
"u=17|d=0,0,0:3,0,147:6,0,162:10,0,177:14,0,193:16,0,209:19,0,226:21,0,242:22,0,257:27,0,273:32,0,289:36,0,306:39,0,322:42,0,338:44,0,353:46,0,370:50,0,386:52,0,402:55,0,417:57,0,433:58,0,449:60,0,465:61,0,481:62,0,529:63,0,601:65,0,617:68,0,633:71,0,649:72,0,666:73,0,681:75,0,713:76,0,730:77,0,746:79,0,777:80,0,793:81,0,809:83,0,833:84,1,994:84,2,1009:83,2,1033:81,2,1049:77,2,1065:72,2,1082:66,2,1097:61,1,1113:56,1,1129:55,1,1145:52,1,1161:49,1,1177:44,1,1193:41,1,1209:39,1,1219:36,1,1233:34,1,1249:33,1,1266:31,1,1281:30,1,1306:29,1,1386:28,1,1482:27,1,1498:26,1,1530:25,1,1569:24,1,1650:23,1,1666:22,1,1762:22,0,1778:21,0,1802:20,0,1874:19,0,1970:18,0,2554:17,0,2633:17,0,3778|t=3778"
"u=97|d=0,0,0:2,0,94:6,0,110:11,0,126:16,0,143:20,0,158:23,0,174:27,0,190:28,0,206:29,0,222:30,0,245:32,0,269:34,0,285:35,0,301:37,0,317:40,0,333:41,0,349:43,0,365:44,0,381:46,0,397:49,0,413:52,0,430:54,0,445:56,0,461:58,0,477:61,0,493:63,0,509:66,0,525:68,0,541:71,0,557:74,0,573:76,0,589:78,0,613:79,0,629:81,0,678:82,0,702:83,0,717:84,0,733:85,0,773:86,0,838:87,0,1061:88,0,1093:89,0,1150:90,0,1189:91,0,1311:92,0,1350:93,0,1414:94,0,1478:95,0,1622:96,0,1670:97,0,1974:97,0,2974|t=2974"

def generate_slider_trace(distance, segments=60):
    total_time = distance * 13
    """
    生成更精确模拟人类操作的滑块轨迹，确保y坐标在0-3之间

    参数:
    distance (int): 滑块需要移动的总距离
    total_time (int): 总耗时(毫秒)
    segments (int): 轨迹分段数

    返回:
    str: 格式化的轨迹数据字符串
    """
    # 轨迹点列表，初始位置
    trace_points = [(0, 0, 0)]
    current_x = 0
    current_y = 0
    time = 0

    # 轨迹阶段划分
    accel_ratio = 0.2  # 加速阶段比例
    steady_ratio = 0.6  # 匀速阶段比例
    adjust_ratio = 0.2  # 调整阶段比例

    accel_points = max(1, int(segments * accel_ratio))
    steady_points = max(1, int(segments * steady_ratio))
    adjust_points = max(1, segments - accel_points - steady_points)

    # 生成加速阶段轨迹 (开始较慢，逐渐加速)
    for i in range(accel_points):
        progress = i / accel_points
        # 使用指数函数模拟加速
        smooth_progress = 1 - math.pow(1 - progress, 3)
        target_x = int(distance * accel_ratio * smooth_progress)

        time_gap = random.randint(15, 30)
        time += time_gap

        # y轴微调，确保在0-3之间
        if current_y < 3 and random.random() > 0.5:
            current_y += 1
        elif current_y > 0 and random.random() < 0.2:
            current_y -= 1

        # 更新x坐标并确保不超过当前阶段的目标
        current_x = min(target_x, current_x + random.randint(1, 3))
        trace_points.append((current_x, current_y, time))

    # 生成匀速阶段轨迹
    steady_distance = int(distance * steady_ratio)
    start_steady_x = current_x

    for i in range(steady_points):
        # 计算匀速阶段的目标位置
        target_x = start_steady_x + int(steady_distance * (i + 1) / steady_points)

        time_gap = random.randint(15, 35)
        time += time_gap

        # y轴微调，确保在0-3之间
        if current_y < 3 and random.random() > 0.6:
            current_y += 1
        elif current_y > 0 and random.random() < 0.3:
            current_y -= 1

        # 更新x坐标，确保匀速增长
        step = max(1, (target_x - current_x) // (steady_points - i))
        current_x = min(target_x, current_x + step)
        trace_points.append((current_x, current_y, time))

    # 生成调整阶段轨迹 (接近终点时的微调)
    remaining_distance = distance - current_x
    start_adjust_x = current_x

    for i in range(adjust_points):
        # 接近终点时的过冲和回调
        overshoot = int(remaining_distance * 0.3 * math.sin((i + 1) * 0.6))
        target_x = start_adjust_x + remaining_distance + overshoot

        time_gap = random.randint(20, 50)
        time += time_gap

        # y轴微调，确保在0-3之间
        if current_y < 3 and random.random() > 0.7:
            current_y += 1
        elif current_y > 0 and random.random() < 0.4:
            current_y -= 1

        # 逐步接近目标位置
        if current_x < target_x:
            current_x = min(target_x, current_x + random.randint(1, 3))
        else:
            current_x = max(target_x, current_x - random.randint(1, 3))

        # 确保最终停在目标位置
        if i == adjust_points - 1:
            current_x = distance

        trace_points.append((current_x, current_y, time))

    # 确保最后一个点的时间是总时间
    if trace_points[-1][2] != total_time:
        last_point = list(trace_points[-1])
        last_point[2] = total_time
        trace_points[-1] = tuple(last_point)

    # 格式化轨迹数据
    trace_str = ":".join([f"{p[0]},{p[1]},{p[2]}" for p in trace_points])
    return trace_str ,total_time


# 示例使用
if __name__ == "__main__":
    # 生成距离为175的轨迹数据
    distance = 175
    trace_data = generate_slider_trace(distance)
    print(trace_data)
    # d =
    # 0, 0, 0:
    # 0, 1, 42:
    # 1, 1, 74:
    # 6, 1, 91:
    # 13, 1, 107:
    # 19, 2, 122:
    # 24, 2, 138:
    # 28, 3, 154:
    # 30, 3, 166:
    # 34, 3, 178:
    # 38, 3, 195:
    # 41, 3, 210:
    # 43, 3, 227:
    # 48, 3, 242:
    # 57, 3, 258:
    # 64, 3, 274:
    # 68, 3, 290:
    # 73, 3, 306:
    # 78, 3, 322:
    # 82, 3, 338:
    # 85, 3, 349:
    # 90, 3, 362:
    # 94, 3, 378:
    # 97, 3, 394:
    # 103, 3, 410:
    # 106, 3, 427:
    # 109, 3, 443:
    # 112, 3, 467:
    # 114, 3, 490:
    # 117, 3, 507:
    # 119, 3, 522:
    # 122, 3, 538:
    # 123, 3, 548:
    # 124, 3, 563:
    # 127, 3, 587:
    # 129, 3, 602:
    # 132, 3, 618:
    # 133, 3, 629:
    # 136, 3, 642:
    # 137, 3, 659:
    # 140, 3, 682:
    # 142, 3, 698:
    # 143, 3, 723:
    # 145, 3, 739:
    # 146, 3, 754:
    # 149, 3, 778:
    # 150, 3, 810:
    # 151, 3, 851:
    # 152, 3, 867:
    # 153, 3, 899:
    # 154, 3, 923:
    # 155, 3, 955:
    # 157, 3, 986:
    # 158, 3, 1018:
    # 159, 3, 1067:
    # 160, 3, 1098:
    # 161, 3, 1124:
    # 162, 3, 1179:
    # 163, 3, 1218:
    # 164, 3, 1250:
    # 165, 3, 1275:
    # 166, 3, 1314:
    # 167, 3, 1403:
    # 168, 3, 1427:
    # 169, 3, 1467:
    # 170, 3, 1514:
    # 171, 3, 1554:
    # 172, 3, 1611:
    # 173, 3, 1635:
    # 174, 3, 1691:
    # 175, 3, 1763:
    # 175, 3, 2291