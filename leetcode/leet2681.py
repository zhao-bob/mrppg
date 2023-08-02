import heapq
import math
from collections import Counter, deque
from functools import cache
from itertools import product
from typing import List, Optional


# 2681. 英雄的力量
# 困难
# 给你一个下标从 0 开始的整数数组 nums ，它表示英雄的能力值。如果我们选出一部分英雄，这组英雄的 力量 定义为：
#
# i0 ，i1 ，... ik 表示这组英雄在数组中的下标。那么这组英雄的力量为 max(nums[i0],nums[i1] ... nums[ik])2 * min(nums[i0],nums[i1] ... nums[ik]) 。
# 请你返回所有可能的 非空 英雄组的 力量 之和。由于答案可能非常大，请你将结果对 109 + 7 取余。
#
#
#
# 示例 1：
#
# 输入：nums = [2,1,4]
# 输出：141
# 解释：
# 第 1 组：[2] 的力量为 22 * 2 = 8 。
# 第 2 组：[1] 的力量为 12 * 1 = 1 。
# 第 3 组：[4] 的力量为 42 * 4 = 64 。
# 第 4 组：[2,1] 的力量为 22 * 1 = 4 。
# 第 5 组：[2,4] 的力量为 42 * 2 = 32 。
# 第 6 组：[1,4] 的力量为 42 * 1 = 16 。
# 第​ ​​​​​​7 组：[2,1,4] 的力量为 42​​​​​​​ * 1 = 16 。
# 所有英雄组的力量之和为 8 + 1 + 64 + 4 + 32 + 16 + 16 = 141 。
# 示例 2：
#
# 输入：nums = [1,1,1]
# 输出：7
# 解释：总共有 7 个英雄组，每一组的力量都是 1 。所以所有英雄组的力量之和为 7 。
#

class Solution:
    def sumOfPower(self, nums: List[int]) -> int:
        nums.sort()

        fs = -1
        res = 0
        for i in range(len(nums)):
            f = nums[i] + fs + 1
            res += nums[i] * nums[i] * f
            fs += f
        return res % 1000000007


if __name__ == "__main__":
    nums = [1,1,1]

    test = Solution().sumOfPower(nums)
    print(test)
