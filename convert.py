from moviepy.editor import *
import os

def mp4_to_gif(mp4_path, gif_path):
    # 加载MP4视频
    video = VideoFileClip(mp4_path)
    
    # 将视频转换为GIF动画
    video.write_gif(gif_path)

# 指定MP4文件路径和GIF文件路径
# in_path_root = ".\static\\compare_examples\\videos"
# out_path_root = ".\static\\compare_examples\\gifs"
in_path_root = "..\..\changed_video"
out_path_root = "..\..\changed_video"


input_dirs = os.listdir(in_path_root)
for name in input_dirs:
    order,_ = name.split(".")
    mp4_path = os.path.join(in_path_root,name)
    gif_path = os.path.join(out_path_root,order+".gif")
    mp4_to_gif(mp4_path, gif_path)