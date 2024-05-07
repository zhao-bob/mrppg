# 466. 统计重复个数
# 困难
# 197
# 相关企业
# 定义 str = [s, n] 表示 str 由 n 个字符串 s 连接构成。
#
# 例如，str == ["abc", 3] =="abcabcabc" 。
# 如果可以从 s2 中删除某些字符使其变为 s1，则称字符串 s1 可以从字符串 s2 获得。
#
# 例如，根据定义，s1 = "abc" 可以从 s2 = "abdbec" 获得，仅需要删除加粗且用斜体标识的字符。
# 现在给你两个字符串 s1 和 s2 和两个整数 n1 和 n2 。由此构造得到两个字符串，其中 str1 = [s1, n1]、str2 = [s2, n2] 。
#
# 请你找出一个最大整数 m ，以满足 str = [str2, m] 可以从 str1 获得。
#
#
#
# 示例 1：
#
# 输入：s1 = "acb", n1 = 4, s2 = "ab", n2 = 2
# 输出：2
# 示例 2：
#
# 输入：s1 = "acb", n1 = 1, s2 = "acb", n2 = 1
# 输出：1
#

import heapq
import math
from collections import Counter
from datetime import date
from typing import List


class Solution:
    def getMaxRepetitions(self, s1: str, n1: int, s2: str, n2: int) -> int:
        # if n1 == 0:
        #     return 0
        # s1cnt, index, s2cnt = 0, 0, 0
        # # recall 是我们用来找循环节的变量，它是一个哈希映射
        # # 我们如何找循环节？假设我们遍历了 s1cnt 个 s1，此时匹配到了第 s2cnt 个 s2 中的第 index 个字符
        # # 如果我们之前遍历了 s1cnt' 个 s1 时，匹配到的是第 s2cnt' 个 s2 中同样的第 index 个字符，那么就有循环节了
        # # 我们用 (s1cnt', s2cnt', index) 和 (s1cnt, s2cnt, index) 表示两次包含相同 index 的匹配结果
        # # 那么哈希映射中的键就是 index，值就是 (s1cnt', s2cnt') 这个二元组
        # # 循环节就是；
        # #    - 前 s1cnt' 个 s1 包含了 s2cnt' 个 s2
        # #    - 以后的每 (s1cnt - s1cnt') 个 s1 包含了 (s2cnt - s2cnt') 个 s2
        # # 那么还会剩下 (n1 - s1cnt') % (s1cnt - s1cnt') 个 s1, 我们对这些与 s2 进行暴力匹配
        # # 注意 s2 要从第 index 个字符开始匹配
        # recall = dict()
        # while True:
        #     # 我们多遍历一个 s1，看看能不能找到循环节
        #     s1cnt += 1
        #     for ch in s1:
        #         if ch == s2[index]:
        #             index += 1
        #             if index == len(s2):
        #                 s2cnt, index = s2cnt + 1, 0
        #     # 还没有找到循环节，所有的 s1 就用完了
        #     if s1cnt == n1:
        #         return s2cnt // n2
        #     # 出现了之前的 index，表示找到了循环节
        #     if index in recall:
        #         s1cnt_prime, s2cnt_prime = recall[index]
        #         # 前 s1cnt' 个 s1 包含了 s2cnt' 个 s2
        #         pre_loop = (s1cnt_prime, s2cnt_prime)
        #         # 以后的每 (s1cnt - s1cnt') 个 s1 包含了 (s2cnt - s2cnt') 个 s2
        #         in_loop = (s1cnt - s1cnt_prime, s2cnt - s2cnt_prime)
        #         break
        #     else:
        #         recall[index] = (s1cnt, s2cnt)
        #
        # # ans 存储的是 S1 包含的 s2 的数量，考虑的之前的 pre_loop 和 in_loop
        # ans = pre_loop[1] + (n1 - pre_loop[0]) // in_loop[0] * in_loop[1]
        # # S1 的末尾还剩下一些 s1，我们暴力进行匹配
        # rest = (n1 - pre_loop[0]) % in_loop[0]
        # for i in range(rest):
        #     for ch in s1:
        #         if ch == s2[index]:
        #             index += 1
        #             if index == len(s2):
        #                 ans, index = ans + 1, 0
        # # S1 包含 ans 个 s2，那么就包含 ans / n2 个 S2
        # return ans // n2

        n = len(s2)
        d = {}
        for i in range(n):
            cnt = 0
            j = i
            for c in s1:
                if c == s2[j]:
                    j += 1
                if j == n:
                    cnt += 1
                    j = 0
            d[i] = (cnt, j)

        ans = 0
        j = 0
        for _ in range(n1):
            cnt, j = d[j]
            ans += cnt
        return ans // n2

if __name__ == "__main__":
    s1 = "acb"
    n1 = 10
    s2 = "ba"
    n2 = 1
    test = Solution().getMaxRepetitions(s1, n1, s2, n2)
    print(test)
