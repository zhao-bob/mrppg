from os import listdir
from os.path import join, isfile, isdir

def listDirWidthFirst(directory):
    '''广度优先遍历文件夹'''
    # 使用列表存放需要遍历但还没遍历的文件夹
    dirs = [directory]
    # 如果还有没遍历过的文件夹，继续循环
    while dirs:
        # 遍历还没遍历过的第一项
        current = dirs.pop(0)
        # 遍历该文件夹，如果是文件就直接输出显示
        # 如果是文件夹，输出显示后，标记为待遍历项
        for subPath in listdir(current):
            path = join(current, subPath)
            if isfile(path):
                print(path)
            elif isdir(path):
                print(path)
                dirs.append(path)

listDirWidthFirst('.')
