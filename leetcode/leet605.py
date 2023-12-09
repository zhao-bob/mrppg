import collections
import heapq
import math
from bisect import bisect_right, bisect_left
from collections import Counter, deque
from functools import cache
from itertools import product
from typing import List, Optional


# 605. 种花问题
# 简单
# 640
# 相关企业
# 假设有一个很长的花坛，一部分地块种植了花，另一部分却没有。可是，花不能种植在相邻的地块上，它们会争夺水源，两者都会死去。
#
# 给你一个整数数组 flowerbed 表示花坛，由若干 0 和 1 组成，其中 0 表示没种植花，1 表示种植了花。另有一个数 n ，能否在不打破种植规则的情况下种入 n 朵花？能则返回 true ，不能则返回 false 。
#
#
#
# 示例 1：
#
# 输入：flowerbed = [1,0,0,0,1], n = 1
# 输出：true
# 示例 2：
#
# 输入：flowerbed = [1,0,0,0,1], n = 2
# 输出：false

class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        # k = 0
        # for i in range(len(flowerbed)):
        #     if flowerbed[i] == 0:
        #         pre = 0
        #         nxt = 0
        #         if i - 1 >= 0:
        #             pre = flowerbed[i - 1]
        #         if i + 1 < len(flowerbed):
        #             nxt = flowerbed[i + 1]
        #         if pre + nxt == 0:
        #             k += 1
        #             flowerbed[i] = 1
        # return k >= n
        k = 0
        for i in range(len(flowerbed)):
            if flowerbed[i] == 0 and (i == 0 or flowerbed[i - 1] == 0) and (i + 1 == len(flowerbed) or flowerbed[i + 1] == 0):
                k += 1
                flowerbed[i] = 1
        return k >= n


if __name__ == "__main__":
    flowerbed = [1,0,0,0,0,1]
    n = 2
    test = Solution().canPlaceFlowers(flowerbed, n)
    print(test)
