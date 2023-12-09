import heapq
import math
from collections import Counter
from typing import List
from sortedcontainers import SortedList


# 2316. 统计无向图中无法互相到达点对数
# 提示
# 中等
# 46
# 相关企业
# 给你一个整数 n ，表示一张 无向图 中有 n 个节点，编号为 0 到 n - 1 。同时给你一个二维整数数组 edges ，其中 edges[i] = [ai, bi] 表示节点 ai 和 bi 之间有一条 无向 边。
#
# 请你返回 无法互相到达 的不同 点对数目 。
#
#
#
# 示例 1：
#
#
#
# 输入：n = 3, edges = [[0,1],[0,2],[1,2]]
# 输出：0
# 解释：所有点都能互相到达，意味着没有点对无法互相到达，所以我们返回 0 。
# 示例 2：
#
#
#
# 输入：n = 7, edges = [[0,2],[0,5],[2,4],[1,6],[5,4]]
# 输出：14
# 解释：总共有 14 个点对互相无法到达：
# [[0,1],[0,3],[0,6],[1,2],[1,3],[1,4],[1,5],[2,3],[2,6],[3,4],[3,5],[3,6],[4,6],[5,6]]
# 所以我们返回 14 。
#


class Solution:
    def countPairs(self, n: int, edges: List[List[int]]) -> int:
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

        searched = set()
        com = []
        for i in range(n):
            if i not in searched:
                q = [i]
                k = 1
                searched.add(i)
                while q:
                    node = q[0]
                    q = q[1:]
                    if node in adj:
                        for j in adj[node]:
                            if j not in searched:
                                q.append(j)
                                searched.add(j)
                                k += 1
                com.append(k)
        remain = n
        res = 0
        for x in com:
            res += x * (remain - x)
            remain -= x
        return res



if __name__ == "__main__":
    n = 7
    edges = [[0,2],[0,5],[2,4],[1,6],[5,4]]
    test = Solution().countPairs(n, edges)
    print(test)
