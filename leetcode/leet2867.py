# 2867. 统计树中的合法路径数目
# 困难
# 相关标签
# 相关企业
# 提示
# 给你一棵 n 个节点的无向树，节点编号为 1 到 n 。给你一个整数 n 和一个长度为 n - 1 的二维整数数组 edges ，其中 edges[i] = [ui, vi] 表示节点 ui 和 vi 在树中有一条边。
#
# 请你返回树中的 合法路径数目 。
#
# 如果在节点 a 到节点 b 之间 恰好有一个 节点的编号是质数，那么我们称路径 (a, b) 是 合法的 。
#
# 注意：
#
# 路径 (a, b) 指的是一条从节点 a 开始到节点 b 结束的一个节点序列，序列中的节点 互不相同 ，且相邻节点之间在树上有一条边。
# 路径 (a, b) 和路径 (b, a) 视为 同一条 路径，且只计入答案 一次 。
#
#
# 示例 1：
#
#
#
# 输入：n = 5, edges = [[1,2],[1,3],[2,4],[2,5]]
# 输出：4
# 解释：恰好有一个质数编号的节点路径有：
# - (1, 2) 因为路径 1 到 2 只包含一个质数 2 。
# - (1, 3) 因为路径 1 到 3 只包含一个质数 3 。
# - (1, 4) 因为路径 1 到 4 只包含一个质数 2 。
# - (2, 4) 因为路径 2 到 4 只包含一个质数 2 。
# 只有 4 条合法路径。
# 示例 2：
#
#
#
# 输入：n = 6, edges = [[1,2],[1,3],[2,4],[3,5],[3,6]]
# 输出：6
# 解释：恰好有一个质数编号的节点路径有：
# - (1, 2) 因为路径 1 到 2 只包含一个质数 2 。
# - (1, 3) 因为路径 1 到 3 只包含一个质数 3 。
# - (1, 4) 因为路径 1 到 4 只包含一个质数 2 。
# - (1, 6) 因为路径 1 到 6 只包含一个质数 3 。
# - (2, 4) 因为路径 2 到 4 只包含一个质数 2 。
# - (3, 6) 因为路径 3 到 6 只包含一个质数 3 。
# 只有 6 条合法路径。
#
#
# 提示：
#
# 1 <= n <= 105
# edges.length == n - 1
# edges[i].length == 2
# 1 <= ui, vi <= n
# 输入保证 edges 形成一棵合法的树。
#

import heapq
import math
from collections import Counter, deque, defaultdict
from datetime import date
from functools import cache
from typing import List, Optional

from sortedcontainers import SortedList


class Solution:
    def countPaths(self, n: int, edges: List[List[int]]) -> int:

        def prime(n):
            if n <= 1:
                return False
            for i in range(2, math.floor(math.sqrt(n) + 1)):
                if n % i == 0:
                    return False
            return True

        if n == 1:
            return 0
        ps = set()
        for i in range(1, n + 1):
            if prime(i):
                ps.add(i)
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

        k = 0
        nset = [0] * n
        s = {}
        seen = set()

        def dfs(n):
            res = 1
            seen.add(n)
            for a in adj[n]:
                if a not in ps and a not in seen:
                    nset[a - 1] = k
                    res += dfs(a)
            return res

        for i in range(1, n + 1):
            if i in ps:
                continue
            else:
                if nset[i - 1] == 0:
                    k += 1
                    nset[i - 1] = k
                    s[k] = dfs(i)
        res = 0
        for p in ps:
            cs = 0
            c = 0
            for a in adj[p]:
                if a not in ps:
                    cs += s[nset[a - 1]] * c
                    c += s[nset[a - 1]]
            cs += c
            res += cs
        return res


if __name__ == "__main__":
    n = 10
    edges = [[10,9],[2,10],[1,10],[3,2],[6,10],[4,3],[8,6],[5,8],[7,6]]
    test = Solution().countPaths(n, edges)
    print(test)
