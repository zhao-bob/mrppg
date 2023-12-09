s = 'Hello world\n文本文件的读取方法\n文本文件的写入方法\n'

with open('sample.txt', 'w') as fp:    # Windows系统中默认使用cp936编码
    fp.write(s)

with open('sample.txt') as fp:         # Windows系统中默认使用cp936编码
    print(fp.read())
