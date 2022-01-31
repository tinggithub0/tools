# 去檔名字尾

import os
 
files = os.listdir(".")
for filename in files:
    file_ext = os.path.splitext(filename)[0]
    old_ext = "_en"
    new_ext = ""
    if old_ext in file_ext:
        # print('11')
        newfile = filename.replace(old_ext, new_ext)
        os.rename(filename, newfile)