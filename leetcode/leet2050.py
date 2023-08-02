import heapq
import math
from collections import Counter, deque
from functools import cache
from itertools import product
from typing import List, Optional


# 2050. 并行课程 III
# 困难
# 给你一个整数 n ，表示有 n 节课，课程编号从 1 到 n 。同时给你一个二维整数数组 relations ，其中 relations[j] = [prevCoursej, nextCoursej] ，表示课程 prevCoursej 必须在课程 nextCoursej 之前 完成（先修课的关系）。同时给你一个下标从 0 开始的整数数组 time ，其中 time[i] 表示完成第 (i+1) 门课程需要花费的 月份 数。
#
# 请你根据以下规则算出完成所有课程所需要的 最少 月份数：
#
# 如果一门课的所有先修课都已经完成，你可以在 任意 时间开始这门课程。
# 你可以 同时 上 任意门课程 。
# 请你返回完成所有课程所需要的 最少 月份数。
#
# 注意：测试数据保证一定可以完成所有课程（也就是先修课的关系构成一个有向无环图）。
#
#
#
# 示例 1:
#
#
#
# 输入：n = 3, relations = [[1,3],[2,3]], time = [3,2,5]
# 输出：8
# 解释：上图展示了输入数据所表示的先修关系图，以及完成每门课程需要花费的时间。
# 你可以在月份 0 同时开始课程 1 和 2 。
# 课程 1 花费 3 个月，课程 2 花费 2 个月。
# 所以，最早开始课程 3 的时间是月份 3 ，完成所有课程所需时间为 3 + 5 = 8 个月。
# 示例 2：
#
#
#
# 输入：n = 5, relations = [[1,5],[2,5],[3,5],[3,4],[4,5]], time = [1,2,3,4,5]
# 输出：12
# 解释：上图展示了输入数据所表示的先修关系图，以及完成每门课程需要花费的时间。
# 你可以在月份 0 同时开始课程 1 ，2 和 3 。
# 在月份 1，2 和 3 分别完成这三门课程。
# 课程 4 需在课程 3 之后开始，也就是 3 个月后。课程 4 在 3 + 4 = 7 月完成。
# 课程 5 需在课程 1，2，3 和 4 之后开始，也就是在 max(1,2,3,7) = 7 月开始。
# 所以完成所有课程所需的最少时间为 7 + 5 = 12 个月。
#

class Solution:
    def minimumTime(self, n: int, relations: List[List[int]], time: List[int]) -> int:
        adj = {}
        di = [0] * n
        for r in relations:
            i = r[0] - 1
            o = r[1] - 1
            di[o] += 1
            if i in adj:
                adj[i].add(o)
            else:
                adj[i] = {o}
        q = deque()
        res = [0] * n
        for i in range(n):
            if di[i] == 0:
                q.append(i)
                res[i] = time[i]

        while q:
            i = q.popleft()
            if i in adj:
                for j in adj[i]:
                    res[j] = max(res[i] + time[j], res[j])
                    di[j] -= 1
                    if di[j] == 0:
                        q.append(j)
        return max(res)

    # mx = 0
    # prev = [[] for _ in range(n + 1)]
    # for x, y in relations:
    #     prev[y].append(x)
    #
    # @lru_cache(None)
    # def dp(i: int) -> int:
    #     cur = 0
    #     for p in prev[i]:
    #         cur = max(cur, dp(p))
    #     cur += time[i - 1]
    #     return cur
    #
    # for i in range(1, n + 1):
    #     mx = max(mx, dp(i))
    # return mx


if __name__ == "__main__":
    n = 9
    relations = [[2,7],[2,6],[3,6],[4,6],[7,6],[2,1],[3,1],[4,1],[6,1],[7,1],[3,8],[5,8],[7,8],[1,9],[2,9],[6,9],[7,9]]
    time = [9,5,9,5,8,7,7,8,4]

    test = Solution().minimumTime(n, relations, time)
    print(test)
