import heapq
import math
from collections import Counter, deque
from functools import cache
from itertools import product
from typing import List, Optional


# 1749. 任意子数组和的绝对值的最大值
# 中等
# 给你一个整数数组 nums 。一个子数组 [numsl, numsl+1, ..., numsr-1, numsr] 的 和的绝对值 为 abs(numsl + numsl+1 + ... + numsr-1 + numsr) 。
#
# 请你找出 nums 中 和的绝对值 最大的任意子数组（可能为空），并返回该 最大值 。
#
# abs(x) 定义如下：
#
# 如果 x 是负整数，那么 abs(x) = -x 。
# 如果 x 是非负整数，那么 abs(x) = x 。
#
#
# 示例 1：
#
# 输入：nums = [1,-3,2,3,-4]
# 输出：5
# 解释：子数组 [2,3] 和的绝对值最大，为 abs(2+3) = abs(5) = 5 。
# 示例 2：
#
# 输入：nums = [2,-5,1,-4,3,-2]
# 输出：8
# 解释：子数组 [-5,1,-4] 和的绝对值最大，为 abs(-5+1-4) = abs(-8) = 8 。

class Solution:
    def maxAbsoluteSum(self, nums: List[int]) -> int:
        mx = [0] * (len(nums) + 1)
        mn = [0] * (len(nums) + 1)
        res = 0

        for i in range(len(nums)):
            mx[i + 1] = max(mx[i] + nums[i], nums[i])
            mn[i + 1] = min(mn[i] + nums[i], nums[i])

            res = max(res, max(mx[i + 1], -mn[i + 1]))
        return res


if __name__ == "__main__":
    nums = [2,-5,1,-4,3,-2]

    test = Solution().maxAbsoluteSum(nums)
    print(test)
