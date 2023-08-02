from collections import Counter
from typing import List


# 剑指 Offer 47. 礼物的最大价值

# 在一个 m*n 的棋盘的每一格都放有一个礼物，每个礼物都有一定的价值（价值大于 0）。你可以从棋盘的左上角开始拿格子里的礼物，并每次向右或者向下移动一格、直到到达棋盘的右下角。给定一个棋盘及其上面的礼物的价值，请计算你最多能拿到多少价值的礼物？
#
#  
#
# 示例 1:
#
# 输入:
# [
#   [1,3,1],
#   [1,5,1],
#   [4,2,1]
# ]
# 输出: 12
# 解释: 路径 1→3→5→2→1 可以拿到最多价值的礼物
#

class Solution:
    def maxValue(self, grid: List[List[int]]) -> int:
        length = len(grid[0])
        width = len(grid)
        dp = [[0 for _ in range(length)] for _ in range(width)]
        dp[0][0] = grid[0][0]
        for i in range(1, length):
            dp[0][i] = grid[0][i] + dp[0][i - 1]
        for i in range(1, width):
            dp[i][0] = grid[i][0] + + dp[i - 1][0]

        for i in range(1, width):
            for j in range(1, length):
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1]) + grid[i][j]
        return dp[width - 1][length - 1]


if __name__ == "__main__":
    grid = [
        [1, 3, 1],
        [1, 5, 1],
        [4, 2, 1]
    ]
    test = Solution().maxValue(grid)
    print(test)
