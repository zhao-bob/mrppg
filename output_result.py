# coding=utf-8
# 根据空格和换行对数据进行提取并输出
import os

filename = 'P2_No1.txt'  # 给定文件路径
imagename = 'P2_No1.jpg'
lines = ''  # 用于将存储行的变量提前声明为string格式，避免编译器自动声明时可能由于第一行的特殊情况造成的数据类型错误

with open(filename, 'r') as file_to_read:  # 打开文件，将其值赋予file_to_read
    count = [0] * 10
    total = 0
    while True:
        lines = file_to_read.readline()  # 整行读取数据
        if not lines:  # 若该行为空
            break  # 喀嚓
        else:
            this_lines = lines.split()  # 根据空格对字符串进行切割，由于切割后的数据类型有所改变(str-array)建议新建变量进行存储
            # for this_line in this_lines:  # 遍历数组并输出
            #     print(this_line)  # 直接在这里写处理代码就可以了，因为切割后的数组是按照顺序排列的，并且自动剔除了换行符
            # 但仍需注意，调试后发现切割后进行遍历的this_line变量为str格式，可能需要强制类型转换才能作为数字进行计算，所以这段代码同样支持英语汉语的分割输出
            if this_lines[0].isdigit():
                count[int(this_lines[0])] += 1
                total += 1
    print("图片\"%s\"中人群总数%u人，红色系%u人，蓝色系%u人，黑色系%u人" % (imagename, total, count[1], count[0], count[2]))
    # 0代表蓝色，1代表红色，2代表黑色

# print("\nFinsh!")
