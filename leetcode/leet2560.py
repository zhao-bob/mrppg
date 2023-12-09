import collections
import heapq
import math
from bisect import bisect_right
from collections import Counter, deque
from functools import cache
from itertools import product
from typing import List, Optional


# 2560. 打家劫舍 IV
# 提示
# 中等
# 106
# 相关企业
# 沿街有一排连续的房屋。每间房屋内都藏有一定的现金。现在有一位小偷计划从这些房屋中窃取现金。
#
# 由于相邻的房屋装有相互连通的防盗系统，所以小偷 不会窃取相邻的房屋 。
#
# 小偷的 窃取能力 定义为他在窃取过程中能从单间房屋中窃取的 最大金额 。
#
# 给你一个整数数组 nums 表示每间房屋存放的现金金额。形式上，从左起第 i 间房屋中放有 nums[i] 美元。
#
# 另给你一个整数 k ，表示窃贼将会窃取的 最少 房屋数。小偷总能窃取至少 k 间房屋。
#
# 返回小偷的 最小 窃取能力。
#
#
#
# 示例 1：
#
# 输入：nums = [2,3,5,9], k = 2
# 输出：5
# 解释：
# 小偷窃取至少 2 间房屋，共有 3 种方式：
# - 窃取下标 0 和 2 处的房屋，窃取能力为 max(nums[0], nums[2]) = 5 。
# - 窃取下标 0 和 3 处的房屋，窃取能力为 max(nums[0], nums[3]) = 9 。
# - 窃取下标 1 和 3 处的房屋，窃取能力为 max(nums[1], nums[3]) = 9 。
# 因此，返回 min(5, 9, 9) = 5 。
# 示例 2：
#
# 输入：nums = [2,7,9,3,1], k = 2
# 输出：2
# 解释：共有 7 种窃取方式。窃取能力最小的情况所对应的方式是窃取下标 0 和 4 处的房屋。返回 max(nums[0], nums[4]) = 2 。

class Solution:
    def minCapability(self, nums: List[int], k: int) -> int:
        l = min(nums)
        r = max(nums)

        while l < r:
            m = (l + r) // 2
            f1 = 0
            f2 = 0
            n = 0
            for i in range(len(nums)):
                if nums[i] <= m:
                    n = max(f1, f2 + 1)
                else:
                    n = f1
                f2 = f1
                f1 = n
            if n >= k:
                r = m
            else:
                l = m + 1
        return l


if __name__ == "__main__":
    nums = [2, 7, 9, 3, 1]
    k = 2

    test = Solution().minCapability(nums, k)

    print(test)
