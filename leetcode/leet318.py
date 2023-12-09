import heapq
import math
from collections import Counter, deque, defaultdict
from functools import cache, reduce
from itertools import product
from typing import List, Optional


# 318. 最大单词长度乘积
# 中等
# 442
# 相关企业
# 给你一个字符串数组 words ，找出并返回 length(words[i]) * length(words[j]) 的最大值，并且这两个单词不含有公共字母。如果不存在这样的两个单词，返回 0 。
#
#
#
# 示例 1：
#
# 输入：words = ["abcw","baz","foo","bar","xtfn","abcdef"]
# 输出：16
# 解释：这两个单词为 "abcw", "xtfn"。
# 示例 2：
#
# 输入：words = ["a","ab","abc","d","cd","bcd","abcd"]
# 输出：4
# 解释：这两个单词为 "ab", "cd"。
# 示例 3：
#
# 输入：words = ["a","aa","aaa","aaaa"]
# 输出：0
# 解释：不存在这样的两个单词。
#
#

class Solution:
    def maxProduct(self, words: List[str]) -> int:
        # res = 0
        # for i in range(len(words) - 1):
        #     si = set(words[i])
        #     for j in range(i + 1, len(words)):
        #         sj = set(words[j])
        #         if not si.intersection(sj):
        #             res = max(len(words[i]) * len(words[j]), res)
        # return res

        masks = defaultdict(int)
        for word in words:
            mask = reduce(lambda a, b: a | (1 << (ord(b) - ord('a'))), word, 0)
            masks[mask] = max(masks[mask], len(word))
        return max((masks[x] * masks[y] for x, y in product(masks, repeat=2) if x & y == 0), default=0)


if __name__ == "__main__":
    words = ["eae","ea","aaf","bda","fcf","dc","ac","ce","cefde","dabae"]

    test = Solution().maxProduct(words)
    print(test)
