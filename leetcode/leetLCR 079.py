import heapq
import math
from collections import deque
from typing import List


# LCR 079. 子集
# 中等
# 相关标签
# 相关企业
# 给定一个整数数组 nums ，数组中的元素 互不相同 。返回该数组所有可能的子集（幂集）。
#
# 解集 不能 包含重复的子集。你可以按 任意顺序 返回解集。
#
#
#
# 示例 1：
#
# 输入：nums = [1,2,3]
# 输出：[[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]
# 示例 2：
#
# 输入：nums = [0]
# 输出：[[],[0]]
#
#
# 提示：
#
# 1 <= nums.length <= 10
# -10 <= nums[i] <= 10
# nums 中的所有元素 互不相同
#


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        l = 2 ** n
        res = []
        for i in range(l):
            subset = []
            j = 0
            while i != 0:
                if i % 2 == 1:
                    subset.append(nums[j])
                i //= 2
                j += 1
            res.append(subset)
        return res


if __name__ == "__main__":
    nums = [1,2,3]
    test = Solution().subsets(nums)
    print(test)
