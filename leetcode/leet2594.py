import collections
import heapq
import math
from bisect import bisect_right
from collections import Counter, deque
from functools import cache
from itertools import product
from typing import List, Optional


# 2594. 修车的最少时间
# 中等
# 给你一个整数数组 ranks ，表示一些机械工的 能力值 。ranksi 是第 i 位机械工的能力值。能力值为 r 的机械工可以在 r * n2 分钟内修好 n 辆车。
#
# 同时给你一个整数 cars ，表示总共需要修理的汽车数目。
#
# 请你返回修理所有汽车 最少 需要多少时间。
#
# 注意：所有机械工可以同时修理汽车。
#
#
#
# 示例 1：
#
# 输入：ranks = [4,2,3,1], cars = 10
# 输出：16
# 解释：
# - 第一位机械工修 2 辆车，需要 4 * 2 * 2 = 16 分钟。
# - 第二位机械工修 2 辆车，需要 2 * 2 * 2 = 8 分钟。
# - 第三位机械工修 2 辆车，需要 3 * 2 * 2 = 12 分钟。
# - 第四位机械工修 4 辆车，需要 1 * 4 * 4 = 16 分钟。
# 16 分钟是修理完所有车需要的最少时间。
# 示例 2：
#
# 输入：ranks = [5,1,8], cars = 6
# 输出：16
# 解释：
# - 第一位机械工修 1 辆车，需要 5 * 1 * 1 = 5 分钟。
# - 第二位机械工修 4 辆车，需要 1 * 4 * 4 = 16 分钟。
# - 第三位机械工修 1 辆车，需要 8 * 1 * 1 = 8 分钟。
# 16 分钟时修理完所有车需要的最少时间。

class Solution:
    def repairCars(self, ranks: List[int], cars: int) -> int:
        # c = [0] * len(ranks)
        #
        # h = [(ranks[i], i) for i in range(len(ranks))]
        #
        # heapq.heapify(h)
        #
        # res = 0
        # for i in range(1, cars + 1):
        #     a = heapq.heappop(h)
        #     res = max(res, a[0])
        #     c[a[1]] += 1
        #     heapq.heappush(h, ((c[a[1]] + 1)*(c[a[1]] + 1)*ranks[a[1]], a[1]))
        # return res

        h = min(ranks) * cars * cars
        l = 1

        while l < h:
            m = (l + h) // 2

            if sum([math.floor(math.sqrt(m / x)) for x in ranks]) >= cars:
                h = m
            else:
                l = m + 1
        return l




if __name__ == "__main__":
    ranks = [5,1,8]
    cars = 6

    test = Solution().repairCars(ranks, cars)

    print(test)
