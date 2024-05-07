import heapq
import math
from collections import deque, Counter
from itertools import count
from typing import List


# 1052. 爱生气的书店老板
# 中等
# 相关标签
# 相关企业
# 提示
# 有一个书店老板，他的书店开了 n 分钟。每分钟都有一些顾客进入这家商店。给定一个长度为 n 的整数数组 customers ，其中 customers[i] 是在第 i 分钟开始时进入商店的顾客数量，所有这些顾客在第 i 分钟结束后离开。
#
# 在某些时候，书店老板会生气。 如果书店老板在第 i 分钟生气，那么 grumpy[i] = 1，否则 grumpy[i] = 0。
#
# 当书店老板生气时，那一分钟的顾客就会不满意，若老板不生气则顾客是满意的。
#
# 书店老板知道一个秘密技巧，能抑制自己的情绪，可以让自己连续 minutes 分钟不生气，但却只能使用一次。
#
# 请你返回 这一天营业下来，最多有多少客户能够感到满意 。
#
#
# 示例 1：
#
# 输入：customers = [1,0,1,2,1,1,7,5], grumpy = [0,1,0,1,0,1,0,1], minutes = 3
# 输出：16
# 解释：书店老板在最后 3 分钟保持冷静。
# 感到满意的最大客户数量 = 1 + 1 + 1 + 1 + 7 + 5 = 16.
# 示例 2：
#
# 输入：customers = [1], grumpy = [0], minutes = 1
# 输出：1
#
#
# 提示：
#
# n == customers.length == grumpy.length
# 1 <= minutes <= n <= 2 * 104
# 0 <= customers[i] <= 1000
# grumpy[i] == 0 or 1
#


class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], minutes: int) -> int:
        n = len(customers)
        sn = [0] * (n + 1)
        tn = [0] * (n + 1)
        for i in range(n):
            sn[i + 1] = sn[i] + (customers[i] if grumpy[i] == 0 else 0)
            tn[i + 1] = tn[i] + customers[i]
        res = 0
        for i in range(n - minutes):
            res = max(res, sn[i] - sn[0] + tn[i + minutes] - tn[i] + sn[-1] - sn[i + minutes])
        return res





if __name__ == "__main__":
    customers = [1]
    grumpy = [0]
    minutes = 1
    test = Solution().maxSatisfied(customers, grumpy, minutes)
    print(test)
