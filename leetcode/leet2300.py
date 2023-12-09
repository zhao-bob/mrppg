import heapq
import math
from collections import Counter, deque, defaultdict
from functools import cache, reduce
from itertools import product
from typing import List, Optional


# 2300. 咒语和药水的成功对数
# 提示
# 中等
# 42
# 相关企业
# 给你两个正整数数组 spells 和 potions ，长度分别为 n 和 m ，其中 spells[i] 表示第 i 个咒语的能量强度，potions[j] 表示第 j 瓶药水的能量强度。
#
# 同时给你一个整数 success 。一个咒语和药水的能量强度 相乘 如果 大于等于 success ，那么它们视为一对 成功 的组合。
#
# 请你返回一个长度为 n 的整数数组 pairs，其中 pairs[i] 是能跟第 i 个咒语成功组合的 药水 数目。
#
#
#
# 示例 1：
#
# 输入：spells = [5,1,3], potions = [1,2,3,4,5], success = 7
# 输出：[4,0,3]
# 解释：
# - 第 0 个咒语：5 * [1,2,3,4,5] = [5,10,15,20,25] 。总共 4 个成功组合。
# - 第 1 个咒语：1 * [1,2,3,4,5] = [1,2,3,4,5] 。总共 0 个成功组合。
# - 第 2 个咒语：3 * [1,2,3,4,5] = [3,6,9,12,15] 。总共 3 个成功组合。
# 所以返回 [4,0,3] 。
# 示例 2：
#
# 输入：spells = [3,1,2], potions = [8,5,8], success = 16
# 输出：[2,0,2]
# 解释：
# - 第 0 个咒语：3 * [8,5,8] = [24,15,24] 。总共 2 个成功组合。
# - 第 1 个咒语：1 * [8,5,8] = [8,5,8] 。总共 0 个成功组合。
# - 第 2 个咒语：2 * [8,5,8] = [16,10,16] 。总共 2 个成功组合。
# 所以返回 [2,0,2] 。
#
#

class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        l = len(spells)
        lp = len(potions)
        sortedSpells = sorted([(s, i) for i, s in enumerate(spells)], key=lambda x: x[0], reverse=True)
        potions.sort()
        res = [0] * l
        pre = (-1, -1)
        left = 0
        for i in range(l):
            if sortedSpells[i][0] == pre[0]:
                res[sortedSpells[i][1]] = res[pre[1]]
            else:
                p = success // sortedSpells[i][0] if success % sortedSpells[i][0] == 0 else success // sortedSpells[i][0] + 1

                right = lp
                while left < right:
                    mid = (left + right) // 2
                    if potions[mid] < p:
                        left = mid + 1
                    else:
                        right = mid
                res[sortedSpells[i][1]] = lp - left
                pre = sortedSpells[i]
        return res


if __name__ == "__main__":
    spells = list(range(1, 100000))
    potions = list(range(1, 100000))
    success = 100000
    test = Solution().successfulPairs(spells, potions, success)
    print(test)
