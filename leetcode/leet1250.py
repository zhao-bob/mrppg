import collections
import heapq
import math
from bisect import bisect_right, bisect_left
from collections import Counter, deque
from functools import cache
from itertools import product
from typing import List, Optional


# 1250. 检查「好数组」
# 提示
# 困难
# 130
# 相关企业
# 给你一个正整数数组 nums，你需要从中任选一些子集，然后将子集中每一个数乘以一个 任意整数，并求出他们的和。
#
# 假如该和结果为 1，那么原数组就是一个「好数组」，则返回 True；否则请返回 False。
#
#
#
# 示例 1：
#
# 输入：nums = [12,5,7,23]
# 输出：true
# 解释：挑选数字 5 和 7。
# 5*3 + 7*(-2) = 1
# 示例 2：
#
# 输入：nums = [29,6,10]
# 输出：true
# 解释：挑选数字 29, 6 和 10。
# 29*1 + 6*(-3) + 10*(-1) = 1
# 示例 3：
#
# 输入：nums = [3,6]
# 输出：false

class Solution:
    def isGoodArray(self, nums: List[int]) -> bool:
        s = set(nums)
        mn = min(s)
        if len(s) == 1 and mn > 1:
            return False
        while mn > 1:
            s1 = set()
            s1.add(mn)
            for x in s:
                if x % mn != 0:
                    s1.add(x % mn)
            s = s1
            mn = min(s)
            if len(s) == 1 and mn > 1:
                return False
        return True


if __name__ == "__main__":
    nums = [9, 11]
    test = Solution().isGoodArray(nums)
    print(test)
