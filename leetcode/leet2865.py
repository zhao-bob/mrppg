# 2865. 美丽塔 I
# 中等
# 相关标签
# 相关企业
# 提示
# 给你一个长度为 n 下标从 0 开始的整数数组 maxHeights 。
#
# 你的任务是在坐标轴上建 n 座塔。第 i 座塔的下标为 i ，高度为 heights[i] 。
#
# 如果以下条件满足，我们称这些塔是 美丽 的：
#
# 1 <= heights[i] <= maxHeights[i]
# heights 是一个 山脉 数组。
# 如果存在下标 i 满足以下条件，那么我们称数组 heights 是一个 山脉 数组：
#
# 对于所有 0 < j <= i ，都有 heights[j - 1] <= heights[j]
# 对于所有 i <= k < n - 1 ，都有 heights[k + 1] <= heights[k]
# 请你返回满足 美丽塔 要求的方案中，高度和的最大值 。
#
#
#
# 示例 1：
#
# 输入：maxHeights = [5,3,4,1,1]
# 输出：13
# 解释：和最大的美丽塔方案为 heights = [5,3,3,1,1] ，这是一个美丽塔方案，因为：
# - 1 <= heights[i] <= maxHeights[i]
# - heights 是个山脉数组，峰值在 i = 0 处。
# 13 是所有美丽塔方案中的最大高度和。
# 示例 2：
#
# 输入：maxHeights = [6,5,3,9,2,7]
# 输出：22
# 解释： 和最大的美丽塔方案为 heights = [3,3,3,9,2,2] ，这是一个美丽塔方案，因为：
# - 1 <= heights[i] <= maxHeights[i]
# - heights 是个山脉数组，峰值在 i = 3 处。
# 22 是所有美丽塔方案中的最大高度和。
# 示例 3：
#
# 输入：maxHeights = [3,2,5,5,2,3]
# 输出：18
# 解释：和最大的美丽塔方案为 heights = [2,2,5,5,2,2] ，这是一个美丽塔方案，因为：
# - 1 <= heights[i] <= maxHeights[i]
# - heights 是个山脉数组，最大值在 i = 2 处。
# 注意，在这个方案中，i = 3 也是一个峰值。
# 18 是所有美丽塔方案中的最大高度和。
#
#
# 提示：
#
# 1 <= n == maxHeights <= 103
# 1 <= maxHeights[i] <= 109
#

import heapq
import math
from collections import Counter
from datetime import date
from typing import List, Optional


class Solution:
    def maximumSumOfHeights(self, maxHeights: List[int]) -> int:
        n = len(maxHeights)
        lh = [0] * n
        stk = []

        for i in range(n):
            while stk and maxHeights[stk[-1]] > maxHeights[i]:
                stk.pop()
            if stk:
                lh[i] = lh[stk[-1]] + maxHeights[i] * (i - stk[-1])
            else:
                lh[i] = maxHeights[i] * (i + 1)
            stk.append(i)

        rh = [0] * n

        stk = []
        res = 0
        for i in range(n - 1, -1, -1):
            while stk and maxHeights[stk[-1]] > maxHeights[i]:
                stk.pop()
            if stk:
                rh[i] = rh[stk[-1]] + maxHeights[i] * (stk[-1] - i)
            else:
                rh[i] = maxHeights[i] * (n - i)
            res = max(res, lh[i] + rh[i] - maxHeights[i])
            stk.append(i)

        return res



if __name__ == "__main__":
    maxHeights = [5,3,4,1,1]

    test = Solution().maximumSumOfHeights(maxHeights)

    print(test)
