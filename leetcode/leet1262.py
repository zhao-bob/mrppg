import heapq
import math
from collections import Counter
from typing import List, Optional


# 1262. 可被三整除的最大和
# 给你一个整数数组 nums，请你找出并返回能被三整除的元素最大和。
#
#
#
# 示例 1：
#
# 输入：nums = [3,6,5,1,8]
# 输出：18
# 解释：选出数字 3, 6, 1 和 8，它们的和是 18（可被 3 整除的最大和）。
# 示例 2：
#
# 输入：nums = [4]
# 输出：0
# 解释：4 不能被 3 整除，所以无法选出数字，返回 0。
# 示例 3：
#
# 输入：nums = [1,2,3,4,4]
# 输出：12
# 解释：选出数字 1, 3, 4 以及 4，它们的和是 12（可被 3 整除的最大和）。
#

class Solution:
    def maxSumDivThree(self, nums: List[int]) -> int:
        m = [math.inf, math.inf, math.inf]
        s = 0
        for x in nums:
            s += x
            if x % 3 == 0:
                m[0] = min(m[0], x)
            elif x % 3 == 1:
                m[2] = min(m[2], m[1] + x)
                m[1] = min(m[1], x)
                m[0] = min(m[0], m[1] + m[2])
            else:
                m[1] = min(m[1], m[2] + x)
                m[2] = min(m[2], x)
                m[0] = min(m[0], m[1] + m[2])
        m[0] = 0
        return s - m[s % 3]


if __name__ == "__main__":
    nums = [1,2,3,4,4]

    test = Solution().maxSumDivThree(nums)
    print(test)
