import math
from functools import lru_cache
from typing import List


# 2427. 公因子的数目
# 给你两个正整数 a 和 b ，返回 a 和 b 的 公 因子的数目。
#
# 如果 x 可以同时整除 a 和 b ，则认为 x 是 a 和 b 的一个 公因子 。
#
#
#
# 示例 1：
#
# 输入：a = 12, b = 6
# 输出：4
# 解释：12 和 6 的公因子是 1、2、3、6 。
# 示例 2：
#
# 输入：a = 25, b = 30
# 输出：2
# 解释：25 和 30 的公因子是 1、5 。
#

class Solution:
    def commonFactors(self, a: int, b: int) -> int:
        mi = min(a, b)
        ma = max(a, b)

        k = ma % mi
        ma = mi
        mi = k
        while k != 0:
            k = ma % mi
            ma = mi
            mi = k

        res = 0
        # for i in range(ma):
        #     if ma % (i+1) == 0:
        #         res += 1
        i = 1
        while i * i <= ma:
            if ma % i == 0:
                res += 1
                if i * i != ma:
                    res += 1
            i += 1
        return res


if __name__ == "__main__":
    a = 7
    b = 30

    test = Solution().commonFactors(a, b)
    print(test)
