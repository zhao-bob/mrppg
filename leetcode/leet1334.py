import heapq
import math
from collections import Counter, deque, defaultdict
from functools import cache, reduce
from itertools import product
from typing import List, Optional


# 1334. 阈值距离内邻居最少的城市
# 提示
# 中等
# 122
# 相关企业
# 有 n 个城市，按从 0 到 n-1 编号。给你一个边数组 edges，其中 edges[i] = [fromi, toi, weighti] 代表 fromi 和 toi 两个城市之间的双向加权边，距离阈值是一个整数 distanceThreshold。
#
# 返回能通过某些路径到达其他城市数目最少、且路径距离 最大 为 distanceThreshold 的城市。如果有多个这样的城市，则返回编号最大的城市。
#
# 注意，连接城市 i 和 j 的路径的距离等于沿该路径的所有边的权重之和。
#
#
#
# 示例 1：
#
#
#
# 输入：n = 4, edges = [[0,1,3],[1,2,1],[1,3,4],[2,3,1]], distanceThreshold = 4
# 输出：3
# 解释：城市分布图如上。
# 每个城市阈值距离 distanceThreshold = 4 内的邻居城市分别是：
# 城市 0 -> [城市 1, 城市 2]
# 城市 1 -> [城市 0, 城市 2, 城市 3]
# 城市 2 -> [城市 0, 城市 1, 城市 3]
# 城市 3 -> [城市 1, 城市 2]
# 城市 0 和 3 在阈值距离 4 以内都有 2 个邻居城市，但是我们必须返回城市 3，因为它的编号最大。
# 示例 2：
#
#
#
# 输入：n = 5, edges = [[0,1,2],[0,4,8],[1,2,3],[1,4,2],[2,3,1],[3,4,1]], distanceThreshold = 2
# 输出：0
# 解释：城市分布图如上。
# 每个城市阈值距离 distanceThreshold = 2 内的邻居城市分别是：
# 城市 0 -> [城市 1]
# 城市 1 -> [城市 0, 城市 4]
# 城市 2 -> [城市 3, 城市 4]
# 城市 3 -> [城市 2, 城市 4]
# 城市 4 -> [城市 1, 城市 2, 城市 3]
# 城市 0 在阈值距离 2 以内只有 1 个邻居城市。
#
#
class Solution:
    def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:
        adj = [[math.inf for _ in range(n)] for _ in range(n)]
        for e in edges:
            if e[2] <= distanceThreshold:
                adj[e[0]][e[1]] = e[2]
                adj[e[1]][e[0]] = e[2]

        def shortestPath(s):
            p = [math.inf for _ in range(n)]
            p[s] = 0
            ns = set()
            searched = set()
            for i in range(n):
                m = math.inf
                c = -1
                for k in range(n):
                    if p[k] != math.inf and p[k] < m and k not in searched:
                        m = p[k]
                        c = k
                searched.add(c)
                for j in range(n):
                    if j != c and j not in searched:
                        p[j] = min(p[j], p[c] + adj[c][j])
                        if p[j] <= distanceThreshold:
                            ns.add(j)
            return len(ns)

        l = math.inf
        res = -1
        for i in range(n):
            count = 0
            # for j in range(n):
            #     if adj[i][j] != math.inf:
            #         count += 1
            #         break
            # if count > 0:
            a = shortestPath(i)
            if a <= l:
                l = a
                res = i
        return res


if __name__ == "__main__":
    n = 5
    edges = [[0,1,2],[0,4,8],[1,2,3],[1,4,2],[2,3,1],[3,4,1]]
    distanceThreshold = 5

    test = Solution().findTheCity(n, edges, distanceThreshold)

    print(test)
