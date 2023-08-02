import math
from bisect import bisect_right, bisect_left
from collections import defaultdict
from functools import lru_cache
from random import randint
from typing import List, Optional


# 1043. 分隔数组以得到最大和
# 给你一个整数数组 arr，请你将该数组分隔为长度 最多 为 k 的一些（连续）子数组。分隔完成后，每个子数组的中的所有值都会变为该子数组中的最大值。
#
# 返回将数组分隔变换后能够得到的元素最大和。本题所用到的测试用例会确保答案是一个 32 位整数。
#
#
#
# 示例 1：
#
# 输入：arr = [1,15,7,9,2,5,10], k = 3
# 输出：84
# 解释：数组变为 [15,15,15,9,10,10,10]
# 示例 2：
#
# 输入：arr = [1,4,1,5,7,3,6,1,9,9,3], k = 4
# 输出：83
# 示例 3：
#
# 输入：arr = [1], k = 1
# 输出：1
#

class Solution:
    def maxSumAfterPartitioning(self, arr: List[int], k: int) -> int:
        dp = [0] * (len(arr) + 1)
        for i in range(1, len(arr) + 1):
            a = 0 if i - k < 0 else i - k
            for j in range(a, i):
                dp[i] = max(dp[i], dp[j] + max(arr[j:i]) * (i - j))
        return dp[-1]


if __name__ == "__main__":
    arr = [1]
    k = 1

    test = Solution().maxSumAfterPartitioning(arr, k)
    print(test)
