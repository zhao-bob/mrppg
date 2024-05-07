# 2846. 边权重均等查询
# 困难
# 相关标签
# 相关企业
# 提示
# 现有一棵由 n 个节点组成的无向树，节点按从 0 到 n - 1 编号。给你一个整数 n 和一个长度为 n - 1 的二维整数数组 edges ，其中 edges[i] = [ui, vi, wi] 表示树中存在一条位于节点 ui 和节点 vi 之间、权重为 wi 的边。
#
# 另给你一个长度为 m 的二维整数数组 queries ，其中 queries[i] = [ai, bi] 。对于每条查询，请你找出使从 ai 到 bi 路径上每条边的权重相等所需的 最小操作次数 。在一次操作中，你可以选择树上的任意一条边，并将其权重更改为任意值。
#
# 注意：
#
# 查询之间 相互独立 的，这意味着每条新的查询时，树都会回到 初始状态 。
# 从 ai 到 bi的路径是一个由 不同 节点组成的序列，从节点 ai 开始，到节点 bi 结束，且序列中相邻的两个节点在树中共享一条边。
# 返回一个长度为 m 的数组 answer ，其中 answer[i] 是第 i 条查询的答案。
#
#
#
# 示例 1：
#
#
# 输入：n = 7, edges = [[0,1,1],[1,2,1],[2,3,1],[3,4,2],[4,5,2],[5,6,2]], queries = [[0,3],[3,6],[2,6],[0,6]]
# 输出：[0,0,1,3]
# 解释：第 1 条查询，从节点 0 到节点 3 的路径中的所有边的权重都是 1 。因此，答案为 0 。
# 第 2 条查询，从节点 3 到节点 6 的路径中的所有边的权重都是 2 。因此，答案为 0 。
# 第 3 条查询，将边 [2,3] 的权重变更为 2 。在这次操作之后，从节点 2 到节点 6 的路径中的所有边的权重都是 2 。因此，答案为 1 。
# 第 4 条查询，将边 [0,1]、[1,2]、[2,3] 的权重变更为 2 。在这次操作之后，从节点 0 到节点 6 的路径中的所有边的权重都是 2 。因此，答案为 3 。
# 对于每条查询 queries[i] ，可以证明 answer[i] 是使从 ai 到 bi 的路径中的所有边的权重相等的最小操作次数。
# 示例 2：
#
#
# 输入：n = 8, edges = [[1,2,6],[1,3,4],[2,4,6],[2,5,3],[3,6,6],[3,0,8],[7,0,2]], queries = [[4,6],[0,4],[6,5],[7,4]]
# 输出：[1,2,2,3]
# 解释：第 1 条查询，将边 [1,3] 的权重变更为 6 。在这次操作之后，从节点 4 到节点 6 的路径中的所有边的权重都是 6 。因此，答案为 1 。
# 第 2 条查询，将边 [0,3]、[3,1] 的权重变更为 6 。在这次操作之后，从节点 0 到节点 4 的路径中的所有边的权重都是 6 。因此，答案为 2 。
# 第 3 条查询，将边 [1,3]、[5,2] 的权重变更为 6 。在这次操作之后，从节点 6 到节点 5 的路径中的所有边的权重都是 6 。因此，答案为 2 。
# 第 4 条查询，将边 [0,7]、[0,3]、[1,3] 的权重变更为 6 。在这次操作之后，从节点 7 到节点 4 的路径中的所有边的权重都是 6 。因此，答案为 3 。
# 对于每条查询 queries[i] ，可以证明 answer[i] 是使从 ai 到 bi 的路径中的所有边的权重相等的最小操作次数。
#
#
# 提示：
#
# 1 <= n <= 104
# edges.length == n - 1
# edges[i].length == 3
# 0 <= ui, vi < n
# 1 <= wi <= 26
# 生成的输入满足 edges 表示一棵有效的树
# 1 <= queries.length == m <= 2 * 104
# queries[i].length == 2
# 0 <= ai, bi < n
#

import heapq
import math
from collections import Counter
from datetime import date
from typing import List, Optional


class Solution:
    def find(self, uf: List[int], i: int) -> int:
        if uf[i] == i:
            return i
        uf[i] = self.find(uf, uf[i])
        return uf[i]

    def minOperationsQueries(self, n: int, edges: List[List[int]], queries: List[List[int]]) -> List[int]:
        m, W = len(queries), 26
        neighbors = [dict() for i in range(n)]
        for edge in edges:
            neighbors[edge[0]][edge[1]] = edge[2]
            neighbors[edge[1]][edge[0]] = edge[2]
        queryArr = [[] for i in range(n)]
        for i in range(m):
            queryArr[queries[i][0]].append([queries[i][1], i])
            queryArr[queries[i][1]].append([queries[i][0], i])

        count = [[0 for j in range(W + 1)] for i in range(n)]
        visited, uf, lca = [0 for i in range(n)], [0 for i in range(n)], [0 for i in range(m)]

        def tarjan(node: int, parent: int):
            if parent != -1:
                count[node] = count[parent].copy()
                count[node][neighbors[node][parent]] += 1
            uf[node] = node
            for child in neighbors[node].keys():
                if child == parent:
                    continue
                tarjan(child, node)
                uf[child] = node
            for [node1, index] in queryArr[node]:
                if node != node1 and not visited[node1]:
                    continue
                lca[index] = self.find(uf, node1)
            visited[node] = 1

        tarjan(0, -1)
        res = [0 for i in range(m)]
        for i in range(m):
            totalCount, maxCount = 0, 0
            for j in range(1, W + 1):
                t = count[queries[i][0]][j] + count[queries[i][1]][j] - 2 * count[lca[i]][j]
                maxCount = max(maxCount, t)
                totalCount += t
            res[i] = totalCount - maxCount
        return res


if __name__ == "__main__":
    n = 7
    edges = [[0,1,1],[1,2,1],[2,3,1],[3,4,2],[4,5,2],[5,6,2]]
    queries = [[0,3],[3,6],[2,6],[0,6]]

    test = Solution().minOperationsQueries(n, edges, queries)

    print(test)
