import heapq
import math
from collections import Counter
from typing import List, Optional


# 1156. 单字符重复子串的最大长度
# 如果字符串中的所有字符都相同，那么这个字符串是单字符重复的字符串。
#
# 给你一个字符串 text，你只能交换其中两个字符一次或者什么都不做，然后得到一些单字符重复的子串。返回其中最长的子串的长度。
#
#
#
# 示例 1：
#
# 输入：text = "ababa"
# 输出：3
# 示例 2：
#
# 输入：text = "aaabaaa"
# 输出：6
# 示例 3：
#
# 输入：text = "aaabbaaa"
# 输出：4
# 示例 4：
#
# 输入：text = "aaaaa"
# 输出：5
# 示例 5：
#
# 输入：text = "abcdef"
# 输出：1
#

class Solution:
    def maxRepOpt2(self, text: str) -> int:
        count = Counter(text)
        res = 0
        for i in range(len(text)):
            # step1: 找出当前连续的一段 [i, j)
            j = i
            while j < len(text) and text[j] == text[i]:
                j += 1

            # step2: 如果这一段长度小于该字符出现的总数，并且前面或后面有空位，则使用 cur_cnt + 1 更新答案
            cur_cnt = j - i
            if cur_cnt < count[text[i]] and (j < len(text) or i > 0):
                res = max(res, cur_cnt + 1)

            # step3: 找到这一段后面与之相隔一个不同字符的另一段 [j + 1, k)，如果不存在则 k = j + 1
            k = j + 1
            while k < len(text) and text[k] == text[i]:
                k += 1
            res = max(res, min(k - i, count[text[i]]))
            i = j
        return res

    def maxRepOpt1(self, text: str) -> int:
        c = {}
        for x in text:
            if x in c:
                c[x] += 1
            else:
                c[x] = 1

        res = 1
        for x in c.keys():
            cl = 0
            sl = 0
            state = 0
            successive = True
            for i in range(len(text)):
                if state == 0:
                    if text[i] == x:
                        state = 1
                        cl = 1
                elif state == 1:
                    if text[i] != x:
                        if successive:
                            state = 2
                            successive = False
                            cl += 1
                        else:
                            state = 2
                            if cl > c[x]:
                                res = max(res, c[x])
                            else:
                                res = max(res, cl)
                            cl = sl + 1
                            sl = 0
                    else:
                        if not successive:
                            sl += 1
                        cl += 1
                else:
                    if text[i] == x:
                        cl += 1
                        sl = 1
                        state = 1
                    else:
                        successive = True
                        state = 0
                        if cl > c[x]:
                            res = max(res, c[x])
                        else:
                            res = max(res, cl)
                        cl = 0
            if cl >= c[x]:
                res = max(res, c[x])
            else:
                if state == 1 and successive:
                    cl += 1
                res = max(res, cl)
        return res




if __name__ == "__main__":
    text = "ababa"
    test = Solution().maxRepOpt2(text)
    print(test)
