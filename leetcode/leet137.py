import heapq
import math
from collections import Counter
from typing import List
from sortedcontainers import SortedList


# 137. 只出现一次的数字 II
# 中等
# 1.1K
# 相关企业
# 给你一个整数数组 nums ，除某个元素仅出现 一次 外，其余每个元素都恰出现 三次 。请你找出并返回那个只出现了一次的元素。
#
# 你必须设计并实现线性时间复杂度的算法且使用常数级空间来解决此问题。
#
#
#
# 示例 1：
#
# 输入：nums = [2,2,3,2]
# 输出：3
# 示例 2：
#
# 输入：nums = [0,1,0,1,0,1,99]
# 输出：99
#


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        a = b = 0
        for num in nums:
            b = ~a & (b ^ num)
            a = ~b & (a ^ num)
        return b


if __name__ == "__main__":
    nums = [2,1,2,1,2,1,97]
    test = Solution().singleNumber(nums)
    print(test)
