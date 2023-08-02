import heapq
import math
from collections import Counter, deque
from functools import cache
from itertools import product
from typing import List, Optional

# 918. 环形子数组的最大和
# 给定一个长度为 n 的环形整数数组 nums ，返回 nums 的非空 子数组 的最大可能和 。
#
# 环形数组 意味着数组的末端将会与开头相连呈环状。形式上， nums[i] 的下一个元素是 nums[(i + 1) % n] ， nums[i] 的前一个元素是 nums[(i - 1 + n) % n] 。
#
# 子数组 最多只能包含固定缓冲区 nums 中的每个元素一次。形式上，对于子数组 nums[i], nums[i + 1], ..., nums[j] ，不存在 i <= k1, k2 <= j 其中 k1 % n == k2 % n 。
#
#
#
# 示例 1：
#
# 输入：nums = [1,-2,3,-2]
# 输出：3
# 解释：从子数组 [3] 得到最大和 3
# 示例 2：
#
# 输入：nums = [5,-3,5]
# 输出：10
# 解释：从子数组 [5,5] 得到最大和 5 + 5 = 10
# 示例 3：
#
# 输入：nums = [3,-2,2,-3]
# 输出：3
# 解释：从子数组 [3] 和 [3,-2,2] 都可以得到最大和 3
#

class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        mx = [-math.inf] * (len(nums) + 1)
        mi = [math.inf] * (len(nums) + 1)
        total = 0
        for i in range(len(nums)):
            mx[i + 1] = max(mx[i] + nums[i], nums[i])
            mi[i + 1] = min(mi[i] + nums[i], nums[i])
            total += nums[i]

        # l = nums[0]
        # r = total - nums[0]
        # ml = nums[0]
        # mr = total - nums[0]
        # mc = l + r
        # li = 0
        # ri = 0
        # for i in range(1, len(nums) - 1):
        #     if l + nums[i] > ml:
        #         li = i
        #         ml = l + nums[i]
        #     l += nums[i]
        #     if r - nums[i] >= mr:
        #         ri = i
        #         mr = r - nums[i]
        #     r -= nums[i]
        #     if li < ri:
        #         mc = max(mc, mr + ml)
        if total - min(mi) != 0:
            return max(max(mx), total - min(mi))
        else:
            return max(mx)


if __name__ == "__main__":
    nums = [-3,-2,-3]

    test = Solution().maxSubarraySumCircular(nums)
    print(test)
