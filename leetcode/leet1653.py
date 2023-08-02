from collections import Counter
from typing import List


# 1653. 使字符串平衡的最少删除次数

# 给你一个字符串 s ，它仅包含字符 'a' 和 'b'​​​​ 。
#
# 你可以删除 s 中任意数目的字符，使得 s 平衡 。当不存在下标对 (i,j) 满足 i < j ，且 s[i] = 'b' 的同时 s[j]= 'a' ，此时认为 s 是 平衡 的。
#
# 请你返回使 s 平衡 的 最少 删除次数。
#
#  
#
# 示例 1：
#
# 输入：s = "aababbab"
# 输出：2
# 解释：你可以选择以下任意一种方案：
# 下标从 0 开始，删除第 2 和第 6 个字符（"aababbab" -> "aaabbb"），
# 下标从 0 开始，删除第 3 和第 6 个字符（"aababbab" -> "aabbbb"）。
# 示例 2：
#
# 输入：s = "bbaaaaabb"
# 输出：2
# 解释：唯一的最优解是删除最前面两个字符。
#


class Solution:
    def minimumDeletions(self, s: str) -> int:
        a = [0] * len(s)
        bs = 0
        if s[0] == "a":
            a[0] = 0
        else:
            bs += 1
        for i in range(1, len(s)):
            if s[i] == "a":
                a[i] = min(a[i - 1] + 1, bs)
            else:
                a[i] = a[i - 1]
                bs += 1
        return a[len(s) - 1]


if __name__ == "__main__":
    s = "ababaaaabbbbbaaababbbbbbaaabbaababbabbbbaabbbbaabbabbabaabbbababaa"
    test = Solution().minimumDeletions(s)
    print(test)
