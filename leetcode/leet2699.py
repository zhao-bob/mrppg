import heapq
import math
from collections import Counter
from typing import List, Optional


# 2699. 修改图中的边权
# 给你一个 n 个节点的 无向带权连通 图，节点编号为 0 到 n - 1 ，再给你一个整数数组 edges ，其中 edges[i] = [ai, bi, wi] 表示节点 ai 和 bi 之间有一条边权为 wi 的边。
#
# 部分边的边权为 -1（wi = -1），其他边的边权都为 正 数（wi > 0）。
#
# 你需要将所有边权为 -1 的边都修改为范围 [1, 2 * 109] 中的 正整数 ，使得从节点 source 到节点 destination 的 最短距离 为整数 target 。如果有 多种 修改方案可以使 source 和 destination 之间的最短距离等于 target ，你可以返回任意一种方案。
#
# 如果存在使 source 到 destination 最短距离为 target 的方案，请你按任意顺序返回包含所有边的数组（包括未修改边权的边）。如果不存在这样的方案，请你返回一个 空数组 。
#
# 注意：你不能修改一开始边权为正数的边。
#
#
#
# 示例 1：
#
#
#
# 输入：n = 5, edges = [[4,1,-1],[2,0,-1],[0,3,-1],[4,3,-1]], source = 0, destination = 1, target = 5
# 输出：[[4,1,1],[2,0,1],[0,3,3],[4,3,1]]
# 解释：上图展示了一个满足题意的修改方案，从 0 到 1 的最短距离为 5 。
# 示例 2：
#
#
#
# 输入：n = 3, edges = [[0,1,-1],[0,2,5]], source = 0, destination = 2, target = 6
# 输出：[]
# 解释：上图是一开始的图。没有办法通过修改边权为 -1 的边，使得 0 到 2 的最短距离等于 6 ，所以返回一个空数组。
# 示例 3：
#
#
#
# 输入：n = 4, edges = [[1,0,4],[1,2,3],[2,3,5],[0,3,-1]], source = 0, destination = 2, target = 6
# 输出：[[1,0,4],[1,2,3],[2,3,5],[0,3,1]]
# 解释：上图展示了一个满足题意的修改方案，从 0 到 2 的最短距离为 6 。
#

class Solution:
    # def modifiedGraphEdges(self, n: int, edges: List[List[int]], source: int, destination: int, target: int) -> List[List[int]]:
    #     adj = [set() for _ in range(n)]
    #     minimal = [[] for _ in range(n)]
    #
    #     for i in range(len(edges)):
    #         adj[edges[i][0]].add((edges[i][1], edges[i][2]))
    #         adj[edges[i][1]].add((edges[i][0], edges[i][2]))
    #
    #     searched = {}
    #     self.minimal_path(minimal, source, destination, adj, searched)
    #
    #     rn = minimal[destination]
    #
    #     if searched[rn[1]] > target or (searched[rn[1]] < target and rn[4] == 0):
    #         return []
    #     else:
    #         cp = target - searched[rn[1]]
    #         es = {}
    #         c = 0
    #         for i in range(1, len(rn[3])):
    #             es[(rn[3][i], rn[3][i - 1])] = 0
    #             es[(rn[3][i - 1], rn[3][i])] = 0
    #             for x in adj[rn[3][i - 1]]:
    #                 if x[0] == rn[3][i] and x[1] == -1:
    #                     c += 1
    #                     es[(rn[3][i], rn[3][i - 1])] = c
    #                     es[(rn[3][i-1], rn[3][i])] = c
    #
    #         adj = [set() for _ in range(n)]
    #         for x in edges:
    #             if x[2] == -1:
    #                 if (x[0], x[1]) in es:
    #                     if es[(x[0], x[1])] != rn[4]:
    #                         x[2] = 1
    #                     else:
    #                         x[2] = 1 + cp
    #                 else:
    #                     x[2] = target
    #             adj[x[0]].add((x[1], x[2]))
    #             adj[x[1]].add((x[0], x[2]))
    #     minimal = [[] for _ in range(n)]
    #     searched = {}
    #     self.minimal_path(minimal, source, destination, adj, searched)
    #     rn = minimal[destination]
    #     if searched[rn[1]] != target:
    #         return []
    #     return edges
    #
    # def minimal_path(self, minimal, source, destination, adj, searched):
    #     heap = [(0, source, -1, [], 0)]
    #     heapq.heapify(heap)
    #
    #     while len(heap) > 0:
    #         node = heapq.heappop(heap)
    #         if node[1] not in searched:
    #             searched[node[1]] = node[0]
    #             # if node[2] == -1:
    #             #     searched[node[1]] = 0
    #             # else:
    #             #     if node[0] == -1:
    #             #         searched[node[1]] = searched[node[2]] + 1
    #             #         n1 += 1
    #             #     else:
    #             #         searched[node[1]] = searched[node[2]] + node[0]
    #             node[3].append(node[1])
    #             minimal[node[1]] = node
    #             neighbor = adj[node[1]]
    #             for x in neighbor:
    #                 if x[0] not in searched:
    #                     mp = math.inf
    #                     mn = -1
    #                     mc = math.inf
    #                     for y in adj[x[0]]:
    #                         if y[0] in searched:
    #                             if y[1] == -1:
    #                                 a = 1 + searched[y[0]]
    #                             else:
    #                                 a = y[1] + searched[y[0]]
    #                             if a < mp:
    #                                 mp = a
    #                                 mn = y[0]
    #                                 mc = y[1]
    #                     n1 = minimal[mn][4]
    #                     if mc == -1:
    #                        n1 += 1
    #                     l = minimal[mn][3].copy()
    #                     heapq.heappush(heap, (mp, x[0], mn, l, n1))
    #         if node[1] == destination:
    #             break
    def modifiedGraphEdges(self, n: int, edges: List[List[int]], source: int, destination: int, target: int) -> List[
        List[int]]:
        def dijkstra(op: int, source: int, adj_matrix: List[List[int]]) -> List[int]:
            # 朴素的 dijkstra 算法
            # adj_matrix 是一个邻接矩阵
            dist = [math.inf] * n
            used = set()
            dist[source] = 0

            for round in range(n - 1):
                u = -1
                for i in range(n):
                    if i not in used and (u == -1 or dist[i] < dist[u]):
                        u = i
                used.add(u)
                for v in range(n):
                    if v not in used and adj_matrix[u][v] != -1:
                        if edges[adj_matrix[u][v]][2] != -1:
                            dist[v] = min(dist[v], dist[u] + edges[adj_matrix[u][v]][2])
                        else:
                            if op == 0:
                                dist[v] = min(dist[v], dist[u] + 1)
                            else:
                                modify = target - dist[u] - from_destination[v]
                                if modify > 0:
                                    dist[v] = min(dist[v], dist[u] + modify)
                                    edges[adj_matrix[u][v]][2] = modify
                                else:
                                    edges[adj_matrix[u][v]][2] = target
            return dist

        adj_matrix = [[-1] * n for _ in range(n)]
        # 邻接矩阵中存储边的下标
        for i, (u, v, w) in enumerate(edges):
            adj_matrix[u][v] = adj_matrix[v][u] = i

        from_destination = dijkstra(0, destination, adj_matrix)
        if from_destination[source] > target:
            return []
        from_source = dijkstra(1, source, adj_matrix)
        if from_source[destination] != target:
            return []
        return edges






if __name__ == "__main__":
    n = 4
    edges = [[0,1,-1],[2,0,2],[3,2,6],[2,1,10],[3,0,-1]]
    source = 1
    destination = 3
    target = 12

    test = Solution().modifiedGraphEdges(n, edges, source, destination, target)
    print(test)
