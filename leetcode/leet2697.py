import heapq
import math
from typing import List


# 2697. 字典序最小回文串
# 提示
# 简单
# 16
# 相关企业
# 给你一个由 小写英文字母 组成的字符串 s ，你可以对其执行一些操作。在一步操作中，你可以用其他小写英文字母 替换  s 中的一个字符。
#
# 请你执行 尽可能少的操作 ，使 s 变成一个 回文串 。如果执行 最少 操作次数的方案不止一种，则只需选取 字典序最小 的方案。
#
# 对于两个长度相同的字符串 a 和 b ，在 a 和 b 出现不同的第一个位置，如果该位置上 a 中对应字母比 b 中对应字母在字母表中出现顺序更早，则认为 a 的字典序比 b 的字典序要小。
#
# 返回最终的回文字符串。
#
#
#
# 示例 1：
#
# 输入：s = "egcfe"
# 输出："efcfe"
# 解释：将 "egcfe" 变成回文字符串的最小操作次数为 1 ，修改 1 次得到的字典序最小回文字符串是 "efcfe"，只需将 'g' 改为 'f' 。
# 示例 2：
#
# 输入：s = "abcd"
# 输出："abba"
# 解释：将 "abcd" 变成回文字符串的最小操作次数为 2 ，修改 2 次得到的字典序最小回文字符串是 "abba" 。
# 示例 3：
#
# 输入：s = "seven"
# 输出："neven"
# 解释：将 "seven" 变成回文字符串的最小操作次数为 1 ，修改 1 次得到的字典序最小回文字符串是 "neven" 。
#


class Solution:
    def makeSmallestPalindrome(self, s: str) -> str:
        res = ''
        if len(s) % 2 == 0:
            left = len(s) // 2 - 1
            right = len(s) // 2
        else:
            left = len(s) // 2
            right = len(s) // 2

        while left >= 0:
            if left == right:
                res += s[left]
            else:
                if ord(s[left]) > ord(s[right]):
                    res = s[right] + res + s[right]
                else:
                    res = s[left] + res + s[left]
            left -= 1
            right += 1
        return res


if __name__ == "__main__":
    s = "a"
    test = Solution().makeSmallestPalindrome(s)
    print(test)
