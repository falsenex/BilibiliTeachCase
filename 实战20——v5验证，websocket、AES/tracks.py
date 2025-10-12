import random
import time
import math

def generate_slider_track(distance, mode='smooth', noise=0.2, duration=1000, y_variation=3):
    """
    生成滑块轨迹

    参数:
        distance: 滑动的总距离
        mode: 轨迹模式 - 'smooth'(平滑), 'natural'(自然), 'hesitate'(犹豫)
        noise: 轨迹噪声系数 (0-1)
        duration: 滑动持续时间(毫秒)
        y_variation: y轴最大变化范围

    返回:
        逗号分隔的轨迹字符串
    """
    # 生成开始和结束时间戳
    start_time = int(time.time() * 1000)
    end_time = start_time + duration

    # 初始化轨迹列表
    track = [str(start_time)]

    # 基础y坐标和时间增量
    y_base = -24
    current_time = 0

    # 根据模式选择不同的轨迹生成策略
    if mode == 'smooth':
        # 平滑加速减速的轨迹
        points = 20  # 轨迹点数
        for i in range(1, points + 1):
            # 使用正弦函数模拟加速减速
            t = i / points
            x = int(distance * (0.5 - 0.5 * math.cos(t * math.pi)))

            # 添加随机噪声
            noise_factor = random.uniform(-noise, noise) * distance * 0.1
            x = max(0, min(distance, x + noise_factor))

            # 时间均匀增加
            current_time += duration // points

            # y坐标有小幅波动
            y = y_base + random.randint(-y_variation, y_variation)

            # 添加轨迹点
            track.extend([str(current_time), str(int(x)), str(y)])

    elif mode == 'natural':
        # 自然人类滑动轨迹
        current_x = 0
        remaining_distance = distance

        while remaining_distance > 0:
            # 动态调整步长，模拟人类滑动的速度变化
            progress = current_x / distance
            if progress < 0.2:  # 开始加速
                step_range = (1, 3)
            elif progress < 0.8:  # 中间匀速
                step_range = (2, 5)
            else:  # 末尾减速
                step_range = (1, 2)

            step = min(random.randint(*step_range), remaining_distance)
            current_x += step
            remaining_distance -= step

            # 时间增量，速度变化时时间间隔也变化
            time_factor = 1.0
            if step > 3:
                time_factor = 0.8  # 速度快时时间间隔短
            elif step < 2:
                time_factor = 1.2  # 速度慢时时间间隔长

            current_time += max(10, int(random.randint(20, 60) * time_factor))

            # y坐标有小幅波动
            y = y_base + random.randint(-y_variation, y_variation)

            # 添加轨迹点
            track.extend([str(current_time), str(current_x), str(y)])

    elif mode == 'hesitate':
        # 有犹豫的滑动轨迹
        current_x = 0
        remaining_distance = distance

        while remaining_distance > 0:
            # 偶尔犹豫（小幅后退）
            if random.random() < 0.1 and current_x > 5:
                step = -random.randint(1, 3)
                current_time += random.randint(50, 150)  # 犹豫时时间间隔更长
            else:
                step = min(random.randint(1, 5), remaining_distance)
                current_time += random.randint(20, 60)

            current_x += step
            current_x = max(0, current_x)  # 确保x不会为负
            remaining_distance = distance - current_x

            # y坐标有小幅波动
            y = y_base + random.randint(-y_variation, y_variation)

            # 添加轨迹点
            track.extend([str(current_time), str(current_x), str(y)])

    # 确保最终到达精确的目标距离
    if int(track[-2]) != distance:
        current_time += random.randint(10, 50)
        track.extend([str(current_time), str(distance), str(y_base)])

    # 添加结束时间戳
    track.append(str(end_time))

    # 拼接成逗号分隔的字符串
    track_str = ",".join(track)

    return track_str


# 示例使用
if __name__ == "__main__":


    # 不同模式的轨迹示例
    smooth_track = generate_slider_track(72, mode='smooth')
    natural_track = generate_slider_track(72, mode='natural')
    hesitate_track = generate_slider_track(72, mode='hesitate')

    print("平滑轨迹:", smooth_track)
    print("自然轨迹:", natural_track)
    print("犹豫轨迹:", hesitate_track)
