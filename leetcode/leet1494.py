import heapq
import math
from collections import Counter
from typing import List, Optional


# 1494. 并行课程 II
# 给你一个整数 n 表示某所大学里课程的数目，编号为 1 到 n ，数组 relations 中， relations[i] = [xi, yi]  表示一个先修课的关系，也就是课程 xi 必须在课程 yi 之前上。同时你还有一个整数 k 。
#
# 在一个学期中，你 最多 可以同时上 k 门课，前提是这些课的先修课在之前的学期里已经上过了。
#
# 请你返回上完所有课最少需要多少个学期。题目保证一定存在一种上完所有课的方式。
#
#
#
# 示例 1：
#
#
#
# 输入：n = 4, relations = [[2,1],[3,1],[1,4]], k = 2
# 输出：3
# 解释：上图展示了题目输入的图。在第一个学期中，我们可以上课程 2 和课程 3 。然后第二个学期上课程 1 ，第三个学期上课程 4 。
# 示例 2：
#
#
#
# 输入：n = 5, relations = [[2,1],[3,1],[4,1],[1,5]], k = 2
# 输出：4
# 解释：上图展示了题目输入的图。一个最优方案是：第一学期上课程 2 和 3，第二学期上课程 4 ，第三学期上课程 1 ，第四学期上课程 5 。
# 示例 3：
#
# 输入：n = 11, relations = [], k = 2
# 输出：6
#

class Solution:
    def minNumberOfSemesters(self, n: int, relations: List[List[int]], k: int) -> int:
        # adj1 = [set() for _ in range(n)]
        # adj2 = [set() for _ in range(n)]
        #
        # for x in relations:
        #     adj1[x[1] - 1].add(x[0] - 1)
        #     adj2[x[0] - 1].add(x[1] - 1)
        #
        # s = []
        # dis = [0] * n
        # searched = set()
        # a2 = [adj2[i].copy() for i in range(len(adj2))]
        # stage = 0
        # while len(searched) < n:
        #     ss = set()
        #     for i in range(n):
        #         if len(a2[i]) == 0 and i not in searched:
        #             searched.add(i)
        #             dis[i] = stage
        #             ss.add(i)
        #     for x in ss:
        #         for y in adj1[x]:
        #             a2[y].remove(x)
        #     stage += 1
        #
        # searched = set()
        # for i in range(n):
        #     if len(adj1[i]) == 0:
        #         s.append((dis[i], len(adj2[i]), i))
        #         searched.add(i)
        # s.sort(key=lambda x: (x[0], x[1]), reverse=True)
        #
        # res = 0
        # while len(searched) < n:
        #     res += 1
        #     for i in range(min(k, len(s))):
        #         for y in adj2[s[i][2]]:
        #             adj1[y].remove(s[i][2])
        #     s = s[min(k, len(s)):]
        #     for j in range(n):
        #         if len(adj1[j]) == 0 and j not in searched:
        #             s.append((dis[j], len(adj2[j]), j))
        #             searched.add(j)
        #     if len(s) > 0:
        #         s.sort(key=lambda x: (x[0], x[1]), reverse=True)
        # if len(s) != 0:
        #     if len(s) % k == 0:
        #         res += (len(s) // k)
        #     else:
        #         res += (len(s) // k + 1)
        # return res
        dp = [math.inf] * (1 << n)
        need = [0] * (1 << n)
        for edge in relations:
            need[(1 << (edge[1] - 1))] |= 1 << (edge[0] - 1)
        dp[0] = 0
        for i in range(1, (1 << n)):
            need[i] = need[i & (i - 1)] | need[i & (-i)]
            if (need[i] | i) != i:  # i 中有任意一门课程的前置课程没有完成学习
                continue
            sub = valid = i ^ need[i]  # 当前学期可以进行学习的课程集合
            if sub.bit_count() <= k:  # 如果个数小于 k，则可以全部学习，不再枚举子集
                dp[i] = min(dp[i], dp[i ^ sub] + 1)
            else:  # 枚举子集
                while sub:
                    if sub.bit_count() <= k:
                        dp[i] = min(dp[i], dp[i ^ sub] + 1)
                    sub = (sub - 1) & valid
        return dp[-1]


if __name__ == "__main__":
    n = 4
    relations = [[2,1],[3,1],[1,4]]
    k = 2

    test = Solution().minNumberOfSemesters(n, relations, k)
    print(test)
