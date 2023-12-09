from string import ascii_letters
from os import listdir, rename
from os.path import splitext, join
from random import choices, randint

def randomFilename(directory):
    for fn in listdir(directory):
        # 切分，得到文件名和扩展名
        name, ext = splitext(fn)
        n = randint(5, 20)
        # 生成随机字符串作为新文件名
        newName = ''.join((choices(ascii_letters, k=n)))
        # 修改文件名
        rename(join(directory, fn), join(directory, newName+ext))

randomFilename('C:\\test')
