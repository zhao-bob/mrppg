import heapq
import math
from collections import Counter, deque
from functools import cache
from itertools import product
from typing import List, Optional

# 931. 下降路径最小和
# 给你一个 n x n 的 方形 整数数组 matrix ，请你找出并返回通过 matrix 的下降路径 的 最小和 。
#
# 下降路径 可以从第一行中的任何元素开始，并从每一行中选择一个元素。在下一行选择的元素和当前行所选元素最多相隔一列（即位于正下方或者沿对角线向左或者向右的第一个元素）。具体来说，位置 (row, col) 的下一个元素应当是 (row + 1, col - 1)、(row + 1, col) 或者 (row + 1, col + 1) 。
#
#
#
# 示例 1：
#
#
#
# 输入：matrix = [[2,1,3],[6,5,4],[7,8,9]]
# 输出：13
# 解释：如图所示，为和最小的两条下降路径
# 示例 2：
#
#
#
# 输入：matrix = [[-19,57],[-40,-5]]
# 输出：-59
# 解释：如图所示，为和最小的下降路径
#
#

class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        dp = [[0 for _ in range(len(matrix[0]))] for _ in range(len(matrix))]

        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if i == 0:
                    dp[i][j] = matrix[i][j]
                else:
                    m = math.inf
                    for k in range(j - 1, j + 2):
                        if 0 <= k < len(matrix[0]):
                            if dp[i - 1][k] < m:
                                m = dp[i - 1][k]
                    dp[i][j] = matrix[i][j] + m
        return min(dp[-1])


if __name__ == "__main__":
    matrix = [[-19,57],[-40,-5]]

    test = Solution().minFallingPathSum(matrix)
    print(test)
