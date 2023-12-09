import os

totalSize, fileNum, dirNum = 0, 0, 0

def visitDir(path):
    global totalSize, fileNum, dirNum
    for lists in os.listdir(path):
        sub_path = os.path.join(path, lists)
        if os.path.isfile(sub_path):
            fileNum = fileNum + 1                              # 统计文件数量
            totalSize = totalSize + os.path.getsize(sub_path)  # 统计文件总大小
        elif os.path.isdir(sub_path):
            dirNum = dirNum + 1                                # 统计文件夹数量
            visitDir(sub_path)                                 # 递归遍历子文件夹

def compute(path):
    if not os.path.isdir(path):
        print(f'Error: "{path}" is not a directory or does not exist.')
        return
    visitDir(path)

def sizeConvert(size):                                       # 单位换算
    K, M, G = 1024, 1024**2, 1024**3
    if size >= G:
        return str(size/G) + 'G Bytes'
    elif size >= M:
        return str(size/M) + 'M Bytes'
    elif size >= K:
        return str(size/K) + 'K Bytes'
    else:
        return str(size) + 'Bytes'

def output(path):
    print(f'The total size of {path} is:{sizeConvert(totalSize)}({totalSize} Bytes)')
    print(f'The total number of files in {path} is: {fileNum}')
    print(f'The total number of directories in {path} is: {dirNum}')

if __name__ == '__main__':
    path = r'D:\教学课件\Python程序设计基础（第3版）'
    compute(path)
    output(path)
