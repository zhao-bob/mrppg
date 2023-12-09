import sqlite3
conn = sqlite3.connect(':memory:')
cur = conn.cursor()
cur.execute('CREATE TABLE people(name_last, age)')
who = 'Dong'
age = 38
# 使用问号作为占位符，使用元组提交参数
cur.execute('INSERT INTO people VALUES(?, ?)', (who, age))
# 使用命名变量作为占位符，使用字典提交参数，也可以使用元组(who, age)
cur.execute('SELECT * FROM people WHERE name_last=:who AND age=:age', 
            {'who': who, 'age': age})
print(cur.fetchone())
conn.close()
