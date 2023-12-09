import sqlite3

# 自定义迭代器，按顺序生成小写字母
class IterChars:
    def __init__(self):
        self.count = ord('a')

    def __iter__(self):
        return self

    def __next__(self):
        if self.count > ord('z'):
            raise StopIteration
        self.count += 1
        return (chr(self.count-1),)
    
conn = sqlite3.connect(':memory:')
cur = conn.cursor()
cur.execute('CREATE TABLE characters(c)')
# 创建迭代器对象
theIter = IterChars()
# 插入记录，每次插入一个英文小写字母
cur.executemany('INSERT INTO characters(c) VALUES(?)', theIter)
# 读取并显示所有记录
cur.execute('SELECT c FROM characters')
print(cur.fetchall())
