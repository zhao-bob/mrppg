import heapq
import math
from collections import Counter
from functools import cache
from typing import List, Optional
from sortedcontainers import SortedList


# 2661. 找出叠涂元素
# 提示
# 中等
# 26
# 相关企业
# 给你一个下标从 0 开始的整数数组 arr 和一个 m x n 的整数 矩阵 mat 。arr 和 mat 都包含范围 [1，m * n] 内的 所有 整数。
#
# 从下标 0 开始遍历 arr 中的每个下标 i ，并将包含整数 arr[i] 的 mat 单元格涂色。
#
# 请你找出 arr 中在 mat 的某一行或某一列上都被涂色且下标最小的元素，并返回其下标 i 。
#
#
#
# 示例 1：
#
# image explanation for example 1
# 输入：arr = [1,3,4,2], mat = [[1,4],[2,3]]
# 输出：2
# 解释：遍历如上图所示，arr[2] 在矩阵中的第一行或第二列上都被涂色。
# 示例 2：
#
# image explanation for example 2
# 输入：arr = [2,8,7,4,1,3,5,6,9], mat = [[3,2,5],[1,4,6],[8,7,9]]
# 输出：3
# 解释：遍历如上图所示，arr[3] 在矩阵中的第二列上都被涂色。
#

class Solution:
    def firstCompleteIndex(self, arr: List[int], mat: List[List[int]]) -> int:
        m = len(mat)
        n = len(mat[0])

        pos = {}
        for i in range(m):
            for j in range(n):
                pos[mat[i][j]] = (i, j)

        c = [0] * (m + n)
        for k in range(len(arr)):
            row, column = pos[arr[k]]
            c[row] += 1
            c[m + column] += 1
            if c[row] == n or c[m + column] == m:
                return k
        return -1


if __name__ == "__main__":
    arr = [2,8,7,4,1,3,5,6,9]
    mat = [[3,2,5],[1,4,6],[8,7,9]]
    test = Solution().firstCompleteIndex(arr, mat)
    print(test)
