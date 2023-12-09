import pandas as pd

# 读取数据
df = pd.read_excel('电影导演演员.xlsx')
# 第一种方法，统计出现次数（参演电影数量）最多的3个演员的名字以及出现次数
print(pd.value_counts('，'.join(df.演员.values).split('，')).nlargest(3))
# 第二种方法
df.演员 = df.演员.str.split('，')
print(df.explode('演员').groupby('演员').count()
      .nlargest(3, '电影名称')['电影名称'])
