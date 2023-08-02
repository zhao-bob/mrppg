import math
from collections import deque
from itertools import pairwise
from typing import List


# 1016. 子串能表示从 1 到 N 数字的二进制串
# 给定一个二进制字符串 s 和一个正整数 n，如果对于 [1, n] 范围内的每个整数，其二进制表示都是 s 的 子字符串 ，就返回 true，否则返回 false 。
#
# 子字符串 是字符串中连续的字符序列。
#
#
#
# 示例 1：
#
# 输入：s = "0110", n = 3
# 输出：true
# 示例 2：
#
# 输入：s = "0110", n = 4
# 输出：false
#

class Solution:
    def queryString(self, s: str, n: int) -> bool:
        if int(s, 2) < n:
            return False
        m = set()
        if len(s) == 1:
            return True
        for i in range(len(s) - 1):
            for j in range(i, len(s)):
                if 0 < int(s[i:j+1], 2) <= n:
                    m.add(int(s[i:j+1]))
        if len(m) == n:
            return True
        else:
            return False



if __name__ == "__main__":
    s = "1"
    n = 1

    test = Solution().queryString(s, n)
    print(test)
