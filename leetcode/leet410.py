# 410. 分割数组的最大值
# 困难
# 相关标签
# 相关企业
# 给定一个非负整数数组 nums 和一个整数 k ，你需要将这个数组分成 k 个非空的连续子数组。
#
# 设计一个算法使得这 k 个子数组各自和的最大值最小。
#
#
#
# 示例 1：
#
# 输入：nums = [7,2,5,10,8], k = 2
# 输出：18
# 解释：
# 一共有四种方法将 nums 分割为 2 个子数组。
# 其中最好的方式是将其分为 [7,2,5] 和 [10,8] 。
# 因为此时这两个子数组各自的和的最大值为18，在所有情况中最小。
# 示例 2：
#
# 输入：nums = [1,2,3,4,5], k = 2
# 输出：9
# 示例 3：
#
# 输入：nums = [1,4,4], k = 3
# 输出：4
#
#
# 提示：
#
# 1 <= nums.length <= 1000
# 0 <= nums[i] <= 106
# 1 <= k <= min(50, nums.length)
#

import heapq
import math
from collections import Counter
from datetime import date
from typing import List, Optional


class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        n = len(nums)

        dp = [[math.inf] * n for _ in range(k)]
        dp[0][0] = nums[0]
        for i in range(1, n):
            dp[0][i] = dp[0][i - 1] + nums[i]

        for i in range(1, k):
            for j in range(i, n):
                for l in range(i, j + 1):
                    dp[i][j] = min(dp[i][j], max(dp[i - 1][l - 1], dp[0][j] - dp[0][l - 1]))

        return dp[-1][-1]


if __name__ == "__main__":
    nums = [7,2,5,10,8]
    k = 2

    test = Solution().splitArray(nums, k)

    print(test)
