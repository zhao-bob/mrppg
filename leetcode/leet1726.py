import heapq
import math
from collections import Counter
from typing import List
from sortedcontainers import SortedList


# 1726. 同积元组
# 提示
# 中等
# 45
# 相关企业
# 给你一个由 不同 正整数组成的数组 nums ，请你返回满足 a * b = c * d 的元组 (a, b, c, d) 的数量。其中 a、b、c 和 d 都是 nums 中的元素，且 a != b != c != d 。
#
#
#
# 示例 1：
#
# 输入：nums = [2,3,4,6]
# 输出：8
# 解释：存在 8 个满足题意的元组：
# (2,6,3,4) , (2,6,4,3) , (6,2,3,4) , (6,2,4,3)
# (3,4,2,6) , (4,3,2,6) , (3,4,6,2) , (4,3,6,2)
# 示例 2：
#
# 输入：nums = [1,2,4,5,10]
# 输出：16
# 解释：存在 16 个满足题意的元组：
# (1,10,2,5) , (1,10,5,2) , (10,1,2,5) , (10,1,5,2)
# (2,5,1,10) , (2,5,10,1) , (5,2,1,10) , (5,2,10,1)
# (2,10,4,5) , (2,10,5,4) , (10,2,4,5) , (10,2,4,5)
# (4,5,2,10) , (4,5,10,2) , (5,4,2,10) , (5,4,10,2)
#


class Solution:
    def tupleSameProduct(self, nums: List[int]) -> int:
        t = {}
        res = 0
        for i in range(len(nums) - 1):
            for j in range(i + 1, len(nums)):
                a = nums[i] * nums[j]
                if a in t:
                    res += 8 * t[a]
                    t[a] += 1
                else:
                    t[a] = 1
        return res



if __name__ == "__main__":
    nums = [1,2,4,5,10]
    test = Solution().tupleSameProduct(nums)
    print(test)
