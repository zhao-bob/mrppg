from os import listdir
from os.path import isdir, join

NotRepeatedLines = []                         # 保存非重复的代码行
file_num = 0                                  # 文件数量
code_num = 0                                  # 代码总行数

def LinesCount(directory):
    global file_num, code_num

    for filename in listdir(directory):
        temp = join(directory, filename)
        if isdir(temp):                                # 递归遍历子文件夹
            LinesCount(temp)
        elif temp.endswith('.cpp'):                    # 只考虑.cpp文件
            file_num += 1
            with open(temp, 'r') as fp:
                for line in fp:
                    line = line.strip()                # 删除两端的空白字符
                    if not line:
                        continue
                    if line not in NotRepeatedLines:
                        NotRepeatedLines.append(line)  # 记录非重复行
                    code_num += 1                      # 记录所有代码行

LinesCount(r'D:\教学课件')
print('总行数：{0}，非重复行数：{1}'.format(code_num, len(NotRepeatedLines)))
print('文件数量：{0}'.format(file_num))
