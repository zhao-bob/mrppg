import collections
import heapq
import math
from bisect import bisect_right
from collections import Counter, deque
from functools import cache
from itertools import product
from typing import List, Optional


# 1267. 统计参与通信的服务器
# 中等
# 这里有一幅服务器分布图，服务器的位置标识在 m * n 的整数矩阵网格 grid 中，1 表示单元格上有服务器，0 表示没有。
#
# 如果两台服务器位于同一行或者同一列，我们就认为它们之间可以进行通信。
#
# 请你统计并返回能够与至少一台其他服务器进行通信的服务器的数量。
#
#
#
# 示例 1：
#
#
#
# 输入：grid = [[1,0],[0,1]]
# 输出：0
# 解释：没有一台服务器能与其他服务器进行通信。
# 示例 2：
#
#
#
# 输入：grid = [[1,0],[1,1]]
# 输出：3
# 解释：所有这些服务器都至少可以与一台别的服务器进行通信。
# 示例 3：
#
#
#
# 输入：grid = [[1,1,0,0],[0,0,1,0],[0,0,1,0],[0,0,0,1]]
# 输出：4
# 解释：第一行的两台服务器互相通信，第三列的两台服务器互相通信，但右下角的服务器无法与其他服务器通信。

class Solution:
    def countServers(self, grid: List[List[int]]) -> int:
        c = []
        res = set()
        for i in range(len(grid)):
            fo = -1
            oo = False
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    if fo == -1:
                        fo = j
                        oo = True
                    else:
                        if oo:
                            res.add((i, fo))
                            oo = False
                        res.add((i, j))
            if oo:
                c.append((i, fo))

        for i in c:
            oo = True
            for j in range(len(grid)):
                if grid[j][i[1]] == 1 and j != i[0]:
                    if oo:
                        res.add(i)
                        oo = False
                    if (j, i[1]) not in res:
                        res.add((j, i[1]))
        return len(res)




if __name__ == "__main__":
    grid = [[1,1,0,0],[0,0,1,0],[0,0,1,0],[0,0,0,1]]

    test = Solution().countServers(grid)

    print(test)
