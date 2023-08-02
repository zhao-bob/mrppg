import heapq
import math
from collections import Counter, deque
from functools import cache
from itertools import product
from typing import List, Optional

# 2544. 交替数字和
# 给你一个正整数 n 。n 中的每一位数字都会按下述规则分配一个符号：
#
# 最高有效位 上的数字分配到 正 号。
# 剩余每位上数字的符号都与其相邻数字相反。
# 返回所有数字及其对应符号的和。
#
#
#
# 示例 1：
#
# 输入：n = 521
# 输出：4
# 解释：(+5) + (-2) + (+1) = 4
# 示例 2：
#
# 输入：n = 111
# 输出：1
# 解释：(+1) + (-1) + (+1) = 1
# 示例 3：
#
# 输入：n = 886996
# 输出：0
# 解释：(+8) + (-8) + (+6) + (-9) + (+9) + (-6) = 0
#
#

class Solution:
    def alternateDigitSum(self, n: int) -> int:
        # t = n
        # l = []
        # while t > 0:
        #     l.append(t % 10)
        #     t = t // 10
        #
        # res = 0
        # f = 1
        # while len(l) != 0:
        #     res += (l.pop() * f)
        #     f = -f
        # return res
        t = n
        res = 0
        f = 1
        while t > 0:
            res += ((t % 10) * f)
            t = t // 10
            f = -f

        return res * (-f)


if __name__ == "__main__":
    n = 521

    test = Solution().alternateDigitSum(n)
    print(test)
