import math
from bisect import bisect_right, bisect_left
from collections import defaultdict
from functools import lru_cache
from random import randint
from typing import List, Optional


# 1157. 子数组中占绝大多数的元素
# 设计一个数据结构，有效地找到给定子数组的 多数元素 。
#
# 子数组的 多数元素 是在子数组中出现 threshold 次数或次数以上的元素。
#
# 实现 MajorityChecker 类:
#
# MajorityChecker(int[] arr) 会用给定的数组 arr 对 MajorityChecker 初始化。
# int query(int left, int right, int threshold) 返回子数组中的元素  arr[left...right] 至少出现 threshold 次数，如果不存在这样的元素则返回 -1。
#
#
# 示例 1：
#
# 输入:
# ["MajorityChecker", "query", "query", "query"]
# [[[1, 1, 2, 2, 1, 1]], [0, 5, 4], [0, 3, 3], [2, 3, 2]]
# 输出：
# [null, 1, -1, 2]
#
# 解释：
# MajorityChecker majorityChecker = new MajorityChecker([1,1,2,2,1,1]);
# majorityChecker.query(0,5,4); // 返回 1
# majorityChecker.query(0,3,3); // 返回 -1
# majorityChecker.query(2,3,2); // 返回 2
#

class MajorityChecker:
    k = 20

    def __init__(self, arr: List[int]):
        self.arr = arr
        self.loc = defaultdict(list)

        for i, val in enumerate(arr):
            self.loc[val].append(i)

    def query(self, left: int, right: int, threshold: int) -> int:
        arr_ = self.arr
        loc_ = self.loc

        length = right - left + 1
        for i in range(MajorityChecker.k):
            x = arr_[randint(left, right)]
            pos = loc_[x]
            occ = bisect_right(pos, right) - bisect_left(pos, left)
            if occ >= threshold:
                return x
            elif occ * 2 >= length:
                return -1

        return -1

    # def __init__(self, arr: List[int]):
    #     self.d = arr
        # self.dp = [[{} for _ in range(len(arr))] for _ in range(len(arr))]
        # for i in range(len(arr)):
        #     a = self.dp[i][i]
        #     a[arr[i]] = 1
        #     self.dp[i][i] = a
        # for l in range(1, len(arr)):
        #     for i in range(len(arr) - l):
        #         a = self.dp[i][i + l - 1].copy()
        #         if arr[i + l] in a:
        #             a[arr[i + l]] += 1
        #             self.dp[i][i + l] = a
        #         else:
        #             a[arr[i + l]] = 1
        #             self.dp[i][i + l] = a

    # def query(self, left: int, right: int, threshold: int) -> int:
    #     a = self.d[left: right+1]
    #     c = {}
    #     for x in a:
    #         if x in c:
    #             c[x] += 1
    #         else:
    #             c[x] = 1
    #         if c[x] >= threshold:
    #             return x
    #     return -1
        # a = self.dp[left][right]
        # for x in a:
        #     if a[x] >= threshold:
        #         return x
        #
        # return -1


if __name__ == "__main__":
    d = [[[1,1,2,2,1,1]],[0,5,4],[0,3,3],[2,3,2]]
    mc = MajorityChecker(d[0][0])

    for i in range(1, len(d)):
        test = mc.query(d[i][0], d[i][1], d[i][2])
        print(test)
