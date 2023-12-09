import re
from docx import Document

result = {'li':[], 'fig':[], 'tab':[]}
doc = Document('《Python可以这样学》书稿.docx')

for p in doc.paragraphs:               # 遍历文档所有段落
    t = p.text                         # 获取每一段的文本
    if re.match('例\d+-\d+ ', t):      # 例题
        result['li'].append(t)
    elif re.match('图\d+-\d+ ', t):    # 插图
        result['fig'].append(t)
    elif re.match('表\d+-\d+ ', t):    # 表格
        result['tab'].append(t)

for key, values in result.items():              # 输出结果
    print('='*30)
    for value in values:
        print(value)
