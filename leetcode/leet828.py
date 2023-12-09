import heapq
import math
from collections import Counter
from functools import cache
from typing import List, Optional
from sortedcontainers import SortedList


# 828. 统计子串中的唯一字符
# 困难
# 320
# 相关企业
# 我们定义了一个函数 countUniqueChars(s) 来统计字符串 s 中的唯一字符，并返回唯一字符的个数。
#
# 例如：s = "LEETCODE" ，则其中 "L", "T","C","O","D" 都是唯一字符，因为它们只出现一次，所以 countUniqueChars(s) = 5 。
#
# 本题将会给你一个字符串 s ，我们需要返回 countUniqueChars(t) 的总和，其中 t 是 s 的子字符串。输入用例保证返回值为 32 位整数。
#
# 注意，某些子字符串可能是重复的，但你统计时也必须算上这些重复的子字符串（也就是说，你必须统计 s 的所有子字符串中的唯一字符）。
#
#
#
# 示例 1：
#
# 输入: s = "ABC"
# 输出: 10
# 解释: 所有可能的子串为："A","B","C","AB","BC" 和 "ABC"。
#      其中，每一个子串都由独特字符构成。
#      所以其长度总和为：1 + 1 + 1 + 2 + 2 + 3 = 10
# 示例 2：
#
# 输入: s = "ABA"
# 输出: 8
# 解释: 除了 countUniqueChars("ABA") = 1 之外，其余与示例 1 相同。
# 示例 3：
#
# 输入：s = "LEETCODE"
# 输出：92
#


class Solution:
    def uniqueLetterString(self, s: str) -> int:
        st = [[-1, -1] for _ in range(26)]
        n = len(s)
        c = 0
        res = 0
        for i in range(n - 1, -1, -1):
            k = ord(s[i]) - ord('A')
            if st[k][0] == -1:
                nc = c + (n - i)
            elif st[k][1] == -1:
                nc = c + (st[k][0] - i) - (n - st[k][0])
            else:
                nc = c + (st[k][0] - 1 - i) - (st[k][1] - 1 - st[k][0])
            res += nc
            c = nc
            st[k][1], st[k][0] = st[k][0], i
        return res


if __name__ == "__main__":
    s = "EETCODE"
    test = Solution().uniqueLetterString(s)
    print(test)
