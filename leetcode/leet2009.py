# 2009. 使数组连续的最少操作数
# 困难
# 相关标签
# 相关企业
# 提示
# 给你一个整数数组 nums 。每一次操作中，你可以将 nums 中 任意 一个元素替换成 任意 整数。
#
# 如果 nums 满足以下条件，那么它是 连续的 ：
#
# nums 中所有元素都是 互不相同 的。
# nums 中 最大 元素与 最小 元素的差等于 nums.length - 1 。
# 比方说，nums = [4, 2, 5, 3] 是 连续的 ，但是 nums = [1, 2, 3, 5, 6] 不是连续的 。
#
# 请你返回使 nums 连续 的 最少 操作次数。
#
#
#
# 示例 1：
#
# 输入：nums = [4,2,5,3]
# 输出：0
# 解释：nums 已经是连续的了。
# 示例 2：
#
# 输入：nums = [1,2,3,5,6]
# 输出：1
# 解释：一个可能的解是将最后一个元素变为 4 。
# 结果数组为 [1,2,3,5,4] ，是连续数组。
# 示例 3：
#
# 输入：nums = [1,10,100,1000]
# 输出：3
# 解释：一个可能的解是：
# - 将第二个元素变为 2 。
# - 将第三个元素变为 3 。
# - 将第四个元素变为 4 。
# 结果数组为 [1,2,3,4] ，是连续数组。
#
#
# 提示：
#
# 1 <= nums.length <= 105
# 1 <= nums[i] <= 109
#

import heapq
import math
from collections import Counter, deque, defaultdict
from datetime import date
from functools import cache
from typing import List, Optional

from sortedcontainers import SortedList

class Solution:
    def minOperations(self, nums: List[int]) -> int:
        ss = sorted(set(nums))
        n = len(ss)
        total = len(nums)

        def bisect(k):
            left = 0
            right = n - 1

            while left <= right:
                mid = (left + right) // 2
                if ss[mid] < k:
                    left = mid + 1
                elif ss[mid] > k:
                    right = mid - 1
                else:
                    return mid + 1
            return left

        res = n - 1
        for i in range(n - 1):
            p = bisect(ss[i] + total - 1)
            res = min(res, total + i - p)
        return res

if __name__ == "__main__":
    nums = [8,10,16,18,10,10,16,13,13,16]
    test = Solution().minOperations(nums)
    print(test)
