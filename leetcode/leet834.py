import heapq
import math
from collections import Counter, deque
from functools import cache
from itertools import product
from typing import List, Optional

# 834. 树中距离之和
# 给定一个无向、连通的树。树中有 n 个标记为 0...n-1 的节点以及 n-1 条边 。
#
# 给定整数 n 和数组 edges ， edges[i] = [ai, bi]表示树中的节点 ai 和 bi 之间有一条边。
#
# 返回长度为 n 的数组 answer ，其中 answer[i] 是树中第 i 个节点与所有其他节点之间的距离之和。
#
#
#
# 示例 1:
#
#
#
# 输入: n = 6, edges = [[0,1],[0,2],[2,3],[2,4],[2,5]]
# 输出: [8,12,6,10,10,10]
# 解释: 树如图所示。
# 我们可以计算出 dist(0,1) + dist(0,2) + dist(0,3) + dist(0,4) + dist(0,5)
# 也就是 1 + 1 + 2 + 2 + 2 = 8。 因此，answer[0] = 8，以此类推。
# 示例 2:
#
#
# 输入: n = 1, edges = []
# 输出: [0]
# 示例 3:
#
#
# 输入: n = 2, edges = [[1,0]]
# 输出: [1,1]

class Solution:
    def sumOfDistancesInTree(self, n: int, edges: List[List[int]]) -> List[int]:
        def dfs(s, adj, t, d, searched):
            ne = adj[s]
            searched.add(s)
            if len(ne) == 1:
                t[s] = 1
                d[s] = 0
                return [t[s], d[s]]
            for x in ne:
                if x not in searched:
                    [a, b] = dfs(x, adj, t, d, searched)
                    t[s] += a
                    d[s] += b + a
            return [t[s], d[s]]

        if len(edges) == 0:
            return [0]
        if len(edges) == 1:
            return [1, 1]
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
        s = 0
        m = 0
        for i in range(n):
            if len(adj[i]) > m:
                s = i
                m = len(adj[i])
        t = [1] * n
        d = [0] * n
        searched = set()
        dfs(s, adj, t, d, searched)

        q = [s]
        searched = set()
        while len(q) > 0:
            i = q[0]
            q = q[1:]
            searched.add(i)
            for x in adj[i]:
                if x not in searched:
                    d[x] = d[i] - t[x] + n - t[x]
                    q.append(x)
        return d


if __name__ == "__main__":
    n = 2
    edges = [[1,0]]

    test = Solution().sumOfDistancesInTree(n, edges)
    print(test)
