import math
from collections import deque, Counter
from itertools import pairwise
from typing import List


# 1072. 按列翻转得到最大值等行数
# 给定 m x n 矩阵 matrix 。
#
# 你可以从中选出任意数量的列并翻转其上的 每个 单元格。（即翻转后，单元格的值从 0 变成 1，或者从 1 变为 0 。）
#
# 返回 经过一些翻转后，行与行之间所有值都相等的最大行数 。
#
#
#
# 示例 1：
#
# 输入：matrix = [[0,1],[1,1]]
# 输出：1
# 解释：不进行翻转，有 1 行所有值都相等。
# 示例 2：
#
# 输入：matrix = [[0,1],[1,0]]
# 输出：2
# 解释：翻转第一列的值之后，这两行都由相等的值组成。
# 示例 3：
#
# 输入：matrix = [[0,0,0],[0,0,1],[1,1,0]]
# 输出：2
# 解释：翻转前两列的值之后，后两行由相等的值组成。
#

class Solution:
    def maxEqualRowsAfterFlips(self, matrix: List[List[int]]) -> int:
        lb = {}
        for i in range(len(matrix)):
            s = 0
            for j in range(len(matrix[0])):
                s = (s << 1) | (matrix[i][j] ^ matrix[i][0])
            if s in lb:
                lb[s] += 1
            else:
                lb[s] = 1
        return max([lb[x] for x in lb])

if __name__ == "__main__":
    matrix = [[0,1],[1,1]]
    test = Solution().maxEqualRowsAfterFlips(matrix)
    print(test)
