import heapq
import math
from collections import Counter, deque
from functools import cache
from itertools import product
from typing import List, Optional


# 给你一个整数数组 nums ，判断是否存在三元组 [nums[i], nums[j], nums[k]] 满足 i != j、i != k 且 j != k ，同时还满足 nums[i] + nums[j] + nums[k] == 0 。请
#
# 你返回所有和为 0 且不重复的三元组。
#
# 注意：答案中不可以包含重复的三元组。
#
#  
#
#  
#
# 示例 1：
#
# 输入：nums = [-1,0,1,2,-1,-4]
# 输出：[[-1,-1,2],[-1,0,1]]
# 解释：
# nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0 。
# nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0 。
# nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0 。
# 不同的三元组是 [-1,0,1] 和 [-1,-1,2] 。
# 注意，输出的顺序和三元组的顺序并不重要。
# 示例 2：
#
# 输入：nums = [0,1,1]
# 输出：[]
# 解释：唯一可能的三元组和不为 0 。
#
#

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # c = {}
        # for x in nums:
        #     if x in c:
        #        c[x] += 1
        #     else:
        #         c[x] = 1
        # m = set()
        # nums.sort()
        # res = []
        #
        # for i in range(len(nums) - 1):
        #     for j in range(i+1, len(nums)):
        #         if (nums[i], nums[j]) not in m and (- nums[i] - nums[j]) in c:
        #             t = {}
        #             for x in [nums[i], nums[j], -nums[i] - nums[j]]:
        #                 if x in t:
        #                     t[x] += 1
        #                 else:
        #                     t[x] = 1
        #             r = True
        #             for x in t:
        #                 if c[x] < t[x]:
        #                     r = False
        #                     break
        #             if r:
        #                 res.append([nums[i], nums[j], - nums[i] - nums[j]])
        #                 m.add((nums[i], nums[j]))
        #                 m.add((nums[i], - nums[i] - nums[j]))
        #                 m.add((nums[j], - nums[i] - nums[j]))
        #                 m.add((nums[j], nums[i]))
        #                 m.add((- nums[i] - nums[j], nums[i]))
        #                 m.add((- nums[i] - nums[j], nums[i]))
        # return res

        n = len(nums)
        if not nums or n < 3:
            return []
        nums.sort()
        res = []
        for i in range(n):
            if nums[i] > 0:
                return res
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            L = i + 1
            R = n - 1
            while L < R:
                if nums[i] + nums[L] + nums[R] == 0:
                    res.append([nums[i], nums[L], nums[R]])
                    while L < R and nums[L] == nums[L + 1]:
                        L = L + 1
                    while L < R and nums[R] == nums[R - 1]:
                        R = R - 1
                    L = L + 1
                    R = R - 1
                elif nums[i] + nums[L] + nums[R] > 0:
                    R = R - 1
                else:
                    L = L + 1
        return res


if __name__ == "__main__":
    nums = [-4,-2,-2,-2,0,1,2,2,2,3,3,4,4,6,6]

    test = Solution().threeSum(nums)
    print(test)
