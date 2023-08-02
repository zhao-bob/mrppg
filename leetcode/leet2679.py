import heapq
import math
from collections import Counter, deque
from functools import cache
from itertools import product
from typing import List, Optional


# 445. 两数相加 II
# 给你两个 非空 链表来代表两个非负整数。数字最高位位于链表开始位置。它们的每个节点只存储一位数字。将这两数相加会返回一个新的链表。
#
# 你可以假设除了数字 0 之外，这两个数字都不会以零开头。
#
#
#
# 示例1：
#
#
#
# 输入：l1 = [7,2,4,3], l2 = [5,6,4]
# 输出：[7,8,0,7]
# 示例2：
#
# 输入：l1 = [2,4,3], l2 = [5,6,4]
# 输出：[8,0,7]
# 示例3：
#
# 输入：l1 = [0], l2 = [0]
# 输出：[0]
#

class Solution:
    def matrixSum(self, nums: List[List[int]]) -> int:
        # m = 1
        # res = 0
        # while m != 0:
        #     m = 0
        #     for i in range(len(nums)):
        #         index = -1
        #         c = 0
        #         for j in range(len(nums[i])):
        #             if nums[i][j] > c:
        #                 c = nums[i][j]
        #                 index = j
        #         nums[i][index] = 0
        #         if c > m:
        #             m = c
        #     res += m
        # return res
        res = 0
        for i in range(len(nums)):
            nums[i].sort()
        for i in range(len(nums[0])):
            res += max([nums[j][i] for j in range(len(nums))])
        return res


if __name__ == "__main__":
    nums = [[0]]
    target = 9

    test = Solution().matrixSum(nums)
    print(test)
