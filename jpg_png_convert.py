# 當前資料夾 png 轉 jpg 或 jpg 轉 png 或 jpeg 轉 png

# 引入
from PIL import Image
import os

# 設定
file_types = [".jpeg", ".jpg", ".png"]

# 讀當前資料夾下所有檔名
dir_files = os.listdir(".")

# 判斷 file type & 轉檔
for filename in dir_files:
    file_name, file_type = os.path.splitext(filename)
    if file_type not in file_types:
        pass
    elif file_type == ".png":
        to_type = ".jpg"
        to_name = file_name + to_type
        
        img = Image.open(filename)
        rgb_img = img.convert('RGB')
        rgb_img.save(to_name, "jpeg")
    elif file_type == ".jpg" or file_type == ".jpeg":
        to_type = ".png"
        to_name = file_name + to_type
        
        img = Image.open(filename)
        rgb_img.save(to_name, "png")

