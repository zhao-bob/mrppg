import heapq
import math
from collections import Counter, deque
from functools import cache
from itertools import product
from typing import List, Optional


# 1444. 切披萨的方案数
# 提示
# 困难
# 123
# 相关企业
# 给你一个 rows x cols 大小的矩形披萨和一个整数 k ，矩形包含两种字符： 'A' （表示苹果）和 '.' （表示空白格子）。你需要切披萨 k-1 次，得到 k 块披萨并送给别人。
#
# 切披萨的每一刀，先要选择是向垂直还是水平方向切，再在矩形的边界上选一个切的位置，将披萨一分为二。如果垂直地切披萨，那么需要把左边的部分送给一个人，如果水平地切，那么需要把上面的部分送给一个人。在切完最后一刀后，需要把剩下来的一块送给最后一个人。
#
# 请你返回确保每一块披萨包含 至少 一个苹果的切披萨方案数。由于答案可能是个很大的数字，请你返回它对 10^9 + 7 取余的结果。
#
#
#
# 示例 1：
#
#
#
# 输入：pizza = ["A..","AAA","..."], k = 3
# 输出：3
# 解释：上图展示了三种切披萨的方案。注意每一块披萨都至少包含一个苹果。
# 示例 2：
#
# 输入：pizza = ["A..","AA.","..."], k = 3
# 输出：1
# 示例 3：
#
# 输入：pizza = ["A..","A..","..."], k = 1
# 输出：1

class Solution:
    def ways(self, pizza: List[str], k: int) -> int:
        # aps = [[0 for _ in range(len(pizza[0]) + 1)] for _ in range(len(pizza) + 1)]
        # t = 0
        # for i in range(1, len(pizza) + 1):
        #     for j in range(1, len(pizza[0]) + 1):
        #         if pizza[i - 1][j - 1] == "A":
        #             aps[i][j] = 1 + aps[i][j - 1] + aps[i - 1][j] - aps[i - 1][j - 1]
        #             t += 1
        #         else:
        #             aps[i][j] = aps[i][j - 1] + aps[i - 1][j] - aps[i - 1][j - 1]
        #
        # @cache
        # def divide(r, c, t, k):
        #     if k == 1:
        #         return 1
        #     res = 0
        #     for i in range(r + 1, len(aps)):
        #         a = aps[i][-1] - aps[i][c] - (aps[r][-1] - aps[r][c])
        #         if a > 0 and t - a >= k - 1:
        #             res += divide(i, c, t - a, k - 1)
        #     for i in range(c + 1, len(aps[0])):
        #         a = aps[-1][i] - aps[r][i] - (aps[-1][c] - aps[r][c])
        #         if a > 0 and t - a >= k - 1:
        #             res += divide(r, i, t - a, k - 1)
        #     return res % 1000000007
        #
        # if t < k:
        #     return 0
        # return divide(0, 0, t, k)

        aps = [[0 for _ in range(len(pizza[0]) + 1)] for _ in range(len(pizza) + 1)]
        dp = [[[0 for _ in range(len(pizza[0]))] for _ in range(len(pizza))] for _ in range(k)]
        for i in range(len(pizza) - 1, -1, -1):
            for j in range(len(pizza[0]) - 1, -1, -1):
                aps[i][j] = (pizza[i][j] == 'A') + aps[i][j + 1] + aps[i + 1][j] - aps[i + 1][j + 1]
                dp[0][i][j] = 1 if aps[i][j] > 0 else 0

        for k in range(1, k):
            for i in range(len(pizza)):
                for j in range(len(pizza[0])):
                    # 水平方向切
                    for i2 in range(i + 1, len(pizza)):
                        if aps[i][j] > aps[i2][j]:
                            dp[k][i][j] = (dp[k][i][j] + dp[k - 1][i2][j]) % (10 ** 9 + 7)
                    # 垂直方向切
                    for j2 in range(j + 1, len(pizza[0])):
                        if aps[i][j] > aps[i][j2]:
                            dp[k][i][j] = (dp[k][i][j] + dp[k - 1][i][j2]) % (10 ** 9 + 7)

        return dp[-1][0][0]


if __name__ == "__main__":
    pizza = ["AAAA","AAAA","AAAA"]
    k = 4

    test = Solution().ways(pizza, k)

    print(test)
