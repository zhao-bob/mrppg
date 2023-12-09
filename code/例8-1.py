import re

# 在三引号内每行后面加反斜线，表示不换行
telNumber = '''Suppose my Phone No. is 0535-1234567,\
yours is 010-12345678,\
his is 025-87654321.'''

pattern = r'\d{3,4}-\d{7,8}'
print(re.findall(pattern, telNumber))
