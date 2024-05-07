import heapq
import math
from typing import List, Optional


# 2828. 判别首字母缩略词
# 提示
# 简单
# 17
# 相关企业
# 给你一个字符串数组 words 和一个字符串 s ，请你判断 s 是不是 words 的 首字母缩略词 。
#
# 如果可以按顺序串联 words 中每个字符串的第一个字符形成字符串 s ，则认为 s 是 words 的首字母缩略词。例如，"ab" 可以由 ["apple", "banana"] 形成，但是无法从 ["bear", "aardvark"] 形成。
#
# 如果 s 是 words 的首字母缩略词，返回 true ；否则，返回 false 。
#
#
#
# 示例 1：
#
# 输入：words = ["alice","bob","charlie"], s = "abc"
# 输出：true
# 解释：words 中 "alice"、"bob" 和 "charlie" 的第一个字符分别是 'a'、'b' 和 'c'。因此，s = "abc" 是首字母缩略词。
# 示例 2：
#
# 输入：words = ["an","apple"], s = "a"
# 输出：false
# 解释：words 中 "an" 和 "apple" 的第一个字符分别是 'a' 和 'a'。
# 串联这些字符形成的首字母缩略词是 "aa" 。
# 因此，s = "a" 不是首字母缩略词。
# 示例 3：
#
# 输入：words = ["never","gonna","give","up","on","you"], s = "ngguoy"
# 输出：true
# 解释：串联数组 words 中每个字符串的第一个字符，得到字符串 "ngguoy" 。
# 因此，s = "ngguoy" 是首字母缩略词。
#


class Solution:
    def isAcronym(self, words: List[str], s: str) -> bool:
        abbr = ''
        for w in words:
            abbr += w[0]
        return abbr == s


if __name__ == "__main__":
    words = ["alice","bob","charlie"]
    s = "abc"
    test = Solution().isAcronym(words, s)
    print(test)
