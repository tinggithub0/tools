# ζͺεζεΊ
import os

dir = './cut_src/'
images = os.listdir(dir)
for index, img in enumerate(images):
    os.rename(f'{dir}{img}', f'{dir}{index}.png')

