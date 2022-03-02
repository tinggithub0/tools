import os
import csv
import openpyxl


# 補齊短的 list
def fill_up_length(list1, list2):
    len_list1 = len(list1)
    len_list2 = len(list2)
    if len_list1 > len_list2:
        while len_list1 > len_list2:
            list2.append('')
            len_list2 = len(list2)
    elif len_list2 > len_list1:
        while len_list2 > len_list1:
            list1.append('')
            len_list1 = len(list1)

# 去掉副檔名
def remove_suffix(filname):
    return filname.split('.')[0]


dir1 = 'C:/web/cash/mem/www/tpl/common/images/bank'
dir2 = 'C:/web/cash/mem/mobile/tpl/common/images/bank'
filename_dict = {}

# 讀資料夾檔名
files1 = os.listdir(dir1)
files2 = os.listdir(dir2)
fill_up_length(files1, files2)

# 寫到 excel
workbook = openpyxl.Workbook()
worksheet = workbook.active

for index, (file1, file2) in enumerate(zip(files1, files2)):
    file1 = remove_suffix(file1)
    file2 = remove_suffix(file2)

    worksheet[f'A{index+1}'] = file1
    worksheet[f'B{index+1}'] = file2

workbook.save('new.xlsx')

# 寫到 csv
with open('new.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile, delimiter='	')

    for file1, file2 in zip(files1, files2):
        file1 = remove_suffix(file1)
        file2 = remove_suffix(file2)

        writer.writerow([file1, file2])
