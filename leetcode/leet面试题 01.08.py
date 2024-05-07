import heapq
import math
from collections import deque
from typing import List


# 面试题 01.08. 零矩阵
# 中等
# 相关标签
# 相关企业
# 提示
# 编写一种算法，若M × N矩阵中某个元素为0，则将其所在的行与列清零。
#
#
#
# 示例 1：
#
# 输入：
# [
#   [1,1,1],
#   [1,0,1],
#   [1,1,1]
# ]
# 输出：
# [
#   [1,0,1],
#   [0,0,0],
#   [1,0,1]
# ]
# 示例 2：
#
# 输入：
# [
#   [0,1,2,0],
#   [3,4,5,2],
#   [1,3,1,5]
# ]
# 输出：
# [
#   [0,0,0,0],
#   [0,4,5,0],
#   [0,3,1,0]
# ]
#


class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        m = len(matrix[0])

        r = [0] * n
        c = [0] * m

        for i in range(n):
            for j in range(m):
                if matrix[i][j] == 0:
                    r[i] = 1
                    break
        for i in range(m):
            for j in range(n):
                if matrix[j][i] == 0:
                    c[i] = 1
                    break
        for i in range(n):
            if r[i] == 1:
                for j in range(m):
                    matrix[i][j] = 0
        for j in range(m):
            if c[j] == 1:
                for i in range(n):
                    matrix[i][j] = 0


if __name__ == "__main__":
    matrix = [
        [1, 1, 1],
        [1, 0, 1],
        [1, 1, 1]
    ]
    Solution().setZeroes(matrix)
    print(matrix)
