from random import random

def 轮盘游戏(奖项分布):
    本次转盘读数 = random()
    for k, v in 奖项分布.items():
        if v[0] <= 本次转盘读数 < v[1]:
            return k

奖项分布 = {'一等奖': (0,0.08), '二等奖': (0.08,0.3), '三等奖': (0.3,1.0)}

中奖情况 = dict()
for i in range(10000):
    本次战况 = 轮盘游戏(奖项分布)
    中奖情况[本次战况] = 中奖情况.get(本次战况, 0) + 1

for item in 中奖情况.items():
    print(item)
