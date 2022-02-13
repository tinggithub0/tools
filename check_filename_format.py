import re
import os


# image_ori_dir = './test_ori/'
image_ori_dir = './mark/'
image_ori = os.listdir(image_ori_dir)
pattern = r'[0-9]{4}_[0-9]{1,4}.jpg'

for src in image_ori:
    if re.fullmatch(pattern, src) is None:
        print(src)
