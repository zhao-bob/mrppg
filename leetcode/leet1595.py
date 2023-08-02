import heapq
import math
from collections import Counter
from typing import List, Optional


# 1595. 连通两组点的最小成本
# 给你两组点，其中第一组中有 size1 个点，第二组中有 size2 个点，且 size1 >= size2 。
#
# 任意两点间的连接成本 cost 由大小为 size1 x size2 矩阵给出，其中 cost[i][j] 是第一组中的点 i 和第二组中的点 j 的连接成本。如果两个组中的每个点都与另一组中的一个或多个点连接，则称这两组点是连通的。换言之，第一组中的每个点必须至少与第二组中的一个点连接，且第二组中的每个点必须至少与第一组中的一个点连接。
#
# 返回连通两组点所需的最小成本。
#
#
#
# 示例 1：
#
#
#
# 输入：cost = [[15, 96], [36, 2]]
# 输出：17
# 解释：连通两组点的最佳方法是：
# 1--A
# 2--B
# 总成本为 17 。
# 示例 2：
#
#
#
# 输入：cost = [[1, 3, 5], [4, 1, 1], [1, 5, 3]]
# 输出：4
# 解释：连通两组点的最佳方法是：
# 1--A
# 2--B
# 2--C
# 3--A
# 最小成本为 4 。
# 请注意，虽然有多个点连接到第一组中的点 2 和第二组中的点 A ，但由于题目并不限制连接点的数目，所以只需要关心最低总成本。
#

class Solution:
    def connectTwoGroups(self, cost: List[List[int]]) -> int:
        size1, size2 = len(cost), len(cost[0])
        m = 1 << size2
        dp = [[float("inf")] * m for _ in range(size1 + 1)]
        dp[0][0] = 0

        for i in range(1, size1 + 1):
            for s in range(m):
                for k in range(size2):
                    if (s & (1 << k)) == 0:
                        continue
                    dp[i][s] = min(dp[i][s], dp[i][s ^ (1 << k)] + cost[i - 1][k])
                    dp[i][s] = min(dp[i][s], dp[i - 1][s] + cost[i - 1][k])
                    dp[i][s] = min(dp[i][s], dp[i - 1][s ^ (1 << k)] + cost[i - 1][k])

        return dp[size1][m - 1]
        # cq = []
        # n = len(cost)
        # m = len(cost[0])
        #
        # for i in range(n):
        #     for j in range(m):
        #         cq.append((cost[i][j], i, n + j))
        #
        # cq.sort(key=lambda x: (x[0], x[1]), reverse=True)
        #
        # connected = set()
        #
        # res = 0
        # edge = {}
        # while len(connected) < n + m:
        #     c, i, j = cq.pop()
        #     if i not in connected or j not in connected:
        #         res += c
        #         connected.add(i)
        #         connected.add(j)
        #         if i in edge:
        #             edge[i].add(j)
        #         else:
        #             edge[i] = {j}
        #         if j in edge:
        #             edge[j].add(i)
        #         else:
        #             edge[j] = {i}
        #     else:
        #         e1 = edge[i]
        #         e2 = edge[j]
        #         exchange = False
        #         for x in e2:
        #             for y in e1:
        #                 if x in edge[y] and cost[x][y - n] + c < cost[i][y - n] + cost[x][j - n]:
        #                     edge[x].remove(j)
        #                     edge[j].remove(x)
        #                     edge[y].remove(i)
        #                     edge[i].remove(y)
        #                     exchange = True
        #                     res = res + c - cost[i][y - n] - cost[x][j - n]
        #                     break
        #             if exchange:
        #                 e1.add(j)
        #                 e2.add(i)
        #                 break
        #
        # for x in edge:
        #     if len(edge[x]) > 1:
        #         rl = []
        #         for y in edge[x]:
        #             if len(edge[y]) > 1:
        #                 res -= cost[x][y - n]
        #                 rl.append(y)
        #                 edge[y].remove(x)
        #         for k in rl:
        #             edge[x].remove(k)
        #     else:
        #         if x < n:
        #             for y in edge[x]:
        #                 if len(edge[y]) > 1:
        #                     c = cost[x][y - n]
        #                     e = -1
        #                     for j in range(m):
        #                         if cost[x][j] < c:
        #                             e = j
        #                             c = cost[x][j]
        #                     if e >= 0:
        #                         res -= (cost[x][y - n] - cost[x][e])
        #                         edge[e + n].add(x)
        #                         edge[x].remove(y)
        #                         edge[x].add(e + n)
        #                         edge[y].remove(x)
        #
        # return res


if __name__ == "__main__":
    cost = [[9,1,72],[97,29,85],[16,10,25],[22,49,42],[43,98,81],[38,44,13],[32,22,34]]

    test = Solution().connectTwoGroups(cost)
    print(test)
