import math
from bisect import bisect_right, bisect_left
from collections import defaultdict
from functools import lru_cache
from random import randint
from typing import List, Optional


# 1163. 按字典序排在最后的子串
# 给你一个字符串 s ，找出它的所有子串并按字典序排列，返回排在最后的那个子串。
#
#
#
# 示例 1：
#
# 输入：s = "abab"
# 输出："bab"
# 解释：我们可以找出 7 个子串 ["a", "ab", "aba", "abab", "b", "ba", "bab"]。按字典序排在最后的子串是 "bab"。
# 示例 2：
#
# 输入：s = "leetcode"
# 输出："tcode"
#
#

class Solution:
    def lastSubstring(self, s: str) -> str:
        i, j, k = 0, 1, 0
        while j + k < len(s):
            if s[i + k] == s[j + k]:
                k += 1
            elif s[i + k] < s[j + k]:
                i += k + 1
                k = 0
                if i >= j:
                    j = i + 1
            else:
                j += k + 1
                k = 0
        return s[i:]


if __name__ == "__main__":
    s = "abab"

    test = Solution().lastSubstring(s)
    print(test)
