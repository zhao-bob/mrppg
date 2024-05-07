# 322. 零钱兑换
# 中等
# 相关标签
# 相关企业
# 给你一个整数数组 coins ，表示不同面额的硬币；以及一个整数 amount ，表示总金额。
#
# 计算并返回可以凑成总金额所需的 最少的硬币个数 。如果没有任何一种硬币组合能组成总金额，返回 -1 。
#
# 你可以认为每种硬币的数量是无限的。
#
#
#
# 示例 1：
#
# 输入：coins = [1, 2, 5], amount = 11
# 输出：3
# 解释：11 = 5 + 5 + 1
# 示例 2：
#
# 输入：coins = [2], amount = 3
# 输出：-1
# 示例 3：
#
# 输入：coins = [1], amount = 0
# 输出：0
#
#
# 提示：
#
# 1 <= coins.length <= 12
# 1 <= coins[i] <= 231 - 1
# 0 <= amount <= 104
#

import heapq
import math
from collections import Counter, deque, defaultdict
from datetime import date
from functools import cache
from typing import List, Optional

from sortedcontainers import SortedList


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        a = [math.inf] * (amount + 1)
        a[0] = 0
        for i in range(1, amount + 1):
            for c in coins:
                if i - c >= 0:
                    a[i] = min(a[i - c] + 1, a[i])
        return -1 if a[-1] == math.inf else a[-1]


if __name__ == "__main__":
    coins = [1, 2, 5]
    amount = 11
    test = Solution().coinChange(coins, amount)
    print(test)
