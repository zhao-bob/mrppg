import heapq
import math
from collections import Counter
from functools import cache
from typing import List, Optional
from sortedcontainers import SortedList


# 907. 子数组的最小值之和
# 中等
# 697
# 相关企业
# 给定一个整数数组 arr，找到 min(b) 的总和，其中 b 的范围为 arr 的每个（连续）子数组。
#
# 由于答案可能很大，因此 返回答案模 10^9 + 7 。
#
#
#
# 示例 1：
#
# 输入：arr = [3,1,2,4]
# 输出：17
# 解释：
# 子数组为 [3]，[1]，[2]，[4]，[3,1]，[1,2]，[2,4]，[3,1,2]，[1,2,4]，[3,1,2,4]。
# 最小值为 3，1，2，4，1，1，2，1，1，1，和为 17。
# 示例 2：
#
# 输入：arr = [11,81,94,43,3]
# 输出：444
#
#
# 提示：
#
# 1 <= arr.length <= 3 * 104
# 1 <= arr[i] <= 3 * 104
#


class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        # stk = []
        # n = len(arr)
        # res = 0
        # for i in range(n - 1, -1, -1):
        #     c = arr[i]
        #     while stk and stk[-1][0] >= arr[i]:
        #         stk.pop()
        #     if stk:
        #         c += (stk[-1][1] - i - 1) * arr[i] + stk[-1][2]
        #     else:
        #         c += (n - 1 - i) * arr[i]
        #     res += c
        #     stk.append((arr[i], i, c))
        # return res % (10 ** 9 + 7)
        stk = []
        n = len(arr)
        res = 0
        for i in range(n - 1, -1, -1):
            c = arr[i]
            while stk and arr[stk[-1][0]] >= arr[i]:
                stk.pop()
            if stk:
                c += (stk[-1][0] - i - 1) * arr[i] + stk[-1][1]
            else:
                c += (n - 1 - i) * arr[i]
            res += c
            stk.append((i, c))
        return res % (10 ** 9 + 7)




if __name__ == "__main__":
    arr = [11,81,94,43,3]
    test = Solution().sumSubarrayMins(arr)
    print(test)
