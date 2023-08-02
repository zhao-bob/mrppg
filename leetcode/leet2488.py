import math
from typing import List


# 2488. 统计中位数为 K 的子数组

# 给你一个长度为 n 的数组 nums ，该数组由从 1 到 n 的 不同 整数组成。另给你一个正整数 k 。
#
# 统计并返回 nums 中的 中位数 等于 k 的非空子数组的数目。
#
# 注意：
#
# 数组的中位数是按 递增 顺序排列后位于 中间 的那个元素，如果数组长度为偶数，则中位数是位于中间靠 左 的那个元素。
# 例如，[2,3,1,4] 的中位数是 2 ，[8,4,3,5,1] 的中位数是 4 。
# 子数组是数组中的一个连续部分。
#  
#
# 示例 1：
#
# 输入：nums = [3,2,1,4,5], k = 4
# 输出：3
# 解释：中位数等于 4 的子数组有：[4]、[4,5] 和 [1,4,5] 。
# 示例 2：
#
# 输入：nums = [2,3,1], k = 3
# 输出：1
# 解释：[3] 是唯一一个中位数等于 3 的子数组。
#

class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        diff = [0] * len(nums)
        ki = -1
        for i in range(len(nums)):
            if nums[i] > k:
                diff[i] = 1
            elif nums[i] < k:
                diff[i] = -1
            else:
                ki = i
        if ki == -1:
            return 0

        res = 1
        right = {}
        for i in range(ki + 1, len(nums)):
            diff[i] = diff[i - 1] + diff[i]
            if diff[i] == 0 or diff[i] == 1:
                res += 1
            if diff[i] in right:
                right[diff[i]] += 1
            else:
                right[diff[i]] = 1

        left = {}
        for i in range(ki - 1, -1, -1):
            diff[i] = diff[i] + diff[i + 1]
            if diff[i] == 0 or diff[i] == 1:
                res += 1
            if diff[i] in left:
                left[diff[i]] += 1
            else:
                left[diff[i]] = 1

        for x in right:
            if -x in left:
                res += right[x] * left[-x]
            if (-x + 1) in left:
                res += right[x] * left[1 - x]

        return res




if __name__ == "__main__":
    nums = [3,2,1,4,5]
    k = 4

    test = Solution().countSubarrays(nums, k)
    print(test)
