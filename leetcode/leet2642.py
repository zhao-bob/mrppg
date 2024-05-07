# 2642. 设计可以求最短路径的图类
# 困难
# 相关标签
# 相关企业
# 提示
# 给你一个有 n 个节点的 有向带权 图，节点编号为 0 到 n - 1 。图中的初始边用数组 edges 表示，其中 edges[i] = [fromi, toi, edgeCosti] 表示从 fromi 到 toi 有一条代价为 edgeCosti 的边。
#
# 请你实现一个 Graph 类：
#
# Graph(int n, int[][] edges) 初始化图有 n 个节点，并输入初始边。
# addEdge(int[] edge) 向边集中添加一条边，其中 edge = [from, to, edgeCost] 。数据保证添加这条边之前对应的两个节点之间没有有向边。
# int shortestPath(int node1, int node2) 返回从节点 node1 到 node2 的路径 最小 代价。如果路径不存在，返回 -1 。一条路径的代价是路径中所有边代价之和。
#
#
# 示例 1：
#
#
#
# 输入：
# ["Graph", "shortestPath", "shortestPath", "addEdge", "shortestPath"]
# [[4, [[0, 2, 5], [0, 1, 2], [1, 2, 1], [3, 0, 3]]], [3, 2], [0, 3], [[1, 3, 4]], [0, 3]]
# 输出：
# [null, 6, -1, null, 6]
#
# 解释：
# Graph g = new Graph(4, [[0, 2, 5], [0, 1, 2], [1, 2, 1], [3, 0, 3]]);
# g.shortestPath(3, 2); // 返回 6 。从 3 到 2 的最短路径如第一幅图所示：3 -> 0 -> 1 -> 2 ，总代价为 3 + 2 + 1 = 6 。
# g.shortestPath(0, 3); // 返回 -1 。没有从 0 到 3 的路径。
# g.addEdge([1, 3, 4]); // 添加一条节点 1 到节点 3 的边，得到第二幅图。
# g.shortestPath(0, 3); // 返回 6 。从 0 到 3 的最短路径为 0 -> 1 -> 3 ，总代价为 2 + 4 = 6 。
#
#
# 提示：
#
# 1 <= n <= 100
# 0 <= edges.length <= n * (n - 1)
# edges[i].length == edge.length == 3
# 0 <= fromi, toi, from, to, node1, node2 <= n - 1
# 1 <= edgeCosti, edgeCost <= 106
# 图中任何时候都不会有重边和自环。
# 调用 addEdge 至多 100 次。
# 调用 shortestPath 至多 100 次。
#

import heapq
import math
from collections import Counter, deque, defaultdict
from datetime import date
from functools import cache
from typing import List, Optional

from sortedcontainers import SortedList


class Graph:

    def __init__(self, n: int, edges: List[List[int]]):
        self.n = n
        self.adj = [[0] * n for _ in range(n)]

        for e in edges:
            self.adj[e[0]][e[1]] = e[2]

    def addEdge(self, edge: List[int]) -> None:
        self.adj[edge[0]][edge[1]] = edge[2]

    def shortestPath(self, node1: int, node2: int) -> int:
        d = [math.inf] * self.n
        h = [(0, node1)]

        d[node1] = 0

        while h:
            a = heapq.heappop(h)
            if a[1] == node2:
                return a[0]
            for i in range(self.n):
                if self.adj[a[1]][i] != 0 and d[a[1]] + self.adj[a[1]][i] < d[i]:
                    d[i] = d[a[1]] + self.adj[a[1]][i]
                    heapq.heappush(h, (d[i], i))

        return -1 if d[node2] == math.inf else d[node2]


# Your Graph object will be instantiated and called as such:
# obj = Graph(n, edges)
# obj.addEdge(edge)
# param_2 = obj.shortestPath(node1,node2)


if __name__ == "__main__":
    ops = ["Graph","shortestPath","shortestPath","addEdge","shortestPath"]
    par = [[4,[[0,2,5],[0,1,2],[1,2,1],[3,0,3]]],[3,2],[0,3],[[1,3,4]],[0,3]]
    graph = Graph(par[0][0], par[0][1])
    res = []
    for i in range(1, len(par)):
        if ops[i] == "shortestPath":
            res.append(graph.shortestPath(par[i][0], par[i][1]))
        if ops[i] == "addEdge":
            res.append(graph.addEdge(par[i][0]))
    print(res)
