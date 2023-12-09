import sqlite3

database_name = '核心价值观.sqlite'
table_name = 'information'

def do_sql(sql):
    # 执行指定的SQL语句，如果数据库文件不存在，连接时会创建空数据库
    with sqlite3.connect(database_name) as conn:
        conn.execute(sql)
        conn.commit()

def get_data(sql):
    # 根据指定的SQL查询语句返回得到的数据集
    with sqlite3.connect(database_name) as conn:
        cur = conn.cursor()
        cur.execute(sql)
        return cur.fetchall()

def has_table(table):
    # 检查数据库中是否有指定的数据表
    sql = f'SELECT COUNT(*) FROM sqlite_master WHERE name="{table}"'
    return get_data(sql)[0][0] == 1

if not has_table(table_name):
    # 创建数据表
    sql = f'CREATE TABLE {table_name}(category TEXT, content TEXT)'
    do_sql(sql)

# 往数据库中写入数据
content = (('国家', '富强、民主、文明、和谐'), ('社会', '自由、平等、公正、法治'),
           ('公民', '爱国、敬业、诚信、友善'))
with sqlite3.connect(database_name) as conn:
    # 删除原有的所有记录
    conn.execute(f'DELETE FROM {table_name}')
    # 插入新记录
    conn.executemany(f'INSERT INTO {table_name} VALUES(?,?)', content)
    conn.commit()
    # 压缩数据库文件，释放无用空间
    conn.execute('vacuum')

with sqlite3.connect(database_name) as conn:
    cur = conn.cursor()
    cur.execute(f'SELECT * FROM {table_name}')
    # 读取一条记录
    print(cur.fetchone())
    # 从第2条记录开始，继续读取两条记录
    print(cur.fetchmany(2))

with sqlite3.connect(database_name) as conn:
    cur = conn.cursor()
    cur.execute(f'SELECT * FROM {table_name}')
    # 读取全部记录
    print(cur.fetchall())
