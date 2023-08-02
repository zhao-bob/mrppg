import heapq
import math
from collections import Counter
from typing import List, Optional


# 1170. 比较字符串最小字母出现频次
# 定义一个函数 f(s)，统计 s  中（按字典序比较）最小字母的出现频次 ，其中 s 是一个非空字符串。
#
# 例如，若 s = "dcce"，那么 f(s) = 2，因为字典序最小字母是 "c"，它出现了 2 次。
#
# 现在，给你两个字符串数组待查表 queries 和词汇表 words 。对于每次查询 queries[i] ，需统计 words 中满足 f(queries[i]) < f(W) 的 词的数目 ，W 表示词汇表 words 中的每个词。
#
# 请你返回一个整数数组 answer 作为答案，其中每个 answer[i] 是第 i 次查询的结果。
#
#
#
# 示例 1：
#
# 输入：queries = ["cbd"], words = ["zaaaz"]
# 输出：[1]
# 解释：查询 f("cbd") = 1，而 f("zaaaz") = 3 所以 f("cbd") < f("zaaaz")。
# 示例 2：
#
# 输入：queries = ["bbb","cc"], words = ["a","aa","aaa","aaaa"]
# 输出：[1,2]
# 解释：第一个查询 f("bbb") < f("aaaa")，第二个查询 f("aaa") 和 f("aaaa") 都 > f("cc")。
#

class Solution:
    def numSmallerByFrequency(self, queries: List[str], words: List[str]) -> List[int]:
        def get_frequency(s):
            c = {}
            m = "z"
            for x in s:
                if x in c:
                    c[x] += 1
                else:
                    c[x] = 1
                if x < m:
                    m = x
            return c[m]

        cf = [0] * 11
        for x in words:
            cf[get_frequency(x)] += 1

        accum = [0] * 11
        for i in range(9, -1, -1):
            accum[i] += accum[i + 1] + cf[i + 1]

        ans = [0] * len(queries)

        for i in range(len(queries)):
            ans[i] = accum[get_frequency(queries[i])]
        return ans


if __name__ == "__main__":
    queries = ["bba","abaaaaaa","aaaaaa","bbabbabaab","aba","aa","baab","bbbbbb","aab","bbabbaabb"]
    words = ["aaabbb","aab","babbab","babbbb","b","bbbbbbbbab","a","bbbbbbbbbb","baaabbaab","aa"]

    test = Solution().numSmallerByFrequency(queries, words)
    print(test)
