import math
from typing import List


# 2451. 差值数组不同的字符串
# 给你一个字符串数组 words ，每一个字符串长度都相同，令所有字符串的长度都为 n 。
#
# 每个字符串 words[i] 可以被转化为一个长度为 n - 1 的 差值整数数组 difference[i] ，其中对于 0 <= j <= n - 2 有 difference[i][j] = words[i][j+1] - words[i][j] 。注意两个字母的差值定义为它们在字母表中 位置 之差，也就是说 'a' 的位置是 0 ，'b' 的位置是 1 ，'z' 的位置是 25 。
#
# 比方说，字符串 "acb" 的差值整数数组是 [2 - 0, 1 - 2] = [2, -1] 。
# words 中所有字符串 除了一个字符串以外 ，其他字符串的差值整数数组都相同。你需要找到那个不同的字符串。
#
# 请你返回 words中 差值整数数组 不同的字符串。
#
#
#
# 示例 1：
#
# 输入：words = ["adc","wzy","abc"]
# 输出："abc"
# 解释：
# - "adc" 的差值整数数组是 [3 - 0, 2 - 3] = [3, -1] 。
# - "wzy" 的差值整数数组是 [25 - 22, 24 - 25]= [3, -1] 。
# - "abc" 的差值整数数组是 [1 - 0, 2 - 1] = [1, 1] 。
# 不同的数组是 [1, 1]，所以返回对应的字符串，"abc"。
# 示例 2：
#
# 输入：words = ["aaa","bob","ccc","ddd"]
# 输出："bob"
# 解释：除了 "bob" 的差值整数数组是 [13, -13] 以外，其他字符串的差值整数数组都是 [0, 0] 。
#

class Solution:
    def oddString(self, words: List[str]) -> str:
        s = words[0]
        notodd = False
        odd = ""
        for i in range(1, len(words)):
            k = ord(s[0]) - ord(words[i][0])
            for j in range(len(s)):
                if k != ord(s[j]) - ord(words[i][j]):
                    if notodd:
                        return words[i]
                    else:
                        odd = s
                        break
            else:
                if odd != "":
                    return odd
                else:
                    notodd = True
            s = words[i]
        return odd






if __name__ == "__main__":
    words = ["aaa","bob","ccc","ddd"]

    test = Solution().oddString(words)
    print(test)
