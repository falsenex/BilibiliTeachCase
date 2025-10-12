import io
from PIL import Image
from loguru import logger
def recover_image(image_data, recover_array):
    """
    根据还原数组还原被打乱的图片

    Args:
        image_data: 图片数据（bytes 或 PIL.Image 对象）
        recover_array: 还原数组，用于重新排列图片块

    Returns:
        PIL.Image: 还原后的图片对象
    """
    # 处理输入图片数据
    if isinstance(image_data, bytes):
        # 如果是字节数据，转换为PIL Image对象
        original_image = Image.open(io.BytesIO(image_data))
    elif isinstance(image_data, Image.Image):
        # 如果已经是PIL Image对象，直接使用
        original_image = image_data
    else:
        raise ValueError("image_data must be bytes or PIL.Image object")

    # 获取图片尺寸
    width = original_image.width
    height = original_image.height

    # 计算分块参数
    # 还原数组长度的一半就是每行的块数
    blocks_per_row = len(recover_array) // 2

    # 每个块的宽度和高度
    block_width = width // blocks_per_row
    block_height = height // 2

    # 创建新的图片用于存放还原后的结果
    recovered_image = Image.new(original_image.mode, (width, height))

    # 遍历还原数组，重新排列图片块
    for i in range(len(recover_array)):
        # 当前位置在原图中的坐标
        current_col = i % blocks_per_row
        current_row = 1 if i >= blocks_per_row else 0
        current_x = current_col * block_width
        current_y = current_row * block_height

        # 目标位置（根据还原数组的值）
        target_index = recover_array[i]
        target_col = target_index % blocks_per_row
        target_row = 1 if target_index >= blocks_per_row else 0
        target_x = target_col * block_width
        target_y = target_row * block_height

        # 从原图中提取当前块
        block = original_image.crop((current_x, current_y,
                                     current_x + block_width,
                                     current_y + block_height))

        # 将块放置到还原图片的目标位置
        recovered_image.paste(block, (target_x, target_y))

    return recovered_image
def recover_image_from_file(image_path, recover_array, output_path=None):
    """
    从文件读取图片并还原

    Args:
        image_path: 输入图片文件路径
        recover_array: 还原数组
        output_path: 输出图片文件路径（可选）

    Returns:
        PIL.Image: 还原后的图片对象
    """
    # 读取图片文件
    with open(image_path, 'rb') as f:
        image_data = f.read()

    # 还原图片
    recovered_image = recover_image(image_data, recover_array)

    # 如果指定了输出路径，保存图片
    if output_path:
        recovered_image.save(output_path)
        logger.debug(f"还原后的图片已保存到: {output_path}")

    return recovered_image
# if __name__ == '__main__':
#     recover_image_from_file('test3_bg.webp',[11, 36, 17, 14, 18, 9, 10, 33, 12, 30, 43, 7, 25, 37, 3, 40, 29, 35, 26, 21, 38, 4, 41, 22, 50, 1, 34, 19, 2, 5, 6, 49, 8, 31, 51, 15, 39, 0, 28, 27, 23, 48, 24, 45, 13, 47, 20, 46, 16, 44, 32, 42],'recover_bg3.jpg')
