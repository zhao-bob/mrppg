import math
from typing import List
from functools import cache


# n 座城市，从 0 到 n-1 编号，其间共有 n-1 条路线。因此，要想在两座不同城市之间旅行只有唯一一条路线可供选择（路线网形成一颗树）。去年，交通运输部决定重新规划路线，以改变交通拥堵的状况。
#
# 路线用 connections 表示，其中 connections[i] = [a, b] 表示从城市 a 到 b 的一条有向路线。
#
# 今年，城市 0 将会举办一场大型比赛，很多游客都想前往城市 0 。
#
# 请你帮助重新规划路线方向，使每个城市都可以访问城市 0 。返回需要变更方向的最小路线数。
#
# 题目数据 保证 每个城市在重新规划路线方向后都能到达城市 0 。
#
#
#
# 示例 1：
#
#
#
# 输入：n = 6, connections = [[0,1],[1,3],[2,3],[4,0],[4,5]]
# 输出：3
# 解释：更改以红色显示的路线的方向，使每个城市都可以到达城市 0 。
# 示例 2：
#
#
#
# 输入：n = 5, connections = [[1,0],[1,2],[3,2],[3,4]]
# 输出：2
# 解释：更改以红色显示的路线的方向，使每个城市都可以到达城市 0 。
# 示例 3：
#
# 输入：n = 3, connections = [[1,0],[2,0]]
# 输出：0
#


class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        adj = [set() for _ in range(n)]
        out = [0] * n
        outadj = [set() for _ in range(n)]

        for c in connections:
            adj[c[0]].add(c[1])
            adj[c[1]].add(c[0])
            outadj[c[0]].add(c[1])
            out[c[0]] += 1

        searched = set()

        q = [0]
        res = 0
        while q:
            c = q[0]
            q = q[1:]
            searched.add(c)
            res += out[c]
            for ne in adj[c]:
                if ne not in searched:
                    if ne not in outadj[c]:
                        out[ne] -= 1
                    q.append(ne)
        return res





if __name__ == "__main__":
    n = 3
    connections = [[1,0],[2,0]]

    test = Solution().minReorder(n, connections)
    print(test)
