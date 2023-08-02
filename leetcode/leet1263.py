import math
from collections import deque
from itertools import pairwise
from typing import List


# 1263. 推箱子
# 「推箱子」是一款风靡全球的益智小游戏，玩家需要将箱子推到仓库中的目标位置。
#
# 游戏地图用大小为 m x n 的网格 grid 表示，其中每个元素可以是墙、地板或者是箱子。
#
# 现在你将作为玩家参与游戏，按规则将箱子 'B' 移动到目标位置 'T' ：
#
# 玩家用字符 'S' 表示，只要他在地板上，就可以在网格中向上、下、左、右四个方向移动。
# 地板用字符 '.' 表示，意味着可以自由行走。
# 墙用字符 '#' 表示，意味着障碍物，不能通行。
# 箱子仅有一个，用字符 'B' 表示。相应地，网格上有一个目标位置 'T'。
# 玩家需要站在箱子旁边，然后沿着箱子的方向进行移动，此时箱子会被移动到相邻的地板单元格。记作一次「推动」。
# 玩家无法越过箱子。
# 返回将箱子推到目标位置的最小 推动 次数，如果无法做到，请返回 -1。
#
#
#
# 示例 1：
#
#
#
# 输入：grid = [["#","#","#","#","#","#"],
#              ["#","T","#","#","#","#"],
#              ["#",".",".","B",".","#"],
#              ["#",".","#","#",".","#"],
#              ["#",".",".",".","S","#"],
#              ["#","#","#","#","#","#"]]
# 输出：3
# 解释：我们只需要返回推箱子的次数。
# 示例 2：
#
# 输入：grid = [["#","#","#","#","#","#"],
#              ["#","T","#","#","#","#"],
#              ["#",".",".","B",".","#"],
#              ["#","#","#","#",".","#"],
#              ["#",".",".",".","S","#"],
#              ["#","#","#","#","#","#"]]
# 输出：-1
# 示例 3：
#
# 输入：grid = [["#","#","#","#","#","#"],
#              ["#","T",".",".","#","#"],
#              ["#",".","#","B",".","#"],
#              ["#",".",".",".",".","#"],
#              ["#",".",".",".","S","#"],
#              ["#","#","#","#","#","#"]]
# 输出：5
# 解释：向下、向左、向左、向上再向上。
#

class Solution:
    def minPushBox(self, grid: List[List[str]]) -> int:
        def f(i: int, j: int) -> int:
            return i * n + j

        def check(i: int, j: int) -> bool:
            return 0 <= i < m and 0 <= j < n and grid[i][j] != "#"

        for i, row in enumerate(grid):
            for j, c in enumerate(row):
                if c == "S":
                    si, sj = i, j
                elif c == "B":
                    bi, bj = i, j
        m, n = len(grid), len(grid[0])
        dirs = (-1, 0, 1, 0, -1)
        q = deque([(f(si, sj), f(bi, bj), 0)])
        vis = [[False] * (m * n) for _ in range(m * n)]
        vis[f(si, sj)][f(bi, bj)] = True
        while q:
            s, b, d = q.popleft()
            bi, bj = b // n, b % n
            if grid[bi][bj] == "T":
                return d
            si, sj = s // n, s % n
            for a, b in pairwise(dirs):
                sx, sy = si + a, sj + b
                if not check(sx, sy):
                    continue
                if sx == bi and sy == bj:
                    bx, by = bi + a, bj + b
                    if not check(bx, by) or vis[f(sx, sy)][f(bx, by)]:
                        continue
                    vis[f(sx, sy)][f(bx, by)] = True
                    q.append((f(sx, sy), f(bx, by), d + 1))
                elif not vis[f(sx, sy)][f(bi, bj)]:
                    vis[f(sx, sy)][f(bi, bj)] = True
                    q.appendleft((f(sx, sy), f(bi, bj), d))
        return -1


if __name__ == "__main__":
    grid = [["#", "#", "#", "#", "#", "#"],
            ["#", "T", "#", "#", "#", "#"],
            ["#", ".", ".", "B", ".", "#"],
            ["#", ".", "#", "#", ".", "#"],
            ["#", ".", ".", ".", "S", "#"],
            ["#", "#", "#", "#", "#", "#"]]

    test = Solution().minPushBox(grid)
    print(test)
