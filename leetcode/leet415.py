import heapq
import math
from collections import Counter, deque
from functools import cache
from itertools import product
from typing import List, Optional

# 415. 字符串相加
# 给定两个字符串形式的非负整数 num1 和num2 ，计算它们的和并同样以字符串形式返回。
#
# 你不能使用任何內建的用于处理大整数的库（比如 BigInteger）， 也不能直接将输入的字符串转换为整数形式。
#
#
#
# 示例 1：
#
# 输入：num1 = "11", num2 = "123"
# 输出："134"
# 示例 2：
#
# 输入：num1 = "456", num2 = "77"
# 输出："533"
# 示例 3：
#
# 输入：num1 = "0", num2 = "0"
# 输出："0"
#

class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        l = max(len(num1), len(num2))
        res = ""
        c = 0
        for i in range(-1, -(l+1), -1):
            a = 0
            b = 0
            if -i <= len(num1):
                a = ord(num1[i]) - ord("0")
            if -i <= len(num2):
                b = ord(num2[i]) - ord("0")
            s = (a + b + c) % 10
            res = str(s) + res
            c = (a + b + c) // 10
        if c != 0:
            res = str(c) + res
        return res

if __name__ == "__main__":
    num1 = "456"
    num2 = "777"

    test = Solution().addStrings(num1, num2)
    print(test)
