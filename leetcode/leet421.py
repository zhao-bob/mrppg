import heapq
import math
from collections import Counter, deque
from functools import cache
from itertools import product
from typing import List, Optional


# 421. 数组中两个数的最大异或值
# 中等
# 577
# 相关企业
# 给你一个整数数组 nums ，返回 nums[i] XOR nums[j] 的最大运算结果，其中 0 ≤ i ≤ j < n 。
#
#
#
# 示例 1：
#
# 输入：nums = [3,10,5,25,2,8]
# 输出：28
# 解释：最大运算结果是 5 XOR 25 = 28.
# 示例 2：
#
# 输入：nums = [14,70,53,83,49,91,36,80,92,51,66,70]
# 输出：127
#
#

class Solution:
    def findMaximumXOR(self, nums: List[int]) -> int:
        # 最高位的二进制位编号为 30
        HIGH_BIT = 30

        x = 0
        for k in range(HIGH_BIT, -1, -1):
            seen = set()
            # 将所有的 pre^k(a_j) 放入哈希表中
            for num in nums:
                # 如果只想保留从最高位开始到第 k 个二进制位为止的部分
                # 只需将其右移 k 位
                seen.add(num >> k)

            # 目前 x 包含从最高位开始到第 k+1 个二进制位为止的部分
            # 我们将 x 的第 k 个二进制位置为 1，即为 x = x*2+1
            x_next = x * 2 + 1

            # 枚举 i
            for num in nums:
                if x_next ^ (num >> k) in seen:
                    x = x_next
                    break
            else:
                x = x_next - 1

        return x









if __name__ == "__main__":
    nums = [14,70,53,83,49,91,36,80,92,51,66,70]

    test = Solution().findMaximumXOR(nums)
    print(test)
