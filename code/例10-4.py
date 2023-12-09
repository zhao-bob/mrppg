from os.path import isdir, join, splitext
from os import remove, listdir, chmod, stat

filetypes = ('.tmp', '.log', '.obj', '.txt')     # 指定要删除的文件类型

def delCertainFiles(directory):
    if not isdir(directory):
        return
    for filename in listdir(directory):
        temp = join(directory, filename)
        if isdir(temp):
            delCertainFiles(temp)                # 递归调用
        elif splitext(temp)[1] in filetypes or stat(temp).st_size==0:
            chmod(temp, 0o777)                   # 修改文件属性，获取删除权限
            remove(temp)                         # 删除文件
            print(temp, ' deleted....')

delCertainFiles(r'C:\test')
