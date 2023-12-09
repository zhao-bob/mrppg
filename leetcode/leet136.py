import heapq
import math
from collections import Counter
from typing import List
from sortedcontainers import SortedList


# 136. 只出现一次的数字
# 简单
# 3K
# 相关企业
# 给你一个 非空 整数数组 nums ，除了某个元素只出现一次以外，其余每个元素均出现两次。找出那个只出现了一次的元素。
#
# 你必须设计并实现线性时间复杂度的算法来解决此问题，且该算法只使用常量额外空间。
#
#
#
# 示例 1 ：
#
# 输入：nums = [2,2,1]
# 输出：1
# 示例 2 ：
#
# 输入：nums = [4,1,2,1,2]
# 输出：4
# 示例 3 ：
#
# 输入：nums = [1]
# 输出：1
#


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        single = 0
        for n in nums:
            single ^= n
        return single


if __name__ == "__main__":
    nums = list(range(100000)) + list(range(100000, -1, -1))
    test = Solution().singleNumber(nums)
    print(test)
