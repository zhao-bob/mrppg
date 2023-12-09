import heapq
import math
from collections import Counter
from typing import List
from sortedcontainers import SortedList


# 2652. 倍数求和
# 提示
# 简单
# 17
# 相关企业
# 给你一个正整数 n ，请你计算在 [1，n] 范围内能被 3、5、7 整除的所有整数之和。
#
# 返回一个整数，用于表示给定范围内所有满足约束条件的数字之和。
#
#
#
# 示例 1：
#
# 输入：n = 7
# 输出：21
# 解释：在 [1, 7] 范围内能被 3、5、7 整除的所有整数分别是 3、5、6、7 。数字之和为 21 。
# 示例 2：
#
# 输入：n = 10
# 输出：40
# 解释：在 [1, 10] 范围内能被 3、5、7 整除的所有整数分别是 3、5、6、7、9、10 。数字之和为 40 。
# 示例 3：
#
# 输入：n = 9
# 输出：30
# 解释：在 [1, 9] 范围内能被 3、5、7 整除的所有整数分别是 3、5、6、7、9 。数字之和为 30 。
#


class Solution:
    def sumOfMultiples(self, n: int) -> int:
        res = 0
        for i in range(1, n + 1):
            if i % 3 == 0 or i % 5 == 0 or i % 7 == 0:
                res += i
        return res


if __name__ == "__main__":
    n = 10
    test = Solution().sumOfMultiples(n)
    print(test)
