import heapq
import math
from collections import deque, Counter
from itertools import count
from typing import List, Optional


# 1235. 规划兼职工作
# 困难
# 相关标签
# 相关企业
# 提示
# 你打算利用空闲时间来做兼职工作赚些零花钱。
#
# 这里有 n 份兼职工作，每份工作预计从 startTime[i] 开始到 endTime[i] 结束，报酬为 profit[i]。
#
# 给你一份兼职工作表，包含开始时间 startTime，结束时间 endTime 和预计报酬 profit 三个数组，请你计算并返回可以获得的最大报酬。
#
# 注意，时间上出现重叠的 2 份工作不能同时进行。
#
# 如果你选择的工作在时间 X 结束，那么你可以立刻进行在时间 X 开始的下一份工作。
#
#
#
# 示例 1：
#
#
#
# 输入：startTime = [1,2,3,3], endTime = [3,4,5,6], profit = [50,10,40,70]
# 输出：120
# 解释：
# 我们选出第 1 份和第 4 份工作，
# 时间范围是 [1-3]+[3-6]，共获得报酬 120 = 50 + 70。
# 示例 2：
#
#
#
# 输入：startTime = [1,2,3,4,6], endTime = [3,5,10,6,9], profit = [20,20,100,70,60]
# 输出：150
# 解释：
# 我们选择第 1，4，5 份工作。
# 共获得报酬 150 = 20 + 70 + 60。
# 示例 3：
#
#
#
# 输入：startTime = [1,1,1], endTime = [2,3,4], profit = [5,6,4]
# 输出：6
#
#
# 提示：
#
# 1 <= startTime.length == endTime.length == profit.length <= 5 * 10^4
# 1 <= startTime[i] < endTime[i] <= 10^9
# 1 <= profit[i] <= 10^4
#

class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        n = len(startTime)
        interval = [(startTime[i], endTime[i], profit[i]) for i in range(n)]

        interval.sort(key=lambda x: x[1])

        stk = [(0, 0)]

        def bisect(s):
            left = 0
            right = len(stk)

            while left < right:
                mid = (left + right) // 2
                if stk[mid][0] < s:
                    left = mid + 1
                elif stk[mid][0] > s:
                    right = mid
                else:
                    return mid
            return left - 1

        for i in interval:
            index = bisect(i[0])
            mx = max(stk[-1][1], stk[index][1] + i[2])
            while stk and stk[-1][0] == i[1]:
                stk.pop()
            stk.append((i[1], mx))
        return stk[-1][1]


if __name__ == "__main__":
    startTime = [4,3,1,2,4,8,3,3,3,9]
    endTime = [5,6,3,5,9,9,8,5,7,10]
    profit = [9,9,5,12,10,11,10,4,14,7]
    test = Solution().jobScheduling(startTime, endTime, profit)
    print(test)
