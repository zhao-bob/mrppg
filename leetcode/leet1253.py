import heapq
import math
from collections import Counter, deque
from functools import cache
from itertools import product
from typing import List, Optional


# 1253. 重构 2 行二进制矩阵
# 给你一个 2 行 n 列的二进制数组：
#
# 矩阵是一个二进制矩阵，这意味着矩阵中的每个元素不是 0 就是 1。
# 第 0 行的元素之和为 upper。
# 第 1 行的元素之和为 lower。
# 第 i 列（从 0 开始编号）的元素之和为 colsum[i]，colsum 是一个长度为 n 的整数数组。
# 你需要利用 upper，lower 和 colsum 来重构这个矩阵，并以二维整数数组的形式返回它。
#
# 如果有多个不同的答案，那么任意一个都可以通过本题。
#
# 如果不存在符合要求的答案，就请返回一个空的二维数组。
#
#
#
# 示例 1：
#
# 输入：upper = 2, lower = 1, colsum = [1,1,1]
# 输出：[[1,1,0],[0,0,1]]
# 解释：[[1,0,1],[0,1,0]] 和 [[0,1,1],[1,0,0]] 也是正确答案。
# 示例 2：
#
# 输入：upper = 2, lower = 3, colsum = [2,2,1,1]
# 输出：[]
# 示例 3：
#
# 输入：upper = 5, lower = 5, colsum = [2,1,2,0,1,0,1,2,0,1]
# 输出：[[1,1,1,0,1,0,0,1,0,0],[1,0,1,0,0,0,1,1,0,1]]
#

class Solution:
    def reconstructMatrix(self, upper: int, lower: int, colsum: List[int]) -> List[List[int]]:
        res = [[0 for _ in range(len(colsum))] for _ in range(2)]

        for i in range(len(colsum)):
            if lower < 0 or upper < 0:
                return []
            if colsum[i] % 2 == 0:
                res[0][i] = res[1][i] = colsum[i] // 2
                upper -= colsum[i] // 2
                lower -= colsum[i] // 2
            else:
                if upper >= lower:
                    res[0][i] = 1
                    upper -= 1
                else:
                    res[1][i] = 1
                    lower -= 1
        return res



if __name__ == "__main__":
    upper = 5
    lower = 5
    colsum = [2,1,2,0,1,0,1,2,0,1]

    test = Solution().reconstructMatrix(upper, lower,colsum)
    print(test)
