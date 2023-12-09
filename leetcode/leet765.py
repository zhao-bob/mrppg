import heapq
import math
from collections import Counter, deque, defaultdict
from functools import cache, reduce
from itertools import product
from typing import List, Optional


# 765. 情侣牵手
# 提示
# 困难
# 446
# 相关企业
# n 对情侣坐在连续排列的 2n 个座位上，想要牵到对方的手。
#
# 人和座位由一个整数数组 row 表示，其中 row[i] 是坐在第 i 个座位上的人的 ID。情侣们按顺序编号，第一对是 (0, 1)，第二对是 (2, 3)，以此类推，最后一对是 (2n-2, 2n-1)。
#
# 返回 最少交换座位的次数，以便每对情侣可以并肩坐在一起。 每次交换可选择任意两人，让他们站起来交换座位。
#
#
#
# 示例 1:
#
# 输入: row = [0,2,1,3]
# 输出: 1
# 解释: 只需要交换row[1]和row[2]的位置即可。
# 示例 2:
#
# 输入: row = [3,2,0,1]
# 输出: 0
# 解释: 无需交换座位，所有的情侣都已经可以手牵手了。
#
#

class Solution:
    def minSwapsCouples(self, row: List[int]) -> int:
        p = {r: i for i, r in enumerate(row)}
        n = len(row) // 2
        res = 0
        for i in range(n):
            c = row[i * 2] + 1 if row[i * 2] % 2 == 0 else row[i * 2] - 1
            if p[c] != i * 2 + 1:
                res += 1
                row[p[c]] = row[i * 2 + 1]
                p[row[i * 2 + 1]] = p[c]
        return res


if __name__ == "__main__":
    row = [3,2,0,1]
    test = Solution().minSwapsCouples(row)
    print(test)
