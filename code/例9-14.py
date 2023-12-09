import struct

n = 666666
x = 3.1415926
b = True
s = 'No1中国'
sn = struct.pack('if?', n, x, b)     # 序列化，i表示整数，f表示实数，?表示逻辑值
with open('sample_struct.dat', 'wb') as f:
    f.write(sn)
    f.write(s.encode())              # 字符串需要编码为字节串再写入文件

with open('sample_struct.dat', 'rb') as f:
    sn = f.read(9)                   # 整数和实数各占4个字节，布尔值占1个字节
    tu = struct.unpack('if?', sn)    # 使用指定格式反序列化，得到元组
    n, x, b1 = tu                    # 序列解包
    print('n=', n, 'x=', x, 'b1=', b1)
    s = f.read(9).decode()           # 字符串解码
    print('s=', s)
