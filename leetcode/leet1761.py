import collections
import heapq
import math
from bisect import bisect_right
from collections import Counter, deque
from functools import cache
from itertools import product
from typing import List, Optional


# 1761. 一个图中连通三元组的最小度数
# 困难
# 给你一个无向图，整数 n 表示图中节点的数目，edges 数组表示图中的边，其中 edges[i] = [ui, vi] ，表示 ui 和 vi 之间有一条无向边。
#
# 一个 连通三元组 指的是 三个 节点组成的集合且这三个点之间 两两 有边。
#
# 连通三元组的度数 是所有满足此条件的边的数目：一个顶点在这个三元组内，而另一个顶点不在这个三元组内。
#
# 请你返回所有连通三元组中度数的 最小值 ，如果图中没有连通三元组，那么返回 -1 。
#
#
#
# 示例 1：
#
#
# 输入：n = 6, edges = [[1,2],[1,3],[3,2],[4,1],[5,2],[3,6]]
# 输出：3
# 解释：只有一个三元组 [1,2,3] 。构成度数的边在上图中已被加粗。
# 示例 2：
#
#
# 输入：n = 7, edges = [[1,3],[4,1],[4,3],[2,5],[5,6],[6,7],[7,5],[2,6]]
# 输出：0
# 解释：有 3 个三元组：
# 1) [1,4,3]，度数为 0 。
# 2) [2,5,6]，度数为 2 。
# 3) [5,6,7]，度数为 2 。

class Solution:
    def minTrioDegree(self, n: int, edges: List[List[int]]) -> int:
        d = [0] * n
        adj = {}

        for e in edges:
            if e[0] in adj:
                adj[e[0]].add(e[1])
            else:
                adj[e[0]] = {e[1]}
            if e[1] in adj:
                adj[e[1]].add(e[0])
            else:
                adj[e[1]] = {e[0]}
            d[e[0] - 1] += 1
            d[e[1] - 1] += 1
        ds = [[d[i], i] for i in range(n)]
        ds.sort(key=lambda x: x[0])

        # for x in ds:
        #     if x[0] >= 2:
        #
        #         g = [[0] * n for _ in range(n)]
        #         degree = [0] * n
        #
        #         for x, y in edges:
        #             x, y = x - 1, y - 1
        #             g[x][y] = g[y][x] = 1
        #             degree[x] += 1
        #             degree[y] += 1
        #
        #         ans = math.inf
        #         for i in range(n):
        #             for j in range(i + 1, n):
        #                 if g[i][j] == 1:
        #                     for k in range(j + 1, n):
        #                         if g[i][k] == g[j][k] == 1:
        #                             ans = min(ans, degree[i] + degree[j] + degree[k] - 6)
        #
        #         return -1 if ans == math.inf else ans




if __name__ == "__main__":
    n = 6
    edges = [[1,2],[1,3],[3,2],[4,1],[5,2],[3,6]]

    test = Solution().minTrioDegree(n, edges)

    print(test)
