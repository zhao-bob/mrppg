import heapq
import math
from collections import Counter, deque, defaultdict
from functools import cache, reduce
from itertools import product
from typing import List, Optional


# 2609. 最长平衡子字符串
# 提示
# 简单
# 27
# 相关企业
# 给你一个仅由 0 和 1 组成的二进制字符串 s 。
#
# 如果子字符串中 所有的 0 都在 1 之前 且其中 0 的数量等于 1 的数量，则认为 s 的这个子字符串是平衡子字符串。请注意，空子字符串也视作平衡子字符串。
#
# 返回  s 中最长的平衡子字符串长度。
#
# 子字符串是字符串中的一个连续字符序列。
#
#
#
# 示例 1：
#
# 输入：s = "01000111"
# 输出：6
# 解释：最长的平衡子字符串是 "000111" ，长度为 6 。
# 示例 2：
#
# 输入：s = "00111"
# 输出：4
# 解释：最长的平衡子字符串是 "0011" ，长度为  4 。
# 示例 3：
#
# 输入：s = "111"
# 输出：0
# 解释：除了空子字符串之外不存在其他平衡子字符串，所以答案为 0 。
#
#

class Solution:
    def findTheLongestBalancedSubstring(self, s: str) -> int:
        res = 0
        i = 1
        while i < len(s):
            if s[i - 1] == "0" and s[i] == "1":
                left = i - 1
                right = i
                l = 0
                while left >= 0 and right < len(s):
                    if s[left] == "0" and s[right] == "1":
                        l += 2
                    else:
                        break
                    left -= 1
                    right += 1
                res = max(res, l)
                i = right + 1
            else:
                i += 1
        return res


if __name__ == "__main__":
    s = "01000111"

    test = Solution().findTheLongestBalancedSubstring(s)
    print(test)
