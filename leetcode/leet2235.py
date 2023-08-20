import heapq
import math
from collections import Counter, deque
from functools import cache
from itertools import product
from typing import List, Optional


# 2235. 两整数相加
# 简单
# 147
# 相关企业
# 给你两个整数 num1 和 num2，返回这两个整数的和。
#
#
# 示例 1：
#
# 输入：num1 = 12, num2 = 5
# 输出：17
# 解释：num1 是 12，num2 是 5 ，它们的和是 12 + 5 = 17 ，因此返回 17 。
# 示例 2：
#
# 输入：num1 = -10, num2 = 4
# 输出：-6
# 解释：num1 + num2 = -6 ，因此返回 -6 。

class Solution:
    def sum(self, num1: int, num2: int) -> int:
        return num1 + num2

if __name__ == "__main__":
    num1 = 12
    num2 = 5

    test = Solution().sum(num1, num2)

    print(test)
