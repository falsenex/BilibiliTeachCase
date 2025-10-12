import random
import time


def generate_slider_track(target_distance):
    track = []
    start_time = int(time.time() * 1000)
    current_distance = 0
    current_time = 0
    y_offset = 0

    track.extend([str(start_time)])
    while current_distance < target_distance:
        # 时间步长随机，模拟不均匀采样，20~60ms之间
        time_step = random.randint(20, 60)
        current_time += time_step

        # 横向步长，接近目标时减小步长
        if target_distance - current_distance > 10:
            x_step = random.randint(4, 10)
        else:
            x_step = random.randint(1, 4)

        current_distance += x_step
        if current_distance > target_distance:
            current_distance = target_distance

        # 纵向浮动在-9到9之间，模拟抖动
        y_offset = random.randint(-9, 9)

        track.extend([str(current_time), str(current_distance), str(y_offset)])

    end_date = start_time + current_time + random.randint(100, 500)
    track.extend([str(end_date)])
    track_str = ",".join(track)
    return track_str