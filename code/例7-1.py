from itertools import cycle

def convert(source, key):
    # 对应位置上字符的Unicode编码进行异或运算，异或运算两次可得到原文，即A^B^B=A
    return ''.join(map(lambda s, k: chr(ord(s)^ord(k)), source, cycle(key)))

source = '微信公众号：Python小屋。'
key = '董付国'
encrypted = convert(source, key)
decrypted = convert(encrypted, key)
print(f'原文：{source}\n加密后：{encrypted}\n解密后：{decrypted}')
