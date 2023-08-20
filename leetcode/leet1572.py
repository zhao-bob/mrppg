import heapq
import math
from collections import Counter, deque
from functools import cache
from itertools import product
from typing import List, Optional


# 1572. 矩阵对角线元素的和
# 简单
# 给你一个正方形矩阵 mat，请你返回矩阵对角线元素的和。
#
# 请你返回在矩阵主对角线上的元素和副对角线上且不在主对角线上元素的和。
#
#
#
# 示例  1：
#
#
#
# 输入：mat = [[1,2,3],
#             [4,5,6],
#             [7,8,9]]
# 输出：25
# 解释：对角线的和为：1 + 5 + 9 + 3 + 7 = 25
# 请注意，元素 mat[1][1] = 5 只会被计算一次。
# 示例  2：
#
# 输入：mat = [[1,1,1,1],
#             [1,1,1,1],
#             [1,1,1,1],
#             [1,1,1,1]]
# 输出：8
# 示例 3：
#
# 输入：mat = [[5]]
# 输出：5

class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        res = 0

        for i in range(len(mat)):
            res += mat[i][i]
            if i != len(mat) - 1 - i:
                res += mat[i][len(mat) - 1 - i]
        return res



if __name__ == "__main__":
    mat = [[1, 2, 3],
           [4, 5, 6],
           [7, 8, 9]]

    test = Solution().diagonalSum(mat)
    print(test)
