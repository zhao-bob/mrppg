# 2809. 使数组和小于等于 x 的最少时间
# 困难
# 相关标签
# 相关企业
# 提示
# 给你两个长度相等下标从 0 开始的整数数组 nums1 和 nums2 。每一秒，对于所有下标 0 <= i < nums1.length ，nums1[i] 的值都增加 nums2[i] 。操作 完成后 ，你可以进行如下操作：
#
# 选择任一满足 0 <= i < nums1.length 的下标 i ，并使 nums1[i] = 0 。
# 同时给你一个整数 x 。
#
# 请你返回使 nums1 中所有元素之和 小于等于 x 所需要的 最少 时间，如果无法实现，那么返回 -1 。
#
#
#
# 示例 1：
#
# 输入：nums1 = [1,2,3], nums2 = [1,2,3], x = 4
# 输出：3
# 解释：
# 第 1 秒，我们对 i = 0 进行操作，得到 nums1 = [0,2+2,3+3] = [0,4,6] 。
# 第 2 秒，我们对 i = 1 进行操作，得到 nums1 = [0+1,0,6+3] = [1,0,9] 。
# 第 3 秒，我们对 i = 2 进行操作，得到 nums1 = [1+1,0+2,0] = [2,2,0] 。
# 现在 nums1 的和为 4 。不存在更少次数的操作，所以我们返回 3 。
# 示例 2：
#
# 输入：nums1 = [1,2,3], nums2 = [3,3,3], x = 4
# 输出：-1
# 解释：不管如何操作，nums1 的和总是会超过 x 。
#
#
# 提示：
#
# 1 <= nums1.length <= 103
# 1 <= nums1[i] <= 103
# 0 <= nums2[i] <= 103
# nums1.length == nums2.length
# 0 <= x <= 106
#

import heapq
import math
from collections import Counter
from datetime import date
from typing import List, Optional


class Solution:
    def minimumTime(self, nums1: List[int], nums2: List[int], x: int) -> int:
        n = len(nums1)
        s2 = sum(nums2)
        s1 = sum(nums1)
        sn1 = sorted([(n, i) for i, n in enumerate(nums2)])
        s = s1
        dp = [[0] * (n + 1) for _ in range(n + 1)]
        if s <= x:
            return 0

        for k in range(1, n + 1):
            for i in range(k, n + 1):
                dp[k][i] = max(dp[k][i - 1], dp[k - 1][i - 1] + sn1[i - 1][0] * k + nums1[sn1[i - 1][1]])

        for k in range(1, n + 1):
            s += s2
            if s - dp[k][-1] <= x:
                return k
        return -1


if __name__ == "__main__":
    nums1 = [6,5,2,8,8,1,6,4]
    nums2 = [1,2,1,0,1,0,3,1]
    x = 23

    test = Solution().minimumTime(nums1, nums2, x)

    print(test)
