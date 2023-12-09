import heapq
import math
from collections import Counter, deque
from functools import cache
from itertools import product
from typing import List, Optional


# 187. 重复的DNA序列
# 中等
# 518
# 相关企业
# DNA序列 由一系列核苷酸组成，缩写为 'A', 'C', 'G' 和 'T'.。
#
# 例如，"ACGAATTCCG" 是一个 DNA序列 。
# 在研究 DNA 时，识别 DNA 中的重复序列非常有用。
#
# 给定一个表示 DNA序列 的字符串 s ，返回所有在 DNA 分子中出现不止一次的 长度为 10 的序列(子字符串)。你可以按 任意顺序 返回答案。
#
#
#
# 示例 1：
#
# 输入：s = "AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"
# 输出：["AAAAACCCCC","CCCCCAAAAA"]
# 示例 2：
#
# 输入：s = "AAAAAAAAAAAAA"
# 输出：["AAAAAAAAAA"]
#
#

class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        if len(s) <= 10:
            return []

        t = set()
        res = set()
        for i in range(10, len(s) + 1):
            ss = s[i - 10: i]
            if ss in t and ss not in res:
                res.add(ss)
            else:
                t.add(ss)
        return list(res)





if __name__ == "__main__":
    s = "AAAAAAAAAAA"

    test = Solution().findRepeatedDnaSequences(s)
    print(test)
