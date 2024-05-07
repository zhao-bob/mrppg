# 1793. 好子数组的最大分数
# 困难
# 相关标签
# 相关企业
# 提示
# 给你一个整数数组 nums （下标从 0 开始）和一个整数 k 。
#
# 一个子数组 (i, j) 的 分数 定义为 min(nums[i], nums[i+1], ..., nums[j]) * (j - i + 1) 。一个 好 子数组的两个端点下标需要满足 i <= k <= j 。
#
# 请你返回 好 子数组的最大可能 分数 。
#
#
#
# 示例 1：
#
# 输入：nums = [1,4,3,7,4,5], k = 3
# 输出：15
# 解释：最优子数组的左右端点下标是 (1, 5) ，分数为 min(4,3,7,4,5) * (5-1+1) = 3 * 5 = 15 。
# 示例 2：
#
# 输入：nums = [5,5,4,5,4,1,1,1], k = 0
# 输出：20
# 解释：最优子数组的左右端点下标是 (0, 4) ，分数为 min(5,5,4,5,4) * (4-0+1) = 4 * 5 = 20 。
#
#
# 提示：
#
# 1 <= nums.length <= 105
# 1 <= nums[i] <= 2 * 104
# 0 <= k < nums.length
#

import heapq
import math
from collections import Counter, deque, defaultdict
from datetime import date
from functools import cache
from typing import List, Optional

from sortedcontainers import SortedList


class Solution:
    def maximumScore(self, nums: List[int], k: int) -> int:
        n = len(nums)
        ls = []
        rs = []
        i = 0
        while i <= k:
            a = i
            while ls:
                if ls[-1][0] > nums[i]:
                    a = ls[-1][1]
                    ls.pop()
                else:
                    break
            ls.append((nums[i], a))
            i += 1

        i = n - 1
        while i >= k:
            a = i
            while rs:
                if rs[-1][0] > nums[i]:
                    a = rs[-1][1]
                    rs.pop()
                else:
                    break
            rs.append((nums[i], a))
            i -= 1

        res = nums[k]
        j = 0
        for i in ls:
            a = i[0]
            while j < len(rs) and a > rs[j][0]:
                j += 1
            if j < len(rs):
                res = max(res, a * (rs[j][1] - i[1] + 1))
            else:
                res = max(res, a * (k - i[1] + 1))

        j = 0
        for i in rs:
            a = i[0]
            while j < len(ls) and a > ls[j][0]:
                j += 1
            if j < len(ls):
                res = max(res, a * (i[1] - ls[j][1] + 1))
            else:
                res = max(res, a * (i[1] - k + 1))
        return res


if __name__ == "__main__":
    nums = [1, 4, 3, 7, 4, 5]
    k = 2

    test = Solution().maximumScore(nums, k)

    print(test)
