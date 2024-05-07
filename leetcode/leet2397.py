# 2397. 被列覆盖的最多行数
# 提示
# 中等
# 58
# 相关企业
# 给你一个下标从 0 开始、大小为 m x n 的二进制矩阵 matrix ；另给你一个整数 numSelect，表示你必须从 matrix 中选择的 不同 列的数量。
#
# 如果一行中所有的 1 都被你选中的列所覆盖，则认为这一行被 覆盖 了。
#
# 形式上，假设 s = {c1, c2, ...., cnumSelect} 是你选择的列的集合。对于矩阵中的某一行 row ，如果满足下述条件，则认为这一行被集合 s 覆盖：
#
# 对于满足 matrix[row][col] == 1 的每个单元格 matrix[row][col]（0 <= col <= n - 1），col 均存在于 s 中，或者
# row 中 不存在 值为 1 的单元格。
# 你需要从矩阵中选出 numSelect 个列，使集合覆盖的行数最大化。
#
# 返回一个整数，表示可以由 numSelect 列构成的集合 覆盖 的 最大行数 。
#
#
#
# 示例 1：
#
#
#
# 输入：matrix = [[0,0,0],[1,0,1],[0,1,1],[0,0,1]], numSelect = 2
# 输出：3
# 解释：
# 图示中显示了一种覆盖 3 行的可行办法。
# 选择 s = {0, 2} 。
# - 第 0 行被覆盖，因为其中没有出现 1 。
# - 第 1 行被覆盖，因为值为 1 的两列（即 0 和 2）均存在于 s 中。
# - 第 2 行未被覆盖，因为 matrix[2][1] == 1 但是 1 未存在于 s 中。
# - 第 3 行被覆盖，因为 matrix[2][2] == 1 且 2 存在于 s 中。
# 因此，可以覆盖 3 行。
# 另外 s = {1, 2} 也可以覆盖 3 行，但可以证明无法覆盖更多行。
# 示例 2：
#
#
#
# 输入：matrix = [[1],[0]], numSelect = 1
# 输出：2
# 解释：
# 选择唯一的一列，两行都被覆盖了，因为整个矩阵都被覆盖了。
# 所以我们返回 2 。
# 提示：
#
# m == matrix.length
# n == matrix[i].length
# 1 <= m, n <= 12
# matrix[i][j] 要么是 0 要么是 1
# 1 <= numSelect <= n
#

import heapq
import math
from collections import Counter
from datetime import date
from typing import List, Optional


class Solution:
    def maximumRows(self, matrix: List[List[int]], numSelect: int) -> int:
        m = len(matrix)
        n = len(matrix[0])
        d = [0] * m
        adj = {}
        res = 0
        for i in range(m):
            adj[i] = set()
            for j in range(n):
                if matrix[i][j] == 1:
                    adj[i].add(m + j)
                    d[i] += 1
                    if m + j in adj:
                        adj[m + j].add(i)
                    else:
                        adj[m + j] = {i}
        dp = [[0] * m for _ in range(2 ** n)]
        for i in range(m):
            dp[0][i] = d[i]
        for i in range(1, 2 ** n):
            if i.bit_count() <= numSelect:
                t = i
                least = 0
                mask = 1
                while t > 0:
                    if t % 2 == 1:
                        break
                    t //= 2
                    least += 1
                    mask = 1 + (mask << 1)
                for j in range(m):
                    if m + least in adj and j in adj[m + least]:
                        dp[i][j] = dp[i & ~mask][j] - 1
                    else:
                        dp[i][j] = dp[i & ~mask][j]
                if i.bit_count() == numSelect:
                    dr = 0
                    for j in range(m):
                        if dp[i][j] == 0:
                            dr += 1
                    res = max(res, dr)
        return res


if __name__ == "__main__":
    matrix = [[0,0,1],[1,0,1],[1,0,1],[0,0,1]]
    numSelect = 2

    test = Solution().maximumRows(matrix, numSelect)

    print(test)
