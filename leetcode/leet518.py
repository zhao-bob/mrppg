# 518. 零钱兑换 II
# 中等
# 相关标签
# 相关企业
# 给你一个整数数组 coins 表示不同面额的硬币，另给一个整数 amount 表示总金额。
#
# 请你计算并返回可以凑成总金额的硬币组合数。如果任何硬币组合都无法凑出总金额，返回 0 。
#
# 假设每一种面额的硬币有无限个。
#
# 题目数据保证结果符合 32 位带符号整数。
#
#
#
# 示例 1：
#
# 输入：amount = 5, coins = [1, 2, 5]
# 输出：4
# 解释：有四种方式可以凑成总金额：
# 5=5
# 5=2+2+1
# 5=2+1+1+1
# 5=1+1+1+1+1
# 示例 2：
#
# 输入：amount = 3, coins = [2]
# 输出：0
# 解释：只用面额 2 的硬币不能凑成总金额 3 。
# 示例 3：
#
# 输入：amount = 10, coins = [10]
# 输出：1
#
#
# 提示：
#
# 1 <= coins.length <= 300
# 1 <= coins[i] <= 5000
# coins 中的所有值 互不相同
# 0 <= amount <= 5000
#

import heapq
import math
from collections import Counter, deque, defaultdict
from datetime import date
from functools import cache
from typing import List, Optional

from sortedcontainers import SortedList


class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        dp = [0] * (amount + 1)
        dp[0] = 1
        for c in coins:
            for i in range(1, amount + 1):
                if i - c >= 0:
                    dp[i] += dp[i - c]
        return dp[-1]
        # coins.sort(reverse=True)
        # cl = len(coins)
        #
        # @cache
        # def subchange(a, i):
        #     res = 0
        #     for k in range(i, cl):
        #         if a > coins[k]:
        #             res += subchange(a - coins[k], k)
        #         elif a == coins[k]:
        #             res += 1
        #     return res
        #
        # return subchange(amount, 0)


if __name__ == "__main__":
    amount = 1000
    coins = [1, 2, 5]
    test = Solution().change(amount, coins)
    print(test)
