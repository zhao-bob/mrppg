import heapq
import math
from collections import Counter, deque, defaultdict
from functools import cache, reduce
from itertools import product
from typing import List, Optional


# 2258. 逃离火灾
# 提示
# 困难
# 62
# 相关企业
# 给你一个下标从 0 开始大小为 m x n 的二维整数数组 grid ，它表示一个网格图。每个格子为下面 3 个值之一：
#
# 0 表示草地。
# 1 表示着火的格子。
# 2 表示一座墙，你跟火都不能通过这个格子。
# 一开始你在最左上角的格子 (0, 0) ，你想要到达最右下角的安全屋格子 (m - 1, n - 1) 。每一分钟，你可以移动到 相邻 的草地格子。每次你移动 之后 ，着火的格子会扩散到所有不是墙的 相邻 格子。
#
# 请你返回你在初始位置可以停留的 最多 分钟数，且停留完这段时间后你还能安全到达安全屋。如果无法实现，请你返回 -1 。如果不管你在初始位置停留多久，你 总是 能到达安全屋，请你返回 109 。
#
# 注意，如果你到达安全屋后，火马上到了安全屋，这视为你能够安全到达安全屋。
#
# 如果两个格子有共同边，那么它们为 相邻 格子。
#
#
#
# 示例 1：
#
#
#
# 输入：grid = [[0,2,0,0,0,0,0],[0,0,0,2,2,1,0],[0,2,0,0,1,2,0],[0,0,2,2,2,0,2],[0,0,0,0,0,0,0]]
# 输出：3
# 解释：上图展示了你在初始位置停留 3 分钟后的情形。
# 你仍然可以安全到达安全屋。
# 停留超过 3 分钟会让你无法安全到达安全屋。
# 示例 2：
#
#
#
# 输入：grid = [[0,0,0,0],[0,1,2,0],[0,2,0,0]]
# 输出：-1
# 解释：上图展示了你马上开始朝安全屋移动的情形。
# 火会蔓延到你可以移动的所有格子，所以无法安全到达安全屋。
# 所以返回 -1 。
# 示例 3：
#
#
#
# 输入：grid = [[0,0,0],[2,2,0],[1,2,0]]
# 输出：1000000000
# 解释：上图展示了初始网格图。
# 注意，由于火被墙围了起来，所以无论如何你都能安全到达安全屋。
# 所以返回 109 。
#
#

class Solution:
    def maximumMinutes(self, grid: List[List[int]]) -> int:
        w = len(grid[0])
        h = len(grid)
        fireTime = [[math.inf for _ in range(w)] for _ in range(h)]

        q = []
        for i in range(h):
            for j in range(w):
                if grid[i][j] == 1:
                    q.append((i, j))
                    fireTime[i][j] = 0
        searched = set()
        while q:
            n = q[0]
            q = q[1:]
            searched.add(n)
            t = fireTime[n[0]][n[1]]
            for i in [-1, 1]:
                if 0 <= n[0] + i < h and (n[0] + i, n[1]) not in searched:
                    if grid[n[0] + i][n[1]] == 0:
                        q.append((n[0] + i, n[1]))
                        fireTime[n[0] + i][n[1]] = t + 1
                    else:
                        if grid[n[0] + i][n[1]] == 2:
                            searched.add((n[0] + i, n[1]))
                if 0 <= n[1] + i < w and (n[0], n[1] + i) not in searched:
                    if grid[n[0]][n[1] + i] == 0:
                        q.append((n[0], n[1] + i))
                        fireTime[n[0]][n[1] + i] = t + 1
                    else:
                        if grid[n[0]][n[1] + i] == 2:
                            searched.add((n[0], n[1] + i))

        def bfs(s, d, st):
            q = [s]
            searched = {(s[0], s[1])}
            while q:
                n = q[0]
                q = q[1:]
                dist = n[2]
                for i in [-1, 1]:
                    if 0 <= n[0] + i < h and (n[0] + i, n[1]) not in searched:
                        if grid[n[0] + i][n[1]] == 0 and dist + 1 <= fireTime[n[0] + i][n[1]] - st:
                            if n[0] + i == d[0] and n[1] == d[1]:
                                return dist + 1
                            elif dist + 1 < fireTime[n[0] + i][n[1]] - st:
                                q.append((n[0] + i, n[1], dist + 1))
                        searched.add((n[0] + i, n[1]))
                    if 0 <= n[1] + i < w and (n[0], n[1] + i) not in searched:
                        if grid[n[0]][n[1] + i] == 0 and dist + 1 <= fireTime[n[0]][n[1] + i] - st:
                            if n[0] == d[0] and n[1] + i == d[1]:
                                return dist + 1
                            elif dist + 1 < fireTime[n[0]][n[1] + i] - st:
                                q.append((n[0], n[1] + i, dist + 1))
                        searched.add((n[0], n[1] + i))
            return math.inf

        nf = fireTime[0][0]
        nf1 = fireTime[-1][-1]
        dist = bfs((0, 0, 0), (h - 1, w - 1), 0)
        if dist == math.inf:
            return -1
        if nf == math.inf:
            return 10 ** 9
        if dist > nf1:
            return -1
        if dist == nf1:
            return 0
        if bfs((0, 0, 0), (h - 1, w - 1), nf1 - dist) != math.inf:
            return nf1 - dist
        else:
            return nf1 - dist - 1


if __name__ == "__main__":
    grid = [[0,2],[2,0]]
    test = Solution().maximumMinutes(grid)
    print(test)
