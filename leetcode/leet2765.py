# 2765. 最长交替子数组
# 简单
# 相关标签
# 相关企业
# 提示
# 给你一个下标从 0 开始的整数数组 nums 。如果 nums 中长度为 m 的子数组 s 满足以下条件，我们称它是一个 交替子数组 ：
#
# m 大于 1 。
# s1 = s0 + 1 。
# 下标从 0 开始的子数组 s 与数组 [s0, s1, s0, s1,...,s(m-1) % 2] 一样。也就是说，s1 - s0 = 1 ，s2 - s1 = -1 ，s3 - s2 = 1 ，s4 - s3 = -1 ，以此类推，直到 s[m - 1] - s[m - 2] = (-1)m 。
# 请你返回 nums 中所有 交替 子数组中，最长的长度，如果不存在交替子数组，请你返回 -1 。
#
# 子数组是一个数组中一段连续 非空 的元素序列。
#
#
#
# 示例 1：
#
# 输入：nums = [2,3,4,3,4]
# 输出：4
# 解释：交替子数组有 [3,4] ，[3,4,3] 和 [3,4,3,4] 。最长的子数组为 [3,4,3,4] ，长度为4 。
# 示例 2：
#
# 输入：nums = [4,5,6]
# 输出：2
# 解释：[4,5] 和 [5,6] 是仅有的两个交替子数组。它们长度都为 2 。
#
#
# 提示：
#
# 2 <= nums.length <= 100
# 1 <= nums[i] <= 104
#

import heapq
import math
from collections import Counter
from datetime import date
from typing import List, Optional


class Solution:
    def alternatingSubarray(self, nums: List[int]) -> int:
        res = -1
        i = 0
        n = len(nums)
        while i < n - 1:
            if nums[i + 1] - nums[i] == 1:
                k = 2
                j = i + 2
                while j < n:
                    if (j - i) % 2 == 0 and nums[j] == nums[i] or (j - i) % 2 == 1 and nums[j] == nums[i + 1]:
                        k += 1
                        j += 1
                    else:
                        break
                res = max(res, k)
                i = j - 1
            else:
                i += 1
        return res



if __name__ == "__main__":
    nums = [4,5,6,5,4]

    test = Solution().alternatingSubarray(nums)

    print(test)
