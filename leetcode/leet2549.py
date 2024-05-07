# 2549. 统计桌面上的不同数字
# 简单
# 相关标签
# 相关企业
# 提示
# 给你一个正整数 n ，开始时，它放在桌面上。在 109 天内，每天都要执行下述步骤：
#
# 对于出现在桌面上的每个数字 x ，找出符合 1 <= i <= n 且满足 x % i == 1 的所有数字 i 。
# 然后，将这些数字放在桌面上。
# 返回在 109 天之后，出现在桌面上的 不同 整数的数目。
#
# 注意：
#
# 一旦数字放在桌面上，则会一直保留直到结束。
# % 表示取余运算。例如，14 % 3 等于 2 。
#
#
# 示例 1：
#
# 输入：n = 5
# 输出：4
# 解释：最开始，5 在桌面上。
# 第二天，2 和 4 也出现在桌面上，因为 5 % 2 == 1 且 5 % 4 == 1 。
# 再过一天 3 也出现在桌面上，因为 4 % 3 == 1 。
# 在十亿天结束时，桌面上的不同数字有 2 、3 、4 、5 。
# 示例 2：
#
# 输入：n = 3
# 输出：2
# 解释：
# 因为 3 % 2 == 1 ，2 也出现在桌面上。
# 在十亿天结束时，桌面上的不同数字只有两个：2 和 3 。
#
#
# 提示：
#
# 1 <= n <= 100
#

import heapq
import math
from collections import Counter, deque, defaultdict
from datetime import date
from functools import cache
from typing import List, Optional

from sortedcontainers import SortedList


class Solution:
    def distinctIntegers(self, n: int) -> int:
        return 1 if n == 1 else n - 1

if __name__ == "__main__":
    n = 5
    test = Solution().distinctIntegers(n)
    print(test)
