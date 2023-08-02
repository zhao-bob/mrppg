import math
from functools import lru_cache
from typing import List, Optional


# 1147. 段式回文
# 你会得到一个字符串 text 。你应该把它分成 k 个子字符串 (subtext1, subtext2，…， subtextk) ，要求满足:
#
# subtexti 是 非空 字符串
# 所有子字符串的连接等于 text ( 即subtext1 + subtext2 + ... + subtextk == text )
# 对于所有 i 的有效值( 即 1 <= i <= k ) ，subtexti == subtextk - i + 1 均成立
# 返回k可能最大值。
#
#
#
# 示例 1：
#
# 输入：text = "ghiabcdefhelloadamhelloabcdefghi"
# 输出：7
# 解释：我们可以把字符串拆分成 "(ghi)(abcdef)(hello)(adam)(hello)(abcdef)(ghi)"。
# 示例 2：
#
# 输入：text = "merchant"
# 输出：1
# 解释：我们可以把字符串拆分成 "(merchant)"。
# 示例 3：
#
# 输入：text = "antaprezatepzapreanta"
# 输出：11
# 解释：我们可以把字符串拆分成 "(a)(nt)(a)(pre)(za)(tpe)(za)(pre)(a)(nt)(a)"。
#

class Solution:
    def longestDecomposition(self, text: str) -> int:
        if len(text) == 0:
            return 0
        elif len(text) == 1:
            return 1

        res = 1
        for i in range(len(text) - 1, (len(text) - 1) // 2, -1):
            if text[0] == text[i]:
                l = len(text) - i
                if text[0:l] == text[i:]:
                    return max(res, 2 + self.longestDecomposition(text[l:i]))
        return res


if __name__ == "__main__":
    text = "elvtoelvto"
    test = Solution().longestDecomposition(text)
    print(test)
