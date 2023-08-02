import heapq
import math
from collections import Counter
from typing import List, Optional


# 1254. 统计封闭岛屿的数目
# 二维矩阵 grid 由 0 （土地）和 1 （水）组成。岛是由最大的4个方向连通的 0 组成的群，封闭岛是一个 完全 由1包围（左、上、右、下）的岛。
#
# 请返回 封闭岛屿 的数目。
#
#
#
# 示例 1：
#
#
#
# 输入：grid = [[1,1,1,1,1,1,1,0],[1,0,0,0,0,1,1,0],[1,0,1,0,1,1,1,0],[1,0,0,0,0,1,0,1],[1,1,1,1,1,1,1,0]]
# 输出：2
# 解释：
# 灰色区域的岛屿是封闭岛屿，因为这座岛屿完全被水域包围（即被 1 区域包围）。
# 示例 2：
#
#
#
# 输入：grid = [[0,0,1,0,0],[0,1,0,1,0],[0,1,1,1,0]]
# 输出：1
# 示例 3：
#
# 输入：grid = [[1,1,1,1,1,1,1],
#              [1,0,0,0,0,0,1],
#              [1,0,1,1,1,0,1],
#              [1,0,1,0,1,0,1],
#              [1,0,1,1,1,0,1],
#              [1,0,0,0,0,0,1],
#              [1,1,1,1,1,1,1]]
# 输出：2
#

class Solution:
    def closedIsland(self, grid: List[List[int]]) -> int:
        def dfs(grid, i, j, searched):
            u = 1
            l = 1
            d = 1
            r = 1
            searched.add((i, j))
            if grid[i - 1][j] == 0 and (i - 1, j) not in searched:
                if i - 1 == 0:
                    u = 0
                else:
                    u = dfs(grid, i - 1, j, searched)
            if grid[i][j - 1] == 0 and (i, j - 1) not in searched:
                if j - 1 == 0:
                    l = 0
                else:
                    l = dfs(grid, i, j - 1, searched)
            if grid[i + 1][j] == 0 and (i + 1, j) not in searched:
                if i + 1 == len(grid) - 1:
                    d = 0
                else:
                    d = dfs(grid, i + 1, j, searched)
            if grid[i][j + 1] == 0 and (i, j + 1) not in searched:
                if j + 1 == len(grid[0]) - 1:
                    r = 0
                else:
                    r = dfs(grid, i, j + 1, searched)
            if u * l * d * r == 1:
                return 1
            else:
                return 0

        if len(grid) < 3 or len(grid[0]) < 3:
            return 0
        searched = set()
        res = 0
        for i in range(1, len(grid) - 1):
            for j in range(1, len(grid[0]) - 1):
                if grid[i][j] == 0 and (i, j) not in searched:
                    if grid[i - 1][j] == 1 and grid[i][j - 1] == 1:
                        res += dfs(grid, i, j, searched)
        return res


if __name__ == "__main__":
    grid = [[0,0,1,0,0],[0,1,0,1,0],[0,1,1,1,0]]

    test = Solution().closedIsland(grid)
    print(test)
