import math
from functools import lru_cache
from typing import List


# 1017. 负二进制转换
# 给你一个整数 n ，以二进制字符串的形式返回该整数的 负二进制（base -2）表示。
#
# 注意，除非字符串就是 "0"，否则返回的字符串中不能含有前导零。
#
#
#
# 示例 1：
#
# 输入：n = 2
# 输出："110"
# 解释：(-2)2 + (-2)1 = 2
# 示例 2：
#
# 输入：n = 3
# 输出："111"
# 解释：(-2)2 + (-2)1 + (-2)0 = 3
# 示例 3：
#
# 输入：n = 4
# 输出："100"
# 解释：(-2)2 = 4
#

class Solution:
    def baseNeg2(self, n: int) -> str:
        if n == 0:
            return '0'
        r = n
        res = ''
        while r != 0:
            q = r % -2
            r = r // -2
            if q < 0:
                q = 1
                r += 1
            res = str(q) + res

        return res


if __name__ == "__main__":
    n = 6

    test = Solution().baseNeg2(n)
    print(test)
