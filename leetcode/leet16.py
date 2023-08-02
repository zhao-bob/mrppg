import heapq
import math
from collections import Counter, deque
from functools import cache
from itertools import product
from typing import List, Optional


# 16. 最接近的三数之和
# 给你一个长度为 n 的整数数组 nums 和 一个目标值 target。请你从 nums 中选出三个整数，使它们的和与 target 最接近。
#
# 返回这三个数的和。
#
# 假定每组输入只存在恰好一个解。
#
#
#
# 示例 1：
#
# 输入：nums = [-1,2,1,-4], target = 1
# 输出：2
# 解释：与 target 最接近的和是 2 (-1 + 2 + 1 = 2) 。
# 示例 2：
#
# 输入：nums = [0,0,0], target = 1
# 输出：0
#
#

class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        n = len(nums)

        nums.sort()
        td = math.inf
        res = math.inf
        for i in range(n):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            l = i + 1
            r = n - 1
            d = math.inf
            s = math.inf
            while l < r:
                if nums[i] + nums[l] + nums[r] == target:
                    return target
                else:
                    if abs(nums[i] + nums[l] + nums[r] - target) < d:
                        s = nums[i] + nums[l] + nums[r]
                        d = abs(nums[i] + nums[l] + nums[r] - target)
                    if nums[i] + nums[l] + nums[r] > target:
                        while l < r and nums[r] == nums[r - 1]:
                            r = r - 1
                        r = r - 1
                    else:
                        while l < r and nums[l] == nums[l + 1]:
                            l = l + 1
                        l = l + 1
            if d < td:
                res = s
                td = d
        return res


if __name__ == "__main__":
    nums = [-1,2,1,-4]
    target = 0

    test = Solution().threeSumClosest(nums, target)
    print(test)
