# 2645. 构造有效字符串的最少插入数
# 中等
# 相关标签
# 相关企业
# 提示
# 给你一个字符串 word ，你可以向其中任何位置插入 "a"、"b" 或 "c" 任意次，返回使 word 有效 需要插入的最少字母数。
#
# 如果字符串可以由 "abc" 串联多次得到，则认为该字符串 有效 。
#
#
#
# 示例 1：
#
# 输入：word = "b"
# 输出：2
# 解释：在 "b" 之前插入 "a" ，在 "b" 之后插入 "c" 可以得到有效字符串 "abc" 。
# 示例 2：
#
# 输入：word = "aaa"
# 输出：6
# 解释：在每个 "a" 之后依次插入 "b" 和 "c" 可以得到有效字符串 "abcabcabc" 。
# 示例 3：
#
# 输入：word = "abc"
# 输出：0
# 解释：word 已经是有效字符串，不需要进行修改。
#
#
# 提示：
#
# 1 <= word.length <= 50
# word 仅由字母 "a"、"b" 和 "c" 组成。
#

import heapq
import math
from collections import Counter
from datetime import date
from typing import List, Optional


class Solution:
    def addMinimum(self, word: str) -> int:
        state = 0
        res = 0
        for i in range(len(word)):
            if word[i] == 'a':
                if state == 1:
                    res += 2
                elif state == 2:
                    res += 1
                state = 1
            elif word[i] == 'b':
                if state == 0:
                    res += 1
                elif state == 2:
                    res += 2
                state = 2
            elif word[i] == 'c':
                if state == 0:
                    res += 2
                elif state == 1:
                    res += 1
                state = 0
            else:
                return -1
        if state == 1:
            res += 2
        elif state == 2:
            res += 1
        return res



if __name__ == "__main__":
    s = "acbbac"

    test = Solution().addMinimum(s)

    print(test)
