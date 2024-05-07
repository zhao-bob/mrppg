# 2617. 网格图中最少访问的格子数
# 困难
# 相关标签
# 相关企业
# 提示
# 给你一个下标从 0 开始的 m x n 整数矩阵 grid 。你一开始的位置在 左上角 格子 (0, 0) 。
#
# 当你在格子 (i, j) 的时候，你可以移动到以下格子之一：
#
# 满足 j < k <= grid[i][j] + j 的格子 (i, k) （向右移动），或者
# 满足 i < k <= grid[i][j] + i 的格子 (k, j) （向下移动）。
# 请你返回到达 右下角 格子 (m - 1, n - 1) 需要经过的最少移动格子数，如果无法到达右下角格子，请你返回 -1 。
#
#
#
# 示例 1：
#
#
#
# 输入：grid = [[3,4,2,1],[4,2,3,1],[2,1,0,0],[2,4,0,0]]
# 输出：4
# 解释：上图展示了到达右下角格子经过的 4 个格子。
# 示例 2：
#
#
#
# 输入：grid = [[3,4,2,1],[4,2,1,1],[2,1,1,0],[3,4,1,0]]
# 输出：3
# 解释：上图展示了到达右下角格子经过的 3 个格子。
# 示例 3：
#
#
#
# 输入：grid = [[2,1,0],[1,0,0]]
# 输出：-1
# 解释：无法到达右下角格子。
#
#
# 提示：
#
# m == grid.length
# n == grid[i].length
# 1 <= m, n <= 105
# 1 <= m * n <= 105
# 0 <= grid[i][j] < m * n
# grid[m - 1][n - 1] == 0
#

import heapq
import math
from collections import Counter, deque, defaultdict
from datetime import date
from functools import cache
from typing import List, Optional

from sortedcontainers import SortedList


class Solution:
    def minimumVisitedCells(self, grid: List[List[int]]) -> int:
        # m = len(grid)
        # n = len(grid[0])
        # q = deque()
        # q.append((0, 0, 0, 0))
        # r = [[-1] * n for _ in range(m)]
        # r[0][0] = 1
        # while q:
        #     x, y, c, b = q.popleft()
        #     if x == m - 1 and y == n - 1:
        #         return r[x][y]
        #     for i in range(max(c + 1, x + 1), min(m, x + grid[x][y] + 1)):
        #         if r[i][y] == -1:
        #             q.append((i, y, max(grid[x][y], c), y))
        #             r[i][y] = r[x][y] + 1
        #     for i in range(max(b + 1, y + 1), min(n, y + grid[x][y] + 1)):
        #         if r[x][i] == -1:
        #             q.append((x, i, x, max(grid[x][y], b)))
        #             r[x][i] = r[x][y] + 1
        # return r[-1][-1]
        col_heaps = [[] for _ in grid[0]]  # 每一列的最小堆
        for i, row in enumerate(grid):
            row_h = []  # 第 i 行的最小堆
            for j, (g, col_h) in enumerate(zip(row, col_heaps)):
                while row_h and row_h[0][1] < j:  # 无法到达第 j 列
                    heapq.heappop(row_h)  # 弹出无用数据
                while col_h and col_h[0][1] < i:  # 无法到达第 i 行
                    heapq.heappop(col_h)  # 弹出无用数据
                f = math.inf if i or j else 1  # 起点算 1 个格子
                if row_h: f = row_h[0][0] + 1  # 从左边跳过来
                if col_h: f = min(f, col_h[0][0] + 1)  # 从上边跳过来
                if g and f < math.inf:
                    heapq.heappush(row_h, (f, g + j))  # 经过的格子数，向右最远能到达的列号
                    heapq.heappush(col_h, (f, g + i))  # 经过的格子数，向下最远能到达的行号
        return f if f < math.inf else -1  # 此时的 f 是在 (m-1, n-1) 处算出来的

if __name__ == "__main__":
    grid = [[6,1,3,0],[0,1,5,0]]
    test = Solution().minimumVisitedCells(grid)
    print(test)
