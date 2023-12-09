import csv

with open('test.csv', 'w', newline='') as fp:
    test_writer = csv.writer(fp, delimiter=' ', quotechar='"')
    test_writer.writerow(['red', 'blue', 'green'])  # 写入一行内容
    test_writer.writerow(['test_string']*5)

with open('test.csv', newline='') as fp:
    test_reader = csv.reader(fp, delimiter=' ', quotechar='"')
    for row in test_reader:                         # 遍历所有行
        print(row)                                  # 每行作为一个列表返回

with open('test.csv', newline='') as fp:
    test_reader = csv.reader(fp, delimiter=':', quotechar='"')
                                                   # 把冒号当作分隔符
                                                   # 不把空格当作分隔符
    for row in test_reader:
        print(row)

with open('names.csv', 'w') as fp:
    headers = ['姓氏', '名字']
    test_dictWriter = csv.DictWriter(fp, fieldnames=headers)
    test_dictWriter.writeheader()
    test_dictWriter.writerow({'姓氏': '张', '名字': '三'})
    test_dictWriter.writerow({'姓氏': '李', '名字': '四'})
    test_dictWriter.writerow({'姓氏': '王', '名字': '五'})
with open('names.csv') as fp:
    test_dictReader = csv.DictReader(fp)
    print(','.join(test_dictReader.fieldnames))
    for row in test_dictReader:
        print(row['姓氏'], ',', row['名字'])
