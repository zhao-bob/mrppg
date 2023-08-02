import heapq
import math
from collections import Counter, deque
from functools import cache
from itertools import product
from typing import List, Optional

# 18. 四数之和
# 给你一个由 n 个整数组成的数组 nums ，和一个目标值 target 。请你找出并返回满足下述全部条件且不重复的四元组 [nums[a], nums[b], nums[c], nums[d]] （若两个四元组元素一一对应，则认为两个四元组重复）：
#
# 0 <= a, b, c, d < n
# a、b、c 和 d 互不相同
# nums[a] + nums[b] + nums[c] + nums[d] == target
# 你可以按 任意顺序 返回答案 。
#
#
#
# 示例 1：
#
# 输入：nums = [1,0,-1,0,-2,2], target = 0
# 输出：[[-2,-1,1,2],[-2,0,0,2],[-1,0,0,1]]
# 示例 2：
#
# 输入：nums = [2,2,2,2,2], target = 8
# 输出：[[2,2,2,2]]

class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        n = len(nums)
        if not nums or n < 4:
            return []
        nums.sort()
        res = []
        for i in range(n - 1):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            for j in range(i + 1, n):
                if j > i + 1 and nums[j] == nums[j - 1]:
                    continue
                a = nums[i] + nums[j]
                L = j + 1
                R = n - 1
                while L < R:
                    if a + nums[L] + nums[R] == target:
                        res.append([nums[i], nums[j], nums[L], nums[R]])
                        while L < R and nums[L] == nums[L + 1]:
                            L = L + 1
                        while L < R and nums[R] == nums[R - 1]:
                            R = R - 1
                        L = L + 1
                        R = R - 1
                    elif a + nums[L] + nums[R] > target:
                        R = R - 1
                    else:
                        L = L + 1
        return res


if __name__ == "__main__":
    nums = [-3,-2,-1,0,0,1,2,3]
    target = 0

    test = Solution().fourSum(nums, target)
    print(test)
