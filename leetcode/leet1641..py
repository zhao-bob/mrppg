import math
from typing import List


# 1641. 统计字典序元音字符串的数目
# 给你一个整数 n，请返回长度为 n 、仅由元音 (a, e, i, o, u) 组成且按 字典序排列 的字符串数量。
#
# 字符串 s 按 字典序排列 需要满足：对于所有有效的 i，s[i] 在字母表中的位置总是与 s[i+1] 相同或在 s[i+1] 之前。
#
#
#
# 示例 1：
#
# 输入：n = 1
# 输出：5
# 解释：仅由元音组成的 5 个字典序字符串为 ["a","e","i","o","u"]
# 示例 2：
#
# 输入：n = 2
# 输出：15
# 解释：仅由元音组成的 15 个字典序字符串为
# ["aa","ae","ai","ao","au","ee","ei","eo","eu","ii","io","iu","oo","ou","uu"]
# 注意，"ea" 不是符合题意的字符串，因为 'e' 在字母表中的位置比 'a' 靠后
# 示例 3：
#
# 输入：n = 33
# 输出：66045
#

class Solution:
    def countVowelStrings(self, n: int) -> int:
        c = [1] * 5

        # for i in range(1, n):
        #     for l in range(5):
        #         for m in range(0, l):
        #             c[m] += c[l]
        # return sum(c)
        for i in range(1, n):
            for l in range(1, 5):
                c[l] += c[l - 1]
        return sum(c)



if __name__ == "__main__":
    n = 33

    test = Solution().countVowelStrings(n)
    print(test)
