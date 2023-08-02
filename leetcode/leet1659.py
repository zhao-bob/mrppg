import heapq
import math
from collections import Counter, deque
from functools import cache
from itertools import product
from typing import List, Optional


# 1659. 最大化网格幸福感
# 给你四个整数 m、n、introvertsCount 和 extrovertsCount 。有一个 m x n 网格，和两种类型的人：内向的人和外向的人。总共有 introvertsCount 个内向的人和 extrovertsCount 个外向的人。
#
# 请你决定网格中应当居住多少人，并为每个人分配一个网格单元。 注意，不必 让所有人都生活在网格中。
#
# 每个人的 幸福感 计算如下：
#
# 内向的人 开始 时有 120 个幸福感，但每存在一个邻居（内向的或外向的）他都会 失去  30 个幸福感。
# 外向的人 开始 时有 40 个幸福感，每存在一个邻居（内向的或外向的）他都会 得到  20 个幸福感。
# 邻居是指居住在一个人所在单元的上、下、左、右四个直接相邻的单元中的其他人。
#
# 网格幸福感 是每个人幸福感的 总和 。 返回 最大可能的网格幸福感 。
#
#
#
# 示例 1：
#
#
# 输入：m = 2, n = 3, introvertsCount = 1, extrovertsCount = 2
# 输出：240
# 解释：假设网格坐标 (row, column) 从 1 开始编号。
# 将内向的人放置在单元 (1,1) ，将外向的人放置在单元 (1,3) 和 (2,3) 。
# - 位于 (1,1) 的内向的人的幸福感：120（初始幸福感）- (0 * 30)（0 位邻居）= 120
# - 位于 (1,3) 的外向的人的幸福感：40（初始幸福感）+ (1 * 20)（1 位邻居）= 60
# - 位于 (2,3) 的外向的人的幸福感：40（初始幸福感）+ (1 * 20)（1 位邻居）= 60
# 网格幸福感为：120 + 60 + 60 = 240
# 上图展示该示例对应网格中每个人的幸福感。内向的人在浅绿色单元中，而外向的人在浅紫色单元中。
# 示例 2：
#
# 输入：m = 3, n = 1, introvertsCount = 2, extrovertsCount = 1
# 输出：260
# 解释：将内向的人放置在单元 (1,1) 和 (3,1) ，将外向的人放置在单元 (2,1) 。
# - 位于 (1,1) 的内向的人的幸福感：120（初始幸福感）- (1 * 30)（1 位邻居）= 90
# - 位于 (2,1) 的外向的人的幸福感：40（初始幸福感）+ (2 * 20)（2 位邻居）= 80
# - 位于 (3,1) 的内向的人的幸福感：120（初始幸福感）- (1 * 30)（1 位邻居）= 90
# 网格幸福感为 90 + 80 + 90 = 260
# 示例 3：
#
# 输入：m = 2, n = 2, introvertsCount = 4, extrovertsCount = 0
# 输出：240
#

class Solution:
    def getMaxGridHappiness(self, m: int, n: int, introvertsCount: int, extrovertsCount: int) -> int:
        @cache
        def dfs(pos: int, pre: int, ic: int, ec: int) -> int:
            if pos == m * n or (ic == 0 and ec == 0):
                return 0
            ans = 0
            up = pre // p
            left = 0 if pos % n == 0 else pre % 3
            for i in range(3):
                if (i == 1 and ic == 0) or (i == 2 and ec == 0):
                    continue
                cur = pre % p * 3 + i
                a = h[up][i] + h[left][i]
                b = dfs(pos + 1, cur, ic - (i == 1), ec - (i == 2))
                c = 0
                if i == 1:
                    c = 120
                elif i == 2:
                    c = 40
                ans = max(ans, a + b + c)
            return ans

        p = pow(3, n - 1)
        h = [[0, 0, 0], [0, -60, -10], [0, -10, 40]]
        return dfs(0, 0, introvertsCount, extrovertsCount)

    def getMaxGridHappiness1(self, m: int, n: int, introvertsCount: int, extrovertsCount: int) -> int:
        def cal(row, c, j):
            if c == '.':
                return 0
            d = {'I': -30, 'E': 20}
            res = 120 if c == 'I' else 40
            if row[0] != '.':
                res += -10 if row[0] != c else d[c] * 2
            if j and row[-1] != '.':
                res += -10 if row[-1] != c else d[c] * 2
            return res

        ct = Counter({('.' * n, 0, 0): 0})
        for i, j in product(range(m), range(n)):
            ct2 = Counter()
            for st, c in product(ct, '.IE'):
                row, a, b = st
                a, b = a + (c == 'I'), b + (c == 'E')
                if a <= introvertsCount and b <= extrovertsCount:
                    st2 = (row[1:] + c, a, b)
                    ct2[st2] = max(ct2[st2], ct[st] + cal(row, c, j))
            ct = ct2
        return max(ct.values())


if __name__ == "__main__":
    m = 2
    n = 3
    introvertsCount = 1
    extrovertsCount = 2

    test = Solution().getMaxGridHappiness1(m, n, introvertsCount, extrovertsCount)
    print(test)
