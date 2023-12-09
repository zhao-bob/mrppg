from os import listdir
from os.path import join, isfile, isdir

def listDirDepthFirst(directory):
    '''深度优先遍历文件夹'''
    # 遍历文件夹，如果是文件就直接输出
    # 如果是文件夹，就输出显示，然后递归遍历该文件夹
    for subPath in listdir(directory):
        path = join(directory, subPath)
        if isfile(path):
            print(path)
        elif isdir(path):
            print(path)
            listDirDepthFirst(path)

listDirDepthFirst('.')
