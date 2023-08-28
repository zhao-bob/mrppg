import collections
import heapq
import math
from bisect import bisect_right
from collections import Counter, deque
from functools import cache
from itertools import product
from typing import List, Optional


# 228. 汇总区间
# 简单
# 给定一个  无重复元素 的 有序 整数数组 nums 。
#
# 返回 恰好覆盖数组中所有数字 的 最小有序 区间范围列表 。也就是说，nums 的每个元素都恰好被某个区间范围所覆盖，并且不存在属于某个范围但不属于 nums 的数字 x 。
#
# 列表中的每个区间范围 [a,b] 应该按如下格式输出：
#
# "a->b" ，如果 a != b
# "a" ，如果 a == b
#
#
# 示例 1：
#
# 输入：nums = [0,1,2,4,5,7]
# 输出：["0->2","4->5","7"]
# 解释：区间范围是：
# [0,2] --> "0->2"
# [4,5] --> "4->5"
# [7,7] --> "7"
# 示例 2：
#
# 输入：nums = [0,2,3,4,6,8,9]
# 输出：["0","2->4","6","8->9"]
# 解释：区间范围是：
# [0,0] --> "0"
# [2,4] --> "2->4"
# [6,6] --> "6"
# [8,9] --> "8->9"

class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        res = []
        if len(nums) == 0:
            return res
        s = nums[0]
        e = nums[0] + 1
        for x in nums[1:]:
            if x == e:
                e += 1
            elif x > e:
                if e - 1 == s:
                    res.append(str(s))
                else:
                    res.append(str(s) + '->' + str(e - 1))
                s = x
                e = x + 1
        if e - 1 == s:
            res.append(str(s))
        else:
            res.append(str(s) + '->' + str(e - 1))
        return res


if __name__ == "__main__":
    nums = [0,2,3,4,6,8,9]

    test = Solution().summaryRanges(nums)

    print(test)
