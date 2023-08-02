import heapq
import math
from collections import Counter, deque
from typing import List, Optional


# 面试题 16.19. 水域大小
# 你有一个用于表示一片土地的整数矩阵land，该矩阵中每个点的值代表对应地点的海拔高度。若值为0则表示水域。由垂直、水平或对角连接的水域为池塘。池塘的大小是指相连接的水域的个数。编写一个方法来计算矩阵中所有池塘的大小，返回值需要从小到大排序。
#
# 示例：
#
# 输入：
# [
#   [0,2,1,0],
#   [0,1,0,1],
#   [1,1,0,1],
#   [0,1,0,1]
# ]
# 输出： [1,2,4]
#

class Solution:
    def pondSizes(self, land: List[List[int]]) -> List[int]:
        def bfs(land, i, j, searched):
            q = [(i, j)]
            s = 0
            while len(q) > 0:
                p = q[0]
                q = q[1:]
                for k in range(p[0] - 1, p[0] + 2):
                    if 0 <= k < len(land):
                        for l in range(p[1] - 1, p[1] + 2):
                            if 0 <= l < len(land[0]):
                                if (k, l) not in searched:
                                    if land[k][l] == 0:
                                        s += 1
                                        if (k, l) != p:
                                            q.append((k, l))
                                    searched.add((k, l))
            return s

        res = []
        searched = set()
        for i in range(len(land)):
            for j in range(len(land[0])):
                if (i, j) not in searched and land[i][j] == 0:
                    res.append(bfs(land, i, j, searched))

        res.sort()
        return res


if __name__ == "__main__":
    land = [
        [0, 2, 1, 0],
        [0, 1, 0, 1],
        [1, 1, 0, 1],
        [0, 1, 0, 1]
    ]

    test = Solution().pondSizes(land)
    print(test)
