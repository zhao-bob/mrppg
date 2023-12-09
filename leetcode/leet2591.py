import collections
import heapq
import math
from bisect import bisect_right
from collections import Counter, deque
from functools import cache
from itertools import product
from typing import List, Optional


# 2591. 将钱分给最多的儿童
# 提示
# 简单
# 37
# 相关企业
# 给你一个整数 money ，表示你总共有的钱数（单位为美元）和另一个整数 children ，表示你要将钱分配给多少个儿童。
#
# 你需要按照如下规则分配：
#
# 所有的钱都必须被分配。
# 每个儿童至少获得 1 美元。
# 没有人获得 4 美元。
# 请你按照上述规则分配金钱，并返回 最多 有多少个儿童获得 恰好 8 美元。如果没有任何分配方案，返回 -1 。
#
#
#
# 示例 1：
#
# 输入：money = 20, children = 3
# 输出：1
# 解释：
# 最多获得 8 美元的儿童数为 1 。一种分配方案为：
# - 给第一个儿童分配 8 美元。
# - 给第二个儿童分配 9 美元。
# - 给第三个儿童分配 3 美元。
# 没有分配方案能让获得 8 美元的儿童数超过 1 。
# 示例 2：
#
# 输入：money = 16, children = 2
# 输出：2
# 解释：每个儿童都可以获得 8 美元。

class Solution:
    def distMoney(self, money: int, children: int) -> int:
        if money < children:
            return -1
        if money > children * 8:
            return children - 1
        elif money == children * 8:
            return children
        else:
            k = money // 8
            while k > 0:
                if children - k <= money - k * 8 and (money - k * 8 != 4 or children - k != 1):
                    return k
                k -= 1
            return k


if __name__ == "__main__":
    money = 16
    children = 10

    test = Solution().distMoney(money, children)

    print(test)
