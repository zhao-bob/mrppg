import heapq
import math
from collections import Counter
from typing import List
from sortedcontainers import SortedList


# 260. 只出现一次的数字 III
# 中等
# 759
# 相关企业
# 给你一个整数数组 nums，其中恰好有两个元素只出现一次，其余所有元素均出现两次。 找出只出现一次的那两个元素。你可以按 任意顺序 返回答案。
#
# 你必须设计并实现线性时间复杂度的算法且仅使用常量额外空间来解决此问题。
#
#
#
# 示例 1：
#
# 输入：nums = [1,2,1,3,2,5]
# 输出：[3,5]
# 解释：[5, 3] 也是有效的答案。
# 示例 2：
#
# 输入：nums = [-1,0]
# 输出：[-1,0]
# 示例 3：
#
# 输入：nums = [0,1]
# 输出：[1,0]
#


class Solution:
    def singleNumber(self, nums: List[int]) -> list[int]:
        xorsum = 0
        for num in nums:
            xorsum ^= num

        lsb = xorsum & (-xorsum)
        type1 = type2 = 0
        for num in nums:
            if num & lsb:
                type1 ^= num
            else:
                type2 ^= num

        return [type1, type2]


if __name__ == "__main__":
    nums = [1,2,1,3,2,5]
    test = Solution().singleNumber(nums)
    print(test)
