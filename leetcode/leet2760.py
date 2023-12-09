import heapq
import math
from collections import Counter, deque, defaultdict
from functools import cache, reduce
from itertools import product
from typing import List, Optional


# 2760. 最长奇偶子数组
# 提示
# 简单
# 44
# 相关企业
# 给你一个下标从 0 开始的整数数组 nums 和一个整数 threshold 。
#
# 请你从 nums 的子数组中找出以下标 l 开头、下标 r 结尾 (0 <= l <= r < nums.length) 且满足以下条件的 最长子数组 ：
#
# nums[l] % 2 == 0
# 对于范围 [l, r - 1] 内的所有下标 i ，nums[i] % 2 != nums[i + 1] % 2
# 对于范围 [l, r] 内的所有下标 i ，nums[i] <= threshold
# 以整数形式返回满足题目要求的最长子数组的长度。
#
# 注意：子数组 是数组中的一个连续非空元素序列。
#
#
#
# 示例 1：
#
# 输入：nums = [3,2,5,4], threshold = 5
# 输出：3
# 解释：在这个示例中，我们选择从 l = 1 开始、到 r = 3 结束的子数组 => [2,5,4] ，满足上述条件。
# 因此，答案就是这个子数组的长度 3 。可以证明 3 是满足题目要求的最大长度。
# 示例 2：
#
# 输入：nums = [1,2], threshold = 2
# 输出：1
# 解释：
# 在这个示例中，我们选择从 l = 1 开始、到 r = 1 结束的子数组 => [2] 。
# 该子数组满足上述全部条件。可以证明 1 是满足题目要求的最大长度。
# 示例 3：
#
# 输入：nums = [2,3,4,5], threshold = 4
# 输出：3
# 解释：
# 在这个示例中，我们选择从 l = 0 开始、到 r = 2 结束的子数组 => [2,3,4] 。
# 该子数组满足上述全部条件。
# 因此，答案就是这个子数组的长度 3 。可以证明 3 是满足题目要求的最大长度。
#
#
class Solution:
    def longestAlternatingSubarray(self, nums: List[int], threshold: int) -> int:
        res = 0
        s = -1
        e = -1
        alternating = False
        for i in range(len(nums)):
            if nums[i] <= threshold:
                if alternating:
                    if nums[i] % 2 != nums[i - 1] % 2 :
                        e = i
                    else:
                        res = max(res, e - s + 1)
                        if nums[i] % 2 == 0:
                            s = i
                            e = i
                        else:
                            alternating = False
                else:
                    if nums[i] % 2 == 0:
                        s = i
                        e = i
                        alternating = True
            else:
                res = max(res, e - s + 1)
                alternating = False
        if s == -1:
            return 0
        else:
            return max(res, e - s + 1)


if __name__ == "__main__":
    nums = [2,10,5]
    threshold = 7

    test = Solution().longestAlternatingSubarray(nums, threshold)

    print(test)
