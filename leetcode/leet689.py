import heapq
import math
from collections import Counter, deque, defaultdict
from functools import cache, reduce
from itertools import product
from typing import List, Optional


# 689. 三个无重叠子数组的最大和
# 困难
# 373
# 相关企业
# 给你一个整数数组 nums 和一个整数 k ，找出三个长度为 k 、互不重叠、且全部数字和（3 * k 项）最大的子数组，并返回这三个子数组。
#
# 以下标的数组形式返回结果，数组中的每一项分别指示每个子数组的起始位置（下标从 0 开始）。如果有多个结果，返回字典序最小的一个。
#
#
#
# 示例 1：
#
# 输入：nums = [1,2,1,2,6,7,5,1], k = 2
# 输出：[0,3,5]
# 解释：子数组 [1, 2], [2, 6], [7, 5] 对应的起始下标为 [0, 3, 5]。
# 也可以取 [2, 1], 但是结果 [1, 3, 5] 在字典序上更大。
# 示例 2：
#
# 输入：nums = [1,2,1,2,1,2,1,2,1], k = 2
# 输出：[0,2,4]
#
#
class Solution:
    def maxSumOfThreeSubarrays(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        subsum = [0] * n
        dp = [[0] * n for _ in range(3)]
        s1 = [0] * n

        for i in range(k - 1, n):
            subsum[i] = sum(nums[i + 1 - k: i + 1])
            if dp[0][i - 1] < subsum[i]:
                dp[0][i] = subsum[i]
                s1[i] = i
            else:
                dp[0][i] = dp[0][i - 1]
                s1[i] = s1[i - 1]
        s2 = [(0, 0)] * n
        for i in range(2 * k - 1, n):
            if dp[1][i - 1] < dp[0][i - k] + subsum[i]:
                dp[1][i] = dp[0][i - k] + subsum[i]
                s2[i] = (s1[i - k], i)
            else:
                dp[1][i] = dp[1][i - 1]
                s2[i] = s2[i - 1]
        s3 = [(0, 0, 0)] * n
        for i in range(3 * k - 1, n):
            if dp[2][i - 1] < dp[1][i - k] + subsum[i]:
                dp[2][i] = dp[1][i - k] + subsum[i]
                s3[i] = s2[i - k] + (i,)
            else:
                dp[2][i] = dp[2][i - 1]
                s3[i] = s3[i - 1]
        return [i - k + 1 for i in s3[-1]]


if __name__ == "__main__":
    nums = [1,2,1,2,6,7,5,1]
    k = 2

    test = Solution().maxSumOfThreeSubarrays(nums, k)

    print(test)
