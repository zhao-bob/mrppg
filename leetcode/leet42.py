import heapq
import math
from collections import Counter, deque
from functools import cache
from itertools import product
from typing import List, Optional

# 42. 接雨水
# 给定 n 个非负整数表示每个宽度为 1 的柱子的高度图，计算按此排列的柱子，下雨之后能接多少雨水。
#
#
#
# 示例 1：
#
#
#
# 输入：height = [0,1,0,2,1,0,1,3,2,1,2,1]
# 输出：6
# 解释：上面是由数组 [0,1,0,2,1,0,1,3,2,1,2,1] 表示的高度图，在这种情况下，可以接 6 个单位的雨水（蓝色部分表示雨水）。
# 示例 2：
#
# 输入：height = [4,2,0,3,2,5]
# 输出：9
#

class Solution:
    def trap(self, height: List[int]) -> int:
        stk = []

        res = 0
        for i in range(len(height)):
            if stk and stk[-1][0] <= height[i]:
                a, k = stk.pop()
                while stk and stk[-1][0] <= height[i]:
                    b, k = stk.pop()
                    res += (b - a) * (i - k - 1)
                    a = b
                if stk:
                    res += (height[i] - a) * (i - stk[-1][1] - 1)
            stk.append((height[i], i))
        return res

if __name__ == "__main__":
    height = [6,2,0,3,2,5]

    test = Solution().trap(height)
    print(test)
