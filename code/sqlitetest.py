import sqlite3                           # 导入模块
conn = sqlite3.connect('example.db')     # 连接数据库
c = conn.cursor()
# 创建表
# c.execute('CREATE TABLE stocks(date text, trans text, symbol text, qty real, price real)')
# 插入一条记录
c.execute("INSERT INTO stocks VALUES('2023-02-05','SELL', 'RHAT', 1000, 60.14)")
for row in c.execute('SELECT * FROM stocks ORDER BY price DESC'):
    print(row)
# 提交当前事务，保存数据
conn.commit()
# 关闭数据库连接
conn.close()
