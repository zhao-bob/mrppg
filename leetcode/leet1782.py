import collections
import heapq
import math
from bisect import bisect_right
from collections import Counter, deque
from functools import cache
from itertools import product
from typing import List, Optional


# 1782. 统计点对的数目
# 提示
# 困难
# 135
# 相关企业
# 给你一个无向图，无向图由整数 n  ，表示图中节点的数目，和 edges 组成，其中 edges[i] = [ui, vi] 表示 ui 和 vi 之间有一条无向边。同时给你一个代表查询的整数数组 queries 。
#
# 第 j 个查询的答案是满足如下条件的点对 (a, b) 的数目：
#
# a < b
# cnt 是与 a 或者 b 相连的边的数目，且 cnt 严格大于 queries[j] 。
# 请你返回一个数组 answers ，其中 answers.length == queries.length 且 answers[j] 是第 j 个查询的答案。
#
# 请注意，图中可能会有 重复边 。
#
#
#
# 示例 1：
#
#
# 输入：n = 4, edges = [[1,2],[2,4],[1,3],[2,3],[2,1]], queries = [2,3]
# 输出：[6,5]
# 解释：每个点对中，与至少一个点相连的边的数目如上图所示。
# answers[0] = 6。所有的点对(a, b)中边数和都大于2，故有6个；
# answers[1] = 5。所有的点对(a, b)中除了(3,4)边数等于3，其它点对边数和都大于3，故有5个。
# 示例 2：
#
# 输入：n = 5, edges = [[1,5],[1,5],[3,4],[2,5],[1,3],[5,1],[2,3],[2,5]], queries = [1,2,3,4,5]
# 输出：[10,10,9,8,6]

class Solution:
    def countPairs(self, n: int, edges: List[List[int]], queries: List[int]) -> List[int]:
        # degree = [0 for _ in range(n)]
        # cnt = collections.defaultdict(int)
        # for edge in edges:
        #     x, y = edge[0] - 1, edge[1] - 1
        #     if x > y:
        #         x, y = y, x
        #     degree[x] += 1
        #     degree[y] += 1
        #     cnt[x * n + y] += 1
        #
        # arr = sorted(degree)
        # ans = []
        # for bound in queries:
        #     total = 0
        #     for i in range(n):
        #         j = bisect_right(arr, bound - arr[i], i + 1)
        #         total += n - j
        #     for val, freq in cnt.items():
        #         x, y = val // n, val % n
        #         if degree[x] + degree[y] > bound >= degree[x] + degree[y] - freq:
        #             total -= 1
        #     ans.append(total)
        # return ans

        deg = [0] * (n + 1)
        cnt_e = dict()  # 比 Counter 快一点
        for x, y in edges:
            if x > y: x, y = y, x
            deg[x] += 1
            deg[y] += 1
            cnt_e[(x, y)] = cnt_e.get((x, y), 0) + 1
        cnt_deg = Counter(deg[1:])

        # 2)
        cnts = [0] * (max(deg) * 2 + 2)
        for deg1, c1 in cnt_deg.items():
            for deg2, c2 in cnt_deg.items():
                if deg1 < deg2:
                    cnts[deg1 + deg2] += c1 * c2
                elif deg1 == deg2:
                    cnts[deg1 + deg2] += c1 * (c1 - 1) // 2

        # 3)
        for (x, y), c in cnt_e.items():
            s = deg[x] + deg[y]
            cnts[s] -= 1
            cnts[s - c] += 1

        # 4) 计算 cnts 的后缀和
        for i in range(len(cnts) - 1, 0, -1):
            cnts[i - 1] += cnts[i]

        for i, q in enumerate(queries):
            queries[i] = cnts[min(q + 1, len(cnts) - 1)]
        return queries


if __name__ == "__main__":
    n = 4
    edges = [[1,2],[2,4],[1,3],[2,3],[2,1]]
    queries = [2,3]

    test = Solution().countPairs(n, edges, queries)

    print(test)
