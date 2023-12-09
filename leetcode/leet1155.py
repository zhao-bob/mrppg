import heapq
import math
from collections import Counter
from functools import cache
from typing import List
from sortedcontainers import SortedList


# 1155. 掷骰子等于目标和的方法数
# 提示
# 中等
# 186
# 相关企业
# 这里有 n 个一样的骰子，每个骰子上都有 k 个面，分别标号为 1 到 k 。
#
# 给定三个整数 n ,  k 和 target ，返回可能的方式(从总共 kn 种方式中)滚动骰子的数量，使正面朝上的数字之和等于 target 。
#
# 答案可能很大，你需要对 109 + 7 取模 。
#
#
#
# 示例 1：
#
# 输入：n = 1, k = 6, target = 3
# 输出：1
# 解释：你扔一个有 6 个面的骰子。
# 得到 3 的和只有一种方法。
# 示例 2：
#
# 输入：n = 2, k = 6, target = 7
# 输出：6
# 解释：你扔两个骰子，每个骰子有 6 个面。
# 得到 7 的和有 6 种方法：1+6 2+5 3+4 4+3 5+2 6+1。
# 示例 3：
#
# 输入：n = 30, k = 30, target = 500
# 输出：222616187
# 解释：返回的结果必须是对 109 + 7 取模。
#


class Solution:
    def numRollsToTarget(self, n: int, k: int, target: int) -> int:
        @cache
        def roll(r, t):
            if t < 0 or r > n:
                return 0
            elif t == 0:
                if r != n:
                    return 0
                else:
                    return 1
            else:
                if r == n - 1 and t <= k:
                    return 1
            res = 0
            for i in range(k):
                res += roll(r + 1, t - i - 1)
            return res % (10**9 + 7)

        return roll(0, target)



if __name__ == "__main__":
    n = 30
    k = 30
    target = 1000
    test = Solution().numRollsToTarget(n, k, target)
    print(test)
