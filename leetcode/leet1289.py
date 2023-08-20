import heapq
import math
from collections import Counter, deque
from functools import cache
from itertools import product
from typing import List, Optional


# 1289. 下降路径最小和 II
# 困难
# 给你一个 n x n 整数矩阵 grid ，请你返回 非零偏移下降路径 数字和的最小值。
#
# 非零偏移下降路径 定义为：从 grid 数组中的每一行选择一个数字，且按顺序选出来的数字中，相邻数字不在原数组的同一列。
#
#
#
# 示例 1：
#
#
#
# 输入：grid = [[1,2,3],[4,5,6],[7,8,9]]
# 输出：13
# 解释：
# 所有非零偏移下降路径包括：
# [1,5,9], [1,5,7], [1,6,7], [1,6,8],
# [2,4,8], [2,4,9], [2,6,7], [2,6,8],
# [3,4,8], [3,4,9], [3,5,7], [3,5,9]
# 下降路径中数字和最小的是 [1,5,7] ，所以答案是 13 。
# 示例 2：
#
# 输入：grid = [[7]]
# 输出：7

class Solution:
    def minFallingPathSum(self, grid: List[List[int]]) -> int:
        dp = [0] * len(grid[0])

        for i in range(len(grid)):
            mi1 = dp[0]
            ind = 0
            for j in range(1, len(grid[0])):
                if dp[j] < mi1:
                    mi1 = dp[j]
                    ind = j
            mi2 = math.inf
            for j in range(len(grid[0])):
                if mi1 <= dp[j] < mi2 and j != ind:
                    mi2 = dp[j]
            mi2 = mi1 if mi2 == math.inf else mi2

            for j in range(len(grid[0])):
                if dp[j] == mi1:
                    dp[j] = mi2 + grid[i][j]
                else:
                    dp[j] = mi1 + grid[i][j]
        return min(dp)




if __name__ == "__main__":
    grid = [[1,2,3],[4,5,6],[7,8,9]]

    test = Solution().minFallingPathSum(grid)
    print(test)
