import math
from collections import deque
from itertools import pairwise
from typing import List


# 1330. 翻转子数组得到最大的数组值
# 给你一个整数数组 nums 。「数组值」定义为所有满足 0 <= i < nums.length-1 的 |nums[i]-nums[i+1]| 的和。
#
# 你可以选择给定数组的任意子数组，并将该子数组翻转。但你只能执行这个操作 一次 。
#
# 请你找到可行的最大 数组值 。
#
#
#
# 示例 1：
#
# 输入：nums = [2,3,1,5,4]
# 输出：10
# 解释：通过翻转子数组 [3,1,5] ，数组变成 [2,5,1,3,4] ，数组值为 10 。
# 示例 2：
#
# 输入：nums = [2,4,9,24,2,1,10]
# 输出：68
#

class Solution:
    def maxValueAfterReverse(self, nums: List[int]) -> int:
        base = d = 0
        mx, mn = -math.inf, math.inf
        for a, b in pairwise(nums):
            base += abs(a - b)
            mx = max(mx, min(a, b))
            mn = min(mn, max(a, b))
            d = max(d, abs(nums[0] - b) - abs(a - b),  # i=0
                    abs(nums[-1] - a) - abs(a - b))  # j=n-1
        return base + max(d, 2 * (mx - mn))


if __name__ == "__main__":
    nums = [2,3,1,5,4]

    test = Solution().maxValueAfterReverse(nums)
    print(test)
