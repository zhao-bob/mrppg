import math
from typing import List


# 1031. 两个非重叠子数组的最大和
# 给你一个整数数组 nums 和两个整数 firstLen 和 secondLen，请你找出并返回两个非重叠 子数组 中元素的最大和，长度分别为 firstLen 和 secondLen 。
#
# 长度为 firstLen 的子数组可以出现在长为 secondLen 的子数组之前或之后，但二者必须是不重叠的。
#
# 子数组是数组的一个 连续 部分。
#
#
#
# 示例 1：
#
# 输入：nums = [0,6,5,2,2,5,1,9,4], firstLen = 1, secondLen = 2
# 输出：20
# 解释：子数组的一种选择中，[9] 长度为 1，[6,5] 长度为 2。
# 示例 2：
#
# 输入：nums = [3,8,1,3,2,1,8,9,0], firstLen = 3, secondLen = 2
# 输出：29
# 解释：子数组的一种选择中，[3,8,1] 长度为 3，[8,9] 长度为 2。
# 示例 3：
#
# 输入：nums = [2,1,5,6,0,9,5,0,3,8], firstLen = 4, secondLen = 3
# 输出：31
# 解释：子数组的一种选择中，[5,6,0,9] 长度为 4，[0,3,8] 长度为 3。
#

class Solution:
    def maxSumTwoNoOverlap1(self, nums: List[int], firstLen: int, secondLen: int) -> int:
        return max(self.help(nums, firstLen, secondLen), self.help(nums, secondLen, firstLen))

    def help(self, nums, firstLen, secondLen):
        suml = 0
        for i in range(0, firstLen):
            suml += nums[i]
        maxSumL = suml
        sumr = 0
        for i in range(firstLen, firstLen + secondLen):
            sumr += nums[i]
        res = maxSumL + sumr
        j = firstLen
        for i in range(firstLen + secondLen, len(nums)):
            suml += nums[j] - nums[j - firstLen]
            maxSumL = max(maxSumL, suml)
            sumr += nums[i] - nums[i - secondLen]
            res = max(res, maxSumL + sumr)
            j += 1
        return res

    def maxSumTwoNoOverlap(self, nums: List[int], firstLen: int, secondLen: int) -> int:
        s = [0] * len(nums)
        for i in range(len(nums)):
            if i - 1 >= 0:
                s[i] = s[i - 1] + nums[i]
            else:
                s[i] = nums[i]
        rnums = nums[::-1]
        rs = [0] * len(rnums)
        for i in range(len(rnums)):
            if i - 1 >= 0:
                rs[i] = rs[i - 1] + rnums[i]
            else:
                rs[i] = rnums[i]

        m1 = max(self.max_sum(nums, firstLen, secondLen, s), self.max_sum(nums, secondLen, firstLen, s))
        m2 = max(self.max_sum(rnums, firstLen, secondLen, rs), self.max_sum(rnums, secondLen, firstLen, rs))
        return max(m1, m2)

    def max_sum(self, nums, first, second, s):
        mf = s[first - 1]
        ms = [0] * (len(nums) - second - first + 1)
        ms[-1] = s[len(nums) - 1] - s[len(nums) - second - 1]
        for i in range(len(ms) - 2, -1, -1):
            ms[i] = max(ms[i + 1], s[i + first - 1 + second] - s[i + first - 1])

        m = mf + ms[-1]
        for i in range(first, len(nums) - second):
            m = max(m, mf + ms[i - first])
            mf = max(mf, s[i] - s[i - first])
        return m


if __name__ == "__main__":
    nums = [4,5,14,16,16,20,7,13,8,15]
    firstLen = 3
    secondLen = 5

    test = Solution().maxSumTwoNoOverlap1(nums, firstLen, secondLen)
    print(test)
