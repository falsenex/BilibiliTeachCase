import math
import random
from captcha_recognizer.recognizer import Recognizer
from loguru import logger
def get_distance1(bg_img):
    recognizer = Recognizer()
    box, confidence = recognizer.identify_gap(source=bg_img, verbose=False)
    print(confidence)
    return int(box[0]/312*260 - 7)
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
bg_img = "restored_bg.jpg"
distance = get_distance1(bg_img)
trace_str,total_time = generate_slider_trace(distance)
logger.warning(f'滑动距离是==>>{distance},滑动轨迹是==>>{trace_str}')