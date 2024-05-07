# 310. 最小高度树
# 中等
# 相关标签
# 相关企业
# 提示
# 树是一个无向图，其中任何两个顶点只通过一条路径连接。 换句话说，一个任何没有简单环路的连通图都是一棵树。
#
# 给你一棵包含 n 个节点的树，标记为 0 到 n - 1 。给定数字 n 和一个有 n - 1 条无向边的 edges 列表（每一个边都是一对标签），其中 edges[i] = [ai, bi] 表示树中节点 ai 和 bi 之间存在一条无向边。
#
# 可选择树中任何一个节点作为根。当选择节点 x 作为根节点时，设结果树的高度为 h 。在所有可能的树中，具有最小高度的树（即，min(h)）被称为 最小高度树 。
#
# 请你找到所有的 最小高度树 并按 任意顺序 返回它们的根节点标签列表。
#
# 树的 高度 是指根节点和叶子节点之间最长向下路径上边的数量。
#
#
# 示例 1：
#
#
# 输入：n = 4, edges = [[1,0],[1,2],[1,3]]
# 输出：[1]
# 解释：如图所示，当根是标签为 1 的节点时，树的高度是 1 ，这是唯一的最小高度树。
# 示例 2：
#
#
# 输入：n = 6, edges = [[3,0],[3,1],[3,2],[3,4],[5,4]]
# 输出：[3,4]
#
#
# 提示：
#
# 1 <= n <= 2 * 104
# edges.length == n - 1
# 0 <= ai, bi < n
# ai != bi
# 所有 (ai, bi) 互不相同
# 给定的输入 保证 是一棵树，并且 不会有重复的边
#

import heapq
import math
from collections import Counter, deque, defaultdict
from datetime import date
from functools import cache
from typing import List, Optional

from sortedcontainers import SortedList


class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n == 1:
            return [0]
        adj = {}
        for e in edges:
            if e[0] in adj:
                adj[e[0]].append(e[1])
            else:
                adj[e[0]] = [e[1]]
            if e[1] in adj:
                adj[e[1]].append(e[0])
            else:
                adj[e[1]] = [e[0]]

        seen = set()

        def dfs(i, k):
            r = (i, k)
            if i not in seen:
                seen.add(i)
                for a in adj[i]:
                    if a not in seen:
                        r1 = dfs(a, k + 1)
                        if r1[1] > r[1]:
                            r = r1
            return r

        def dfs1(i):
            r = []
            if i not in seen:
                seen.add(i)
                for a in adj[i]:
                    if a not in seen:
                        r1 = dfs1(a)
                        if len(r1) > len(r):
                            r = r1
            r.append(i)
            return r

        s1 = dfs(0, 0)
        seen.clear()
        res = dfs1(s1[0])
        if len(res) % 2 == 1:
            return [res[len(res) // 2]]
        else:
            return [res[len(res) // 2 - 1], res[len(res) // 2]]


if __name__ == "__main__":
    n = 6
    edges = [[3,0],[3,1],[3,2],[3,4],[5,4]]

    test = Solution().findMinHeightTrees(n, edges)
    print(test)
