import heapq
import math
from typing import List, Optional


# 162. 寻找峰值
# 中等
# 1.2K
# 相关企业
# 峰值元素是指其值严格大于左右相邻值的元素。
#
# 给你一个整数数组 nums，找到峰值元素并返回其索引。数组可能包含多个峰值，在这种情况下，返回 任何一个峰值 所在位置即可。
#
# 你可以假设 nums[-1] = nums[n] = -∞ 。
#
# 你必须实现时间复杂度为 O(log n) 的算法来解决此问题。
#
#
#
# 示例 1：
#
# 输入：nums = [1,2,3,1]
# 输出：2
# 解释：3 是峰值元素，你的函数应该返回其索引 2。
# 示例 2：
#
# 输入：nums = [1,2,1,3,5,6,4]
# 输出：1 或 5
# 解释：你的函数可以返回索引 1，其峰值元素为 2；
#      或者返回索引 5， 其峰值元素为 6。
#


class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        nums = [-math.inf] + nums + [-math.inf]
        n = len(nums)

        def find(i, j):
            if i + 1 >= j:
                return -1
            mid = (i + j) // 2
            if nums[mid] > nums[mid - 1] and nums[mid] > nums[mid + 1]:
                return mid
            if nums[mid] < nums[mid - 1]:
                val = find(i, mid)
            else:
                val = find(i, mid - 1)
            if val == -1:
                if nums[mid] < nums[mid + 1]:
                    val = find(mid, j)
                else:
                    val = find(mid + 1, j)
            return val

        return find(0, n - 1) - 1

        # nums = [-math.inf] + nums + [-math.inf]
        # n = len(nums)
        #
        # def find(i, j):
        #     if i > j:
        #         return -1
        #     if i == j:
        #         return i
        #     mid = (i + j) // 2
        #     if nums[mid] > nums[mid - 1] and nums[mid] > nums[mid + 1]:
        #         return mid
        #     if nums[mid] < nums[mid - 1]:
        #         return find(i, mid - 1)
        #     else:
        #         return find(mid + 1, j)
        #
        # return find(0, n - 1) - 1


if __name__ == "__main__":
    nums = [1, 2]
    test = Solution().findPeakElement(nums)
    print(test)
