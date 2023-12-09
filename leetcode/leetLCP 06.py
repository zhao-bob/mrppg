import collections
import heapq
import math
from bisect import bisect_right
from collections import Counter, deque
from functools import cache
from itertools import product
from typing import List, Optional


# LCP 06. 拿硬币
# 简单
# 76
# 相关企业
# 桌上有 n 堆力扣币，每堆的数量保存在数组 coins 中。我们每次可以选择任意一堆，拿走其中的一枚或者两枚，求拿完所有力扣币的最少次数。
#
# 示例 1：
#
# 输入：[4,2,1]
#
# 输出：4
#
# 解释：第一堆力扣币最少需要拿 2 次，第二堆最少需要拿 1 次，第三堆最少需要拿 1 次，总共 4 次即可拿完。
#
# 示例 2：
#
# 输入：[2,3,10]
#
# 输出：8

class Solution:
    def minCount(self, coins: List[int]) -> int:
        res = 0
        for c in coins:
            if c % 2 == 0:
                res += c // 2
            else:
                res += c // 2 + 1
        return res


if __name__ == "__main__":
    coins = [2,3,10]

    test = Solution().minCount(coins)

    print(test)
