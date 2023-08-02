import heapq
import math
from collections import Counter
from typing import List, Optional


# 2475. 数组中不等三元组的数目
# 给你一个下标从 0 开始的正整数数组 nums 。请你找出并统计满足下述条件的三元组 (i, j, k) 的数目：
#
# 0 <= i < j < k < nums.length
# nums[i]、nums[j] 和 nums[k] 两两不同 。
# 换句话说：nums[i] != nums[j]、nums[i] != nums[k] 且 nums[j] != nums[k] 。
# 返回满足上述条件三元组的数目。
#
#
#
# 示例 1：
#
# 输入：nums = [4,4,2,4,3]
# 输出：3
# 解释：下面列出的三元组均满足题目条件：
# - (0, 2, 4) 因为 4 != 2 != 3
# - (1, 2, 4) 因为 4 != 2 != 3
# - (2, 3, 4) 因为 2 != 4 != 3
# 共计 3 个三元组，返回 3 。
# 注意 (2, 0, 4) 不是有效的三元组，因为 2 > 0 。
# 示例 2：
#
# 输入：nums = [1,1,1,1,1]
# 输出：0
# 解释：不存在满足条件的三元组，所以返回 0 。
#

class Solution:
    def unequalTriplets(self, nums: List[int]) -> int:
        c = {}
        cb = [0] * len(nums)

        for i in range(len(nums) - 1):
            if len(c) < 1:
                cb[i] = 0
            else:
                k = 0
                for x in c:
                    if x != nums[i]:
                        k += c[x]
                cb[i] = cb[i - 1] + k
            if nums[i] in c:
                c[nums[i]] += 1
            else:
                c[nums[i]] = 1

        c = {}
        ct = [0] * len(nums)

        for i in range(len(nums)):
            if len(c) < 2:
                ct[i] = 0
            else:
                k = 0
                if nums[i] in c:
                    for x in c:
                        if x != nums[i]:
                            k += c[x]*c[nums[i]]
                ct[i] = ct[i - 1] + cb[i - 1] - k
            if nums[i] in c:
                c[nums[i]] += 1
            else:
                c[nums[i]] = 1
        return ct[-1]



if __name__ == "__main__":
    nums = [1,2,3,4]

    test = Solution().unequalTriplets(nums)
    print(test)
