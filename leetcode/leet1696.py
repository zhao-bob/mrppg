# 1696. 跳跃游戏 VI
# 中等
# 相关标签
# 相关企业
# 提示
# 给你一个下标从 0 开始的整数数组 nums 和一个整数 k 。
#
# 一开始你在下标 0 处。每一步，你最多可以往前跳 k 步，但你不能跳出数组的边界。也就是说，你可以从下标 i 跳到 [i + 1， min(n - 1, i + k)] 包含 两个端点的任意位置。
#
# 你的目标是到达数组最后一个位置（下标为 n - 1 ），你的 得分 为经过的所有数字之和。
#
# 请你返回你能得到的 最大得分 。
#
#
#
# 示例 1：
#
# 输入：nums = [1,-1,-2,4,-7,3], k = 2
# 输出：7
# 解释：你可以选择子序列 [1,-1,4,3] （上面加粗的数字），和为 7 。
# 示例 2：
#
# 输入：nums = [10,-5,-2,4,0,3], k = 3
# 输出：17
# 解释：你可以选择子序列 [10,4,3] （上面加粗数字），和为 17 。
# 示例 3：
#
# 输入：nums = [1,-5,-20,4,-1,3,-6,-3], k = 2
# 输出：0
#
#
# 提示：
#
#  1 <= nums.length, k <= 105
# -104 <= nums[i] <= 104
#

import heapq
import math
from collections import Counter, deque
from datetime import date
from functools import cache
from typing import List, Optional

from sortedcontainers import SortedList


class Solution:
    def maxResult(self, nums: List[int], k: int) -> int:
        # n = len(nums)
        # sl = SortedList()
        # dp = [-math.inf] * n
        # dp[0] = nums[0]
        # sl.add(dp[0])
        # for i in range(1, n):
        #     dp[i] = nums[i] + sl[-1]
        #     if i - k >= 0:
        #         sl.remove(dp[i - k])
        #     sl.add(dp[i])
        #
        # return dp[-1]

        n = len(nums)
        dp = [0] * n
        dp[0] = nums[0]
        queue = deque([0])
        for i in range(1, n):
            while queue and queue[0] < i - k:
                queue.popleft()
            dp[i] = dp[queue[0]] + nums[i]
            while queue and dp[queue[-1]] <= dp[i]:
                queue.pop()
            queue.append(i)
        return dp[n - 1]


        # for i in range(1, n):
        #     for j in range(min(k, i)):
        #         dp[i] = max(dp[i - j - 1] + nums[i], dp[i])
        # return dp[-1]
        # s = nums[0]
        # n = len(nums)
        # pre = 1
        # dp = [0] * k
        # for i in range(1, n - 1):
        #     if nums[i] >= 0 and i - pre <= k:
        #         s += nums[i]
        #         pre = i
        #     else:
        #         if i - pre <= k:
        #
        # while i < n:
        #     l = min(k, n - i)
        #     r = 0
        #     mx = -math.inf
        #     ni = -1
        #     mi = -1
        #     for j in range(l):
        #         if nums[i + j] > 0:
        #             r += nums[i + j]
        #             ni = i + j
        #         else:
        #             if nums[i + j] > mx:
        #                 mx = nums[i + j]
        #                 mi = i + j
        #     if r == 0 and mx < 0:
        #         r = mx
        #         ni = mi
        #     if i + k > n - 1 > ni:
        #         if r <= 0:
        #             r = nums[-1]
        #             ni = n - 1
        #     s += r
        #     i = ni + 1
        # return s




if __name__ == "__main__":
    nums = [1,2,-3,-4,-5,-6]
    k = 2

    test = Solution().maxResult(nums, k)

    print(test)
