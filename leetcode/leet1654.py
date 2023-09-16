import collections
import heapq
import math
from bisect import bisect_right
from collections import Counter, deque
from functools import cache
from itertools import product
from typing import List, Optional


# 1654. 到家的最少跳跃次数
# 提示
# 中等
# 101
# 相关企业
# 有一只跳蚤的家在数轴上的位置 x 处。请你帮助它从位置 0 出发，到达它的家。
#
# 跳蚤跳跃的规则如下：
#
# 它可以 往前 跳恰好 a 个位置（即往右跳）。
# 它可以 往后 跳恰好 b 个位置（即往左跳）。
# 它不能 连续 往后跳 2 次。
# 它不能跳到任何 forbidden 数组中的位置。
# 跳蚤可以往前跳 超过 它的家的位置，但是它 不能跳到负整数 的位置。
#
# 给你一个整数数组 forbidden ，其中 forbidden[i] 是跳蚤不能跳到的位置，同时给你整数 a， b 和 x ，请你返回跳蚤到家的最少跳跃次数。如果没有恰好到达 x 的可行方案，请你返回 -1 。
#
#
#
# 示例 1：
#
# 输入：forbidden = [14,4,18,1,15], a = 3, b = 15, x = 9
# 输出：3
# 解释：往前跳 3 次（0 -> 3 -> 6 -> 9），跳蚤就到家了。
# 示例 2：
#
# 输入：forbidden = [8,3,16,6,12,20], a = 15, b = 13, x = 11
# 输出：-1
# 示例 3：
#
# 输入：forbidden = [1,6,2,14,5,17,4], a = 16, b = 9, x = 7
# 输出：2
# 解释：往前跳一次（0 -> 16），然后往回跳一次（16 -> 7），跳蚤就到家了。

class Solution:
    def minimumJumps(self, forbidden: List[int], a: int, b: int, x: int) -> int:
        s = [[0, 0, 0]]
        f = set(forbidden)
        searched = set()
        upper = max(max(forbidden) + a + b, x)
        searched.add(0)
        while len(s) > 0:
            c = s[0]
            s = s[1:]
            if c[0] == x:
                return c[1]
            if c[0] + a not in searched:
                if c[0] + a - b <= x or (a - b < 0 and c[0] + a <= upper):
                    s.append([c[0] + a, c[1] + 1, 0])
                    searched.add(c[0] + a)
            if c[0] - b >= 0 and c[0] - b not in searched and c[2] < 1:
                s.append([c[0] - b, c[1] + 1, c[2] + 1])
                # searched.add(c[0] - b)
        return -1

        # s = [[0, 0, 0]]
        # f = set(forbidden)
        # searched = set()
        # upper = max(max(forbidden) + a + b, x)
        # searched.add(0)
        # while len(s) > 0:
        #     c = s[0]
        #     s = s[1:]
        #     if c[0] == x:
        #         return c[1]
        #     if c[0] + a not in f and c[0] + a not in searched:
        #         if c[0] + a - b <= x or (a - b < 0 and c[0] + a <= upper):
        #             s.append([c[0] + a, c[1] + 1, 0])
        #             searched.add(c[0] + a)
        #     if c[2] == 0 and c[0] - b >= 0 and - c[0] + b not in searched and c[0] - b not in f:
        #         s.append([c[0] - b, c[1] + 1, c[2] + 1])
        #         searched.add(- c[0] + b)
        # return -1

        # s = [(0, 0)]
        # f = set(forbidden)
        # searched = set()
        # searched.add((0, 0))
        # while len(s) > 0:
        #     c = s[0]
        #     s = s[1:]
        #     y = c[0] * a - c[1] * b
        #     f.add(y)
        #     if y == x:
        #         return c[0] + c[1]
        #     if (c[0] + 1, c[1]) not in searched and y + a not in f:
        #         if y + a - b <= x or a - b < 0:
        #             s.append((c[0] + 1, c[1]))
        #             searched.add((c[0] + 1, c[1]))
        #     if y - b >= 0 and c[1] + 1 <= c[0] and (c[0], c[1] + 1) not in searched and y - b not in f:
        #         s.append((c[0], c[1] + 1))
        #         searched.add((c[0], c[1] + 1))
        # return -1


if __name__ == "__main__":
    forbidden = [162, 118, 178, 152, 167, 100, 40, 74, 199, 186, 26, 73, 200, 127, 30, 124, 193, 84, 184, 36, 103, 149,
                 153, 9, 54, 154, 133, 95, 45, 198, 79, 157, 64, 122, 59, 71, 48, 177, 82, 35, 14, 176, 16, 108, 111, 6,
                 168, 31, 134, 164, 136, 72, 98]
    a = 29
    b = 98
    x = 80

    test = Solution().minimumJumps(forbidden, a, b, x)

    print(test)
