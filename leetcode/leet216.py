import heapq
import math
from collections import deque, Counter
from itertools import count
from typing import List


# 216. 组合总和 III
# 中等
# 相关标签
# 相关企业
# 找出所有相加之和为 n 的 k 个数的组合，且满足下列条件：
#
# 只使用数字1到9
# 每个数字 最多使用一次
# 返回 所有可能的有效组合的列表 。该列表不能包含相同的组合两次，组合可以以任何顺序返回。
#
#
#
# 示例 1:
#
# 输入: k = 3, n = 7
# 输出: [[1,2,4]]
# 解释:
# 1 + 2 + 4 = 7
# 没有其他符合的组合了。
# 示例 2:
#
# 输入: k = 3, n = 9
# 输出: [[1,2,6], [1,3,5], [2,3,4]]
# 解释:
# 1 + 2 + 6 = 9
# 1 + 3 + 5 = 9
# 2 + 3 + 4 = 9
# 没有其他符合的组合了。
# 示例 3:
#
# 输入: k = 4, n = 1
# 输出: []
# 解释: 不存在有效的组合。
# 在[1,9]范围内使用4个不同的数字，我们可以得到的最小和是1+2+3+4 = 10，因为10 > 1，没有有效的组合。
#
#
# 提示:
#
# 2 <= k <= 9
# 1 <= n <= 60
#


class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        # combination = [[] for _ in range(target)]
        #
        # for i in range(target):
        #     for c in candidates:
        #         if i > c - 1 and c <= (i + 1) // 2:
        #             if combination[i - c]:
        #                 for j in combination[i - c]:
        #                     combination[i].append(j + [c])
        #         elif i == c - 1:
        #             combination[i].append([c])
        # return combination[-1]
        res = []

        def combination(remain, ne, step, l):
            if remain == 0 and step == 0:
                res.append(l.copy())
                return
            if step == 0 and remain != 0:
                return
            for i in range(ne, 10):
                if remain - i >= 0:
                    l.append(i)
                    combination(remain - i, i + 1, step - 1, l)
                    l.pop()
                else:
                    break
        combination(n, 1, k, [])
        return res



if __name__ == "__main__":
    k = 3
    n = 7
    test = Solution().combinationSum3(k, n)
    print(test)
