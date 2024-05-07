# 2312. 卖木头块
# 困难
# 相关标签
# 相关企业
# 提示
# 给你两个整数 m 和 n ，分别表示一块矩形木块的高和宽。同时给你一个二维整数数组 prices ，其中 prices[i] = [hi, wi, pricei] 表示你可以以 pricei 元的价格卖一块高为 hi 宽为 wi 的矩形木块。
#
# 每一次操作中，你必须按下述方式之一执行切割操作，以得到两块更小的矩形木块：
#
# 沿垂直方向按高度 完全 切割木块，或
# 沿水平方向按宽度 完全 切割木块
# 在将一块木块切成若干小木块后，你可以根据 prices 卖木块。你可以卖多块同样尺寸的木块。你不需要将所有小木块都卖出去。你 不能 旋转切好后木块的高和宽。
#
# 请你返回切割一块大小为 m x n 的木块后，能得到的 最多 钱数。
#
# 注意你可以切割木块任意次。
#
#
#
# 示例 1：
#
#
#
# 输入：m = 3, n = 5, prices = [[1,4,2],[2,2,7],[2,1,3]]
# 输出：19
# 解释：上图展示了一个可行的方案。包括：
# - 2 块 2 x 2 的小木块，售出 2 * 7 = 14 元。
# - 1 块 2 x 1 的小木块，售出 1 * 3 = 3 元。
# - 1 块 1 x 4 的小木块，售出 1 * 2 = 2 元。
# 总共售出 14 + 3 + 2 = 19 元。
# 19 元是最多能得到的钱数。
# 示例 2：
#
#
#
# 输入：m = 4, n = 6, prices = [[3,2,10],[1,4,2],[4,1,3]]
# 输出：32
# 解释：上图展示了一个可行的方案。包括：
# - 3 块 3 x 2 的小木块，售出 3 * 10 = 30 元。
# - 1 块 1 x 4 的小木块，售出 1 * 2 = 2 元。
# 总共售出 30 + 2 = 32 元。
# 32 元是最多能得到的钱数。
# 注意我们不能旋转 1 x 4 的木块来得到 4 x 1 的木块。
#
#
# 提示：
#
# 1 <= m, n <= 200
# 1 <= prices.length <= 2 * 104
# prices[i].length == 3
# 1 <= hi <= m
# 1 <= wi <= n
# 1 <= pricei <= 106
# 所有 (hi, wi) 互不相同 。
#

import heapq
import math
from collections import Counter, deque, defaultdict
from datetime import date
from functools import cache
from typing import List, Optional

from sortedcontainers import SortedList


class Solution:
    def sellingWood(self, m: int, n: int, prices: List[List[int]]) -> int:
        # dp = [[0] * n for _ in range(m)]
        # p = {}
        # for i in range(len(prices)):
        #     p[(prices[i][0], prices[i][1])] = prices[i][2]
        #
        # if (1, 1) in p:
        #     dp[0][0] = p[(1, 1)]
        # for i in range(1, n):
        #     if (1, i + 1) in p:
        #         dp[0][i] = p[(1, i + 1)]
        #     for j in range(i):
        #         dp[0][i] = max(dp[0][i], dp[0][j] + dp[0][i - j - 1])
        # for i in range(1, m):
        #     if (i + 1, 1) in p:
        #         dp[i][0] = p[(i + 1, 1)]
        #     for j in range(i):
        #         dp[i][0] = max(dp[i][0], dp[j][0] + dp[i - j - 1][0])
        #
        # for i in range(1, m):
        #     for j in range(1, n):
        #         if (i + 1, j + 1) in p:
        #             dp[i][j] = p[(i + 1, j + 1)]
        #         for k in range(i):
        #             dp[i][j] = max(dp[i][j], dp[k][j] + dp[i - k - 1][j])
        #         for k in range(j):
        #             dp[i][j] = max(dp[i][j], dp[i][k] + dp[i][j - k - 1])
        # return dp[-1][-1]
        dp = [[0] * n for _ in range(m)]
        for i in range(len(prices)):
            dp[prices[i][0] - 1][prices[i][1] - 1] = prices[i][2]

        for i in range(1, n):
            for j in range(i):
                dp[0][i] = max(dp[0][i], dp[0][j] + dp[0][i - j - 1])
        for i in range(1, m):
            for j in range(i):
                dp[i][0] = max(dp[i][0], dp[j][0] + dp[i - j - 1][0])

        for i in range(1, m):
            for j in range(1, n):
                for k in range(i // 2 + 1):
                    dp[i][j] = max(dp[i][j], dp[k][j] + dp[i - k - 1][j])
                for k in range(j // 2 + 1):
                    dp[i][j] = max(dp[i][j], dp[i][k] + dp[i][j - k - 1])
        return dp[-1][-1]


if __name__ == "__main__":
    m = 3
    n = 5
    prices = [[1, 4, 2], [2, 2, 7], [2, 1, 3]]

    test = Solution().sellingWood(m, n, prices)
    print(test)
