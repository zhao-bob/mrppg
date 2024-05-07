import heapq
import math
from collections import deque, Counter
from itertools import count
from typing import List, Optional


# 1017. 负二进制转换
# 给你一个整数 n ，以二进制字符串的形式返回该整数的 负二进制（base -2）表示。
#
# 注意，除非字符串就是 "0"，否则返回的字符串中不能含有前导零。
#
#
#
# 示例 1：
#
# 输入：n = 2
# 输出："110"
# 解释：(-2)2 + (-2)1 = 2
# 示例 2：
#
# 输入：n = 3
# 输出："111"
# 解释：(-2)2 + (-2)1 + (-2)0 = 3
# 示例 3：
#
# 输入：n = 4
# 输出："100"
# 解释：(-2)2 = 4
# 提示：
#
# 0 <= n <= 109
#

class Solution:
    def baseNeg2(self, n: int) -> str:
        res = ''
        while n != 0:
            r = n % 2
            if r == 0:
                n = n // -2
            else:
                n = (n - 1) // -2
            res = str(r) + res
        return '0' if res == '' else res

if __name__ == "__main__":
    n = 1
    test = Solution().baseNeg2(n)
    print(test)
