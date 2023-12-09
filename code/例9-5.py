with open('data.txt', 'r') as fp:
    data = fp.read()                              # 读取所有行

data = data.split(',')                            # 分隔得到所有数字字符串
data = [int(item) for item in data]               # 转换为数字
data.sort()                                       # 升序排序
data = ','.join(map(str, data))                   # 将结果转换为字符串

with open('data_asc.txt', 'w') as fp:             # 将结果写入文件
    fp.write(data)
