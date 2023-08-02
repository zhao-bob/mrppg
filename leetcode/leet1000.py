import math
from functools import lru_cache
from typing import List


# 1000. 合并石头的最低成本
# 有 N 堆石头排成一排，第 i 堆中有 stones[i] 块石头。
#
# 每次移动（move）需要将连续的 K 堆石头合并为一堆，而这个移动的成本为这 K 堆石头的总数。
#
# 找出把所有石头合并成一堆的最低成本。如果不可能，返回 -1 。
#
#
#
# 示例 1：
#
# 输入：stones = [3,2,4,1], K = 2
# 输出：20
# 解释：
# 从 [3, 2, 4, 1] 开始。
# 合并 [3, 2]，成本为 5，剩下 [5, 4, 1]。
# 合并 [4, 1]，成本为 5，剩下 [5, 5]。
# 合并 [5, 5]，成本为 10，剩下 [10]。
# 总成本 20，这是可能的最小值。
# 示例 2：
#
# 输入：stones = [3,2,4,1], K = 3
# 输出：-1
# 解释：任何合并操作后，都会剩下 2 堆，我们无法再进行合并。所以这项任务是不可能完成的。.
# 示例 3：
#
# 输入：stones = [3,5,1,2,6], K = 3
# 输出：25
# 解释：
# 从 [3, 5, 1, 2, 6] 开始。
# 合并 [5, 1, 2]，成本为 8，剩下 [3, 8, 6]。
# 合并 [3, 8, 6]，成本为 17，剩下 [17]。
# 总成本 25，这是可能的最小值。
#

class Solution:
    def mergeStones(self, stones: List[int], k: int) -> int:
        n = len(stones)
        if (n - 1) % (k - 1) != 0:
            return -1

        d = [[[math.inf] * (k + 1) for _ in range(n)] for _ in range(n)]
        sum = [0] * n
        s = 0
        for i in range(n):
            d[i][i][1] = 0
            s += stones[i]
            sum[i] = s

        for L in range(2, n + 1):
            for l in range(n - L + 1):
                r = l + L - 1
                for t in range(2, k + 1):
                    for p in range(l, r, k - 1):
                        d[l][r][t] = min(d[l][r][t], d[l][p][1] + d[p + 1][r][t - 1])
                d[l][r][1] = min(d[l][r][1], d[l][r][k] + (sum[r] - (0 if l == 0 else sum[l - 1])))
        return d[0][n - 1][1]


if __name__ == "__main__":
    stones = [6,4,4,6]
    K = 2

    test = Solution().mergeStones(stones, K)
    print(test)
