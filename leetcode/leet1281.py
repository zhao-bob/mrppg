import heapq
import math
from collections import Counter, deque
from functools import cache
from itertools import product
from typing import List, Optional


# 1281. 整数的各位积和之差
# 简单
# 给你一个整数 n，请你帮忙计算并返回该整数「各位数字之积」与「各位数字之和」的差。
#
#
#
# 示例 1：
#
# 输入：n = 234
# 输出：15
# 解释：
# 各位数之积 = 2 * 3 * 4 = 24
# 各位数之和 = 2 + 3 + 4 = 9
# 结果 = 24 - 9 = 15
# 示例 2：
#
# 输入：n = 4421
# 输出：21
# 解释：
# 各位数之积 = 4 * 4 * 2 * 1 = 32
# 各位数之和 = 4 + 4 + 2 + 1 = 11
# 结果 = 32 - 11 = 21

class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        p = 1
        s = 0
        a = n
        while a != 0:
            d = a % 10
            p *= d
            s += d
            a = a // 10
        return p - s


if __name__ == "__main__":
    n = 1111

    test = Solution().subtractProductAndSum(n)
    print(test)
