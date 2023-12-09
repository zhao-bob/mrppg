with open('sample.txt', 'r+') as fp:        # 'r+'模式可读可写
    print(fp.read(20))                      # 读取前20个字符
    fp.seek(5)                              # 定位到下标5的字节位置
    fp.write('Python')                      # 写入新内容，覆盖原内容
    fp.seek(0)                              # 把文件指针定位到文件开始处
    print(fp.read(20))                      # 重新读取前20个字符
