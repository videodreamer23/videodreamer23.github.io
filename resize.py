from PIL import Image
import os

def resize_image(input_image_path, output_image_path, size):
    # 打开图像文件
    with Image.open(input_image_path) as image:
        # 调整图像大小
        resized_image = image.resize(size)
        
        # 保存调整大小后的图像
        resized_image.save(output_image_path)

target_size = (120, 240)

in_path_root = ".\static\\all_examples\\images"
out_path_root = ".\static\\all_examples\\images"

input_dirs = os.listdir(in_path_root)
for name in input_dirs:
    order,_ = name.split(".")
    input_image_path = os.path.join(in_path_root,name)
    output_image_path = os.path.join(out_path_root,order+".png")
# 调用函数进行图像大小调整
    resize_image(input_image_path, output_image_path, target_size)