import heapq
import math
from collections import Counter, deque, defaultdict
from functools import cache, reduce
from itertools import product
from typing import List, Optional


# 1410. HTML 实体解析器
# 提示
# 中等
# 39
# 相关企业
# 「HTML 实体解析器」 是一种特殊的解析器，它将 HTML 代码作为输入，并用字符本身替换掉所有这些特殊的字符实体。
#
# HTML 里这些特殊字符和它们对应的字符实体包括：
#
# 双引号：字符实体为 &quot; ，对应的字符是 " 。
# 单引号：字符实体为 &apos; ，对应的字符是 ' 。
# 与符号：字符实体为 &amp; ，对应对的字符是 & 。
# 大于号：字符实体为 &gt; ，对应的字符是 > 。
# 小于号：字符实体为 &lt; ，对应的字符是 < 。
# 斜线号：字符实体为 &frasl; ，对应的字符是 / 。
# 给你输入字符串 text ，请你实现一个 HTML 实体解析器，返回解析器解析后的结果。
#
#
#
# 示例 1：
#
# 输入：text = "&amp; is an HTML entity but &ambassador; is not."
# 输出："& is an HTML entity but &ambassador; is not."
# 解释：解析器把字符实体 &amp; 用 & 替换
# 示例 2：
#
# 输入：text = "and I quote: &quot;...&quot;"
# 输出："and I quote: \"...\""
# 示例 3：
#
# 输入：text = "Stay home! Practice on Leetcode :)"
# 输出："Stay home! Practice on Leetcode :)"
# 示例 4：
#
# 输入：text = "x &gt; y &amp;&amp; x &lt; y is always false"
# 输出："x > y && x < y is always false"
# 示例 5：
#
# 输入：text = "leetcode.com&frasl;problemset&frasl;all"
# 输出："leetcode.com/problemset/all"
#
#

class Solution:
    def entityParser(self, text: str) -> str:
        # 双引号：字符实体为 &quot; ，对应的字符是 " 。
        # 单引号：字符实体为 &apos; ，对应的字符是 ' 。
        # 与符号：字符实体为 &amp; ，对应对的字符是 & 。
        # 大于号：字符实体为 &gt; ，对应的字符是 > 。
        # 小于号：字符实体为 &lt; ，对应的字符是 < 。
        # 斜线号：字符实体为 &frasl; ，对应的字符是 / 。
        i = 0
        special = False
        res = ''
        while i < len(text):
            if not special:
                if text[i] == '&':
                    special = True
                else:
                    res += text[i]
                i += 1
            else:
                if text[i: i + 3] == 'gt;':
                    res += '>'
                    i += 3
                elif text[i: i + 3] == 'lt;':
                    res += '<'
                    i += 3
                elif text[i: i + 4] == 'amp;':
                    res += '&'
                    i += 4
                elif text[i: i + 5] == 'apos;':
                    res += "'"
                    i += 5
                elif text[i: i + 5] == 'quot;':
                    res += '''"'''
                    i += 5
                elif text[i: i + 6] == 'frasl;':
                    res += '/'
                    i += 6
                else:
                    res += '&'
                special = False
        if special:
            res += '&'
        return res

if __name__ == "__main__":
    text = "&amp; is an HTML entity but &ambassador; is not."

    test = Solution().entityParser(text)

    print(test)
