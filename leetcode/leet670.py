# 670. 最大交换
# 中等
# 相关标签
# 相关企业
# 给定一个非负整数，你至多可以交换一次数字中的任意两位。返回你能得到的最大值。
#
# 示例 1 :
#
# 输入: 2736
# 输出: 7236
# 解释: 交换数字2和数字7。
# 示例 2 :
#
# 输入: 9973
# 输出: 9973
# 解释: 不需要交换。
# 注意:
#
# 给定数字的范围是 [0, 108]
#

import heapq
import math
from collections import Counter
from datetime import date
from typing import List, Optional


class Solution:
    def maximumSwap(self, num: int) -> int:
        d = list(map(int, str(num)))
        n = len(d)
        m = [0] * n
        m[-1] = n - 1

        def cal(i, j):
            r = 0
            for k in range(n):
                if k == i:
                    r = r * 10 + d[j]
                elif k == j:
                    r = r * 10 + d[i]
                else:
                    r = r * 10 + d[k]
            return r

        res = num
        # for i in range(n - 2, -1, -1):
        #     if d[i] <= d[m[i + 1]]:
        #         res = max(res, cal(i, m[i + 1]))
        #         m[i] = m[i + 1]
        #     else:
        #         m[i] = i
        # return res
        ch = -1
        for i in range(n - 2, -1, -1):
            if d[i] < d[m[i + 1]]:
                m[i] = m[i + 1]
                ch = i
            elif d[i] > d[m[i + 1]]:
                m[i] = i
            else:
                m[i] = m[i + 1]
        if ch < 0:
            return res
        else:
            res = cal(ch, m[ch])
        return res


if __name__ == "__main__":
    num = 98368

    test = Solution().maximumSwap(num)

    print(test)
