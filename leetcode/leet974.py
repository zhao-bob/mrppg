# 974. 和可被 K 整除的子数组
# 中等
# 相关标签
# 相关企业
# 给定一个整数数组 nums 和一个整数 k ，返回其中元素之和可被 k 整除的（连续、非空） 子数组 的数目。
#
# 子数组 是数组的 连续 部分。
#
#
#
# 示例 1：
#
# 输入：nums = [4,5,0,-2,-3,1], k = 5
# 输出：7
# 解释：
# 有 7 个子数组满足其元素之和可被 k = 5 整除：
# [4, 5, 0, -2, -3, 1], [5], [5, 0], [5, 0, -2, -3], [0], [0, -2, -3], [-2, -3]
# 示例 2:
#
# 输入: nums = [5], k = 9
# 输出: 0
#
#
# 提示:
#
# 1 <= nums.length <= 3 * 104
# -104 <= nums[i] <= 104
# 2 <= k <= 104
#

import heapq
import math
from collections import Counter, deque, defaultdict
from datetime import date
from functools import cache
from typing import List, Optional

from sortedcontainers import SortedList

class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        n = len(nums)
        s = [0] * n
        s[0] = nums[0] % k

        for i in range(1, n):
            s[i] = (s[i - 1] + nums[i]) % k

        cs = Counter(s)

        res = 0
        a = 0
        for i in range(n):
            if a in cs:
                res += cs[a]
            cs[s[i]] -= 1
            a = s[i]
        return res

if __name__ == "__main__":
    nums = [4,5,0,-2,-3,1]
    k = 5
    test = Solution().subarraysDivByK(nums, k)
    print(test)
