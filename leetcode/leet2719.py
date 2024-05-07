# 2719. 统计整数数目
# 困难
# 相关标签
# 相关企业
# 提示
# 给你两个数字字符串 num1 和 num2 ，以及两个整数 max_sum 和 min_sum 。如果一个整数 x 满足以下条件，我们称它是一个好整数：
#
# num1 <= x <= num2
# min_sum <= digit_sum(x) <= max_sum.
# 请你返回好整数的数目。答案可能很大，请返回答案对 109 + 7 取余后的结果。
#
# 注意，digit_sum(x) 表示 x 各位数字之和。
#
#
#
# 示例 1：
#
# 输入：num1 = "1", num2 = "12", min_num = 1, max_num = 8
# 输出：11
# 解释：总共有 11 个整数的数位和在 1 到 8 之间，分别是 1,2,3,4,5,6,7,8,10,11 和 12 。所以我们返回 11 。
# 示例 2：
#
# 输入：num1 = "1", num2 = "5", min_num = 1, max_num = 5
# 输出：5
# 解释：数位和在 1 到 5 之间的 5 个整数分别为 1,2,3,4 和 5 。所以我们返回 5 。
#
#
# 提示：
#
# 1 <= num1 <= num2 <= 1022
# 1 <= min_sum <= max_sum <= 400
#

import heapq
import math
from collections import Counter
from datetime import date
from typing import List, Optional

class Solution:
    def count(self, num1: str, num2: str, min_sum: int, max_sum: int) -> int:
        s1 = len(num1)
        s2 = len(num2)
        dp = [[0] * (max_sum + 1) for _ in range(s2)]
        dp[0][0] = 1
        for j in range(1, max_sum + 1):
            if j < 10:
                dp[0][j] = dp[0][j - 1] + 1
            else:
                dp[0][j] = dp[0][j - 1]

        for i in range(1, s2):
            for j in range(max_sum + 1):
                for k in range(1, 10):
                    if k <= j:
                        for l in range(i):
                            dp[i][j] += dp[l][j - k]
                    else:
                        break

        l1 = list(map(int, num1))
        sd1 = [0] * (s1 + 1)
        for i in range(len(l1)):
            sd1[i + 1] = l1[i] + sd1[i]
        r1 = 0
        for i in range(s1):
            for j in range(l1[s1 - 1 - i]):
                if sd1[s1 - 1 - i] + j <= max_sum:
                    if i == 0:
                        if sd1[s1 - 1 - i] + j >= min_sum:
                            r1 += 1
                    else:
                        for k in range(i):
                            r1 += (dp[k][max_sum - sd1[s1 - 1 - i] - j] - (dp[k][min_sum - sd1[s1 - 1 - i] - j - 1] if min_sum - sd1[s1 - 1 - i] - j - 1 >= 0 else 0))
                else:
                    break
        l2 = list(map(int, num2))
        sd2 = [0] * (s2 + 1)
        r2 = 0
        for i in range(len(l2)):
            sd2[i + 1] = l2[i] + sd2[i]
        for i in range(s2):
            for j in range(l2[s2 - 1 - i] + 1, 10):
                if sd2[s2 - 1 - i] + j <= max_sum:
                    if i == 0:
                        if sd2[s2 - 1 - i] + j >= min_sum:
                            r2 += 1
                    else:
                        for k in range(i):
                            r2 += (dp[k][max_sum - sd2[s2 - 1 - i] - j] - (dp[k][min_sum - sd2[s2 - 1 - i] - j - 1] if min_sum - sd2[s2 - 1 - i] - j - 1 >= 0 else 0))
                else:
                    break
        res = 0
        for i in range(s2):
            res += dp[i][-1] - dp[i][min_sum - 1]
        res = max(0, res - r1 - r2)
        return res % (10 ** 9 + 7)



if __name__ == "__main__":
    num1 = "1479"
    num2 = "5733"
    min_num = 36
    max_num = 108

    test = Solution().count(num1, num2, min_num, max_num)

    print(test)
