from re import findall

fn = r'气壮山河的凯歌 永载史册的丰碑——写在中国人民志愿军抗美援朝出国作战70周年之际.txt'

with open(fn, encoding='utf8') as fp:
    content = fp.read()

pattern = r'((((\d{4}年)?\d{1,2}月\d{1,2}日)|(\d{4}年)).+?。”?)'
result = findall(pattern, content)
for item in result:
    if '）' not in item[0]:
        print(item[0])
