import math
from typing import List
from functools import cache


# 2646. 最小化旅行的价格总和
# 提示
# 困难
# 46
# 相关企业
# 现有一棵无向、无根的树，树中有 n 个节点，按从 0 到 n - 1 编号。给你一个整数 n 和一个长度为 n - 1 的二维整数数组 edges ，其中 edges[i] = [ai, bi] 表示树中节点 ai 和 bi 之间存在一条边。
#
# 每个节点都关联一个价格。给你一个整数数组 price ，其中 price[i] 是第 i 个节点的价格。
#
# 给定路径的 价格总和 是该路径上所有节点的价格之和。
#
# 另给你一个二维整数数组 trips ，其中 trips[i] = [starti, endi] 表示您从节点 starti 开始第 i 次旅行，并通过任何你喜欢的路径前往节点 endi 。
#
# 在执行第一次旅行之前，你可以选择一些 非相邻节点 并将价格减半。
#
# 返回执行所有旅行的最小价格总和。
#
#
#
# 示例 1：
#
#
# 输入：n = 4, edges = [[0,1],[1,2],[1,3]], price = [2,2,10,6], trips = [[0,3],[2,1],[2,3]]
# 输出：23
# 解释：
# 上图表示将节点 2 视为根之后的树结构。第一个图表示初始树，第二个图表示选择节点 0 、2 和 3 并使其价格减半后的树。
# 第 1 次旅行，选择路径 [0,1,3] 。路径的价格总和为 1 + 2 + 3 = 6 。
# 第 2 次旅行，选择路径 [2,1] 。路径的价格总和为 2 + 5 = 7 。
# 第 3 次旅行，选择路径 [2,1,3] 。路径的价格总和为 5 + 2 + 3 = 10 。
# 所有旅行的价格总和为 6 + 7 + 10 = 23 。可以证明，23 是可以实现的最小答案。
# 示例 2：
#
#
# 输入：n = 2, edges = [[0,1]], price = [2,2], trips = [[0,0]]
# 输出：1
# 解释：
# 上图表示将节点 0 视为根之后的树结构。第一个图表示初始树，第二个图表示选择节点 0 并使其价格减半后的树。
# 第 1 次旅行，选择路径 [0] 。路径的价格总和为 1 。
# 所有旅行的价格总和为 1 。可以证明，1 是可以实现的最小答案。
#


class Solution:
    def minimumTotalPrice(self, n: int, edges: List[List[int]], price: List[int], trips: List[List[int]]) -> int:
        if n == 1:
            return price[0] // 2 * len(trips)
        adj = {}
        deg = [0] * n

        for e in edges:
            if e[0] in adj:
                adj[e[0]].add(e[1])
            else:
                adj[e[0]] = {e[1]}
            if e[1] in adj:
                adj[e[1]].add(e[0])
            else:
                adj[e[1]] = {e[0]}
            deg[e[0]] += 1
            deg[e[1]] += 1

        def dfs(s, d, searched, p):
            p = p + (s,)
            if s == d:
                return p
            searched.add(s)
            for ne in adj[s]:
                if ne not in searched:
                    r = dfs(ne, d, searched, p)
                    if r:
                        return r

        w = [0] * n
        for t in trips:
            p = dfs(t[0], t[1], set(), tuple())
            for i in p:
                w[i] += 1
        res = 0
        p = {}
        v = [i for i in range(n) if deg[i] == 1]
        # searched = set()
        # a = n
        # while v:
        #     c = v[0]
        #     v = v[1:]
        #     searched.add(c)
        #     if w[c] == 0:
        #         deg[c] = 0
        #         a -= 1
        #         for u in adj[c]:
        #             if u not in searched:
        #                 deg[u] -= 1
        #                 adj[u].discard(c)
        #                 if deg[u] == 1:
        #                     v.append(u)
        # v = [i for i in range(n) if deg[i] == 1]
        while v:
            c = v[0]
            v = v[1:]

            p[c] = [price[c] // 2 * w[c], price[c] * w[c]]
            for u in adj[c]:
                if u in p:
                    p[c][0] += p[u][1]
                    p[c][1] += min(p[u])
                else:
                    deg[u] -= 1
                    if deg[u] == 1:
                        v.append(u)
            res = min(p[c])

        return res


if __name__ == "__main__":
    n = 1
    edges = []
    price = [2]
    trips = [[0,0]]

    test = Solution().minimumTotalPrice(n, edges, price, trips)
    print(test)
