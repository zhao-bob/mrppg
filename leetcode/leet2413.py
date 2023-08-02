import math
from bisect import bisect_right, bisect_left
from collections import defaultdict
from functools import lru_cache
from random import randint
from typing import List, Optional


# 2413. 最小偶倍数
# 给你一个正整数 n ，返回 2 和 n 的最小公倍数（正整数）。
#
#
# 示例 1：
#
# 输入：n = 5
# 输出：10
# 解释：5 和 2 的最小公倍数是 10 。
# 示例 2：
#
# 输入：n = 6
# 输出：6
# 解释：6 和 2 的最小公倍数是 6 。注意数字会是它自身的倍数。
#

class Solution:
    def smallestEvenMultiple(self, n: int) -> int:
        return n << (n & 1)


if __name__ == "__main__":
    n = 6

    test = Solution().smallestEvenMultiple(n)
    print(test)
