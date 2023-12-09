import sqlite3
import string

# 包含yield语句的函数可以用来创建生成器对象
def char_generator():
    for c in string.ascii_lowercase:
        yield (c,)

conn = sqlite3.connect(':memory:')
cur = conn.cursor()
cur.execute('CREATE TABLE characters(c)')
# 使用生成器对象得到参数
cur.executemany('INSERT INTO characters(c) VALUES(?)', char_generator())
cur.execute('SELECT c FROM characters')
print(cur.fetchall())
