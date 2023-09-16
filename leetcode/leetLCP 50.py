import collections
import heapq
import math
from bisect import bisect_right
from collections import Counter, deque
from functools import cache
from itertools import product
from typing import List, Optional


# LCP 50. 宝石补给
# 简单
# 15
# 相关企业
# 欢迎各位勇者来到力扣新手村，在开始试炼之前，请各位勇者先进行「宝石补给」。
#
# 每位勇者初始都拥有一些能量宝石， gem[i] 表示第 i 位勇者的宝石数量。现在这些勇者们进行了一系列的赠送，operations[j] = [x, y] 表示在第 j 次的赠送中 第 x 位勇者将自己一半的宝石（需向下取整）赠送给第 y 位勇者。
#
# 在完成所有的赠送后，请找到拥有最多宝石的勇者和拥有最少宝石的勇者，并返回他们二者的宝石数量之差。
#
# 注意：
#
# 赠送将按顺序逐步进行。
# 示例 1：
#
# 输入：gem = [3,1,2], operations = [[0,2],[2,1],[2,0]]
#
# 输出：2
#
# 解释： 第 1 次操作，勇者 0 将一半的宝石赠送给勇者 2， gem = [2,1,3] 第 2 次操作，勇者 2 将一半的宝石赠送给勇者 1， gem = [2,2,2] 第 3 次操作，勇者 2 将一半的宝石赠送给勇者 0， gem = [3,2,1] 返回 3 - 1 = 2
#
# 示例 2：
#
# 输入：gem = [100,0,50,100], operations = [[0,2],[0,1],[3,0],[3,0]]
#
# 输出：75
#
# 解释： 第 1 次操作，勇者 0 将一半的宝石赠送给勇者 2， gem = [50,0,100,100] 第 2 次操作，勇者 0 将一半的宝石赠送给勇者 1， gem = [25,25,100,100] 第 3 次操作，勇者 3 将一半的宝石赠送给勇者 0， gem = [75,25,100,50] 第 4 次操作，勇者 3 将一半的宝石赠送给勇者 0， gem = [100,25,100,25] 返回 100 - 25 = 75
#
# 示例 3：
#
# 输入：gem = [0,0,0,0], operations = [[1,2],[3,1],[1,2]]
#
# 输出：0

class Solution:
    def giveGem(self, gem: List[int], operations: List[List[int]]) -> int:
        for o in operations:
            gem[o[1]] += gem[o[0]] // 2
            gem[o[0]] -= gem[o[0]] // 2
        return max(gem) - min(gem)


if __name__ == "__main__":
    gem = [0,0,0,0]
    operations = [[1,2],[3,1],[1,2]]
    test = Solution().giveGem(gem, operations)

    print(test)
