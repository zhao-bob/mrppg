# 2369. 检查数组是否存在有效划分
# 中等
# 相关标签
# 相关企业
# 提示
# 给你一个下标从 0 开始的整数数组 nums ，你必须将数组划分为一个或多个 连续 子数组。
#
# 如果获得的这些子数组中每个都能满足下述条件 之一 ，则可以称其为数组的一种 有效 划分：
#
# 子数组 恰 由 2 个相等元素组成，例如，子数组 [2,2] 。
# 子数组 恰 由 3 个相等元素组成，例如，子数组 [4,4,4] 。
# 子数组 恰 由 3 个连续递增元素组成，并且相邻元素之间的差值为 1 。例如，子数组 [3,4,5] ，但是子数组 [1,3,5] 不符合要求。
# 如果数组 至少 存在一种有效划分，返回 true ，否则，返回 false 。
#
#
#
# 示例 1：
#
# 输入：nums = [4,4,4,5,6]
# 输出：true
# 解释：数组可以划分成子数组 [4,4] 和 [4,5,6] 。
# 这是一种有效划分，所以返回 true 。
# 示例 2：
#
# 输入：nums = [1,1,1,2]
# 输出：false
# 解释：该数组不存在有效划分。
#
#
# 提示：
#
# 2 <= nums.length <= 105
# 1 <= nums[i] <= 106
#

import heapq
import math
from collections import Counter, deque, defaultdict
from datetime import date
from functools import cache
from typing import List, Optional

from sortedcontainers import SortedList


class Solution:
    def validPartition(self, nums: List[int]) -> bool:
        # count = Counter(nums)
        #
        # def partition():
        #     for c in count:
        #         if count[c] == 1:
        #             a = c
        #             break
        #     else:
        #         return True
        #     if a - 2 in count and a - 1 in count and count[a - 2] > 0 and count[a - 1] > 0 \
        #             or a - 1 in count and a + 1 in count and count[a - 1] > 0 and count[a + 1] > 0 \
        #             or a + 1 in count and a + 2 in count and count[a + 1] > 0 and count[a + 2] > 0:
        #         count[a] -= 1
        #         if a - 2 in count and a - 1 in count and count[a - 2] > 0 and count[a - 1] > 0:
        #             count[a - 2] -= 1
        #             count[a - 1] -= 1
        #             if partition():
        #                 return True
        #             count[a - 2] += 1
        #             count[a - 1] += 1
        #         if a - 1 in count and a + 1 in count and count[a - 1] > 0 and count[a + 1] > 0:
        #             count[a - 1] -= 1
        #             count[a + 1] -= 1
        #             if partition():
        #                 return True
        #             count[a - 1] += 1
        #             count[a + 1] += 1
        #         if a + 1 in count and a + 2 in count and count[a + 1] > 0 and count[a + 2] > 0:
        #             count[a + 1] -= 1
        #             count[a + 2] -= 1
        #             if partition():
        #                 return True
        #             count[a + 1] += 1
        #             count[a + 2] += 1
        #         count[a] += 1
        #         return False
        #     else:
        #         return False

        # return partition()

        # stk = []
        # c = Counter(nums)
        # v = 0
        # start = True
        # i = 0
        # n = len(nums)
        # while i < n:
        #     if c[nums[i]] != 2:
        #         if c[nums[i]] != 1:
        #             if start:
        #                 v += 1
        #         else:
        #             if start:
        #                 start = False
        #         if len(stk) == 0:
        #             stk.append(nums[i])
        #         else:
        #             if stk[-1] == nums[i] - 1:
        #                 stk.append(nums[i])
        #             else:
        #                 if len(stk) > 1:
        #                     if len(stk) == 2:
        #                         if not start and c[stk[-1]] != 1:
        #                             v += 1
        #                     else:
        #                         if not start:
        #                             if c[stk[-1]] != 1:
        #                                 v += 1
        #                             if c[stk[-2]] != 1:
        #                                 v += 1
        #                 if len(stk) % 3 == 0 or v > 1 or (len(stk) % 3 - v) % 3 == 0:
        #                     stk.clear()
        #                     stk.append(nums[i])
        #                     start = True
        #                     v = 0
        #                 else:
        #                     return False
        #     else:
        #         if len(stk) > 1:
        #             if len(stk) == 2:
        #                 if not start and c[stk[-1]] != 1:
        #                     v += 1
        #             else:
        #                 if not start:
        #                     if c[stk[-1]] != 1:
        #                         v += 1
        #                     if c[stk[-2]] != 1:
        #                         v += 1
        #         if len(stk) % 3 == 0 or v > 1 or (len(stk) % 3 - v) % 3 == 0:
        #             stk.clear()
        #             stk.append(nums[i])
        #             start = True
        #             v = 0
        #         else:
        #             return False
        #     i += c[nums[i]]
        # if len(stk) > 1:
        #     if len(stk) == 2:
        #         if not start and c[stk[-1]] != 1:
        #             v += 1
        #     else:
        #         if not start:
        #             if c[stk[-1]] != 1:
        #                 v += 1
        #             if c[stk[-2]] != 1:
        #                 v += 1
        # if len(stk) % 3 == 0 or v > 1 or (len(stk) % 3 - v) % 3 == 0:
        #     return True
        # else:
        #     return False
        n = len(nums)
        dp = [False] * (n + 1)
        dp[0] = True

        for i in range(1, n):
            if nums[i] == nums[i - 1]:
                dp[i + 1] = dp[i - 1]
                if i - 2 >= 0 and nums[i] == nums[i - 2]:
                    dp[i + 1] |= dp[i - 2]
            else:
                if i - 2 >= 0 and nums[i] == nums[i - 1] + 1 and nums[i] == nums[i - 2] + 2:
                    dp[i + 1] = dp[i - 2]
                else:
                    dp[i + 1] = False
        return dp[-1]

if __name__ == "__main__":
    nums = [4,4,4,5,6,7,8,9,9,10,10,10]
    test = Solution().validPartition(nums)
    print(test)
