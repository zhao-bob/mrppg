import heapq
import math
from typing import List


# 2132. 用邮票贴满网格图
# 提示
# 困难
# 74
# 相关企业
# 给你一个 m x n 的二进制矩阵 grid ，每个格子要么为 0 （空）要么为 1 （被占据）。
#
# 给你邮票的尺寸为 stampHeight x stampWidth 。我们想将邮票贴进二进制矩阵中，且满足以下 限制 和 要求 ：
#
# 覆盖所有 空 格子。
# 不覆盖任何 被占据 的格子。
# 我们可以放入任意数目的邮票。
# 邮票可以相互有 重叠 部分。
# 邮票不允许 旋转 。
# 邮票必须完全在矩阵 内 。
# 如果在满足上述要求的前提下，可以放入邮票，请返回 true ，否则返回 false 。
#
#
#
# 示例 1：
#
#
#
# 输入：grid = [[1,0,0,0],[1,0,0,0],[1,0,0,0],[1,0,0,0],[1,0,0,0]], stampHeight = 4, stampWidth = 3
# 输出：true
# 解释：我们放入两个有重叠部分的邮票（图中标号为 1 和 2），它们能覆盖所有与空格子。
# 示例 2：
#
#
#
# 输入：grid = [[1,0,0,0],[0,1,0,0],[0,0,1,0],[0,0,0,1]], stampHeight = 2, stampWidth = 2
# 输出：false
# 解释：没办法放入邮票覆盖所有的空格子，且邮票不超出网格图以外。
#


class Solution:
    def possibleToStamp(self, grid: List[List[int]], stampHeight: int, stampWidth: int) -> bool:
        if stampHeight == 1 and stampWidth == 1:
            return True
        m = len(grid)
        n = len(grid[0])
        fillGrid = [[0] * n for _ in range(m)]

        def fill(i, j, h, w):
            for k in range(h):
                for l in range(w):
                    fillGrid[i + k][j + l] = 1

        def check(grid):
            for i in range(m):
                for j in range(n):
                    if grid[i][j] == 1:
                        if fillGrid[i][j] == 1:
                            return False
                    else:
                        if fillGrid[i][j] == 0:
                            if i - 1 >= 0 and j - 1 >= 0:
                                if grid[i - 1][j] == 1 and grid[i][j - 1] == 1:
                                    if i + stampHeight <= m and j + stampWidth <= n:
                                        fill(i, j, stampHeight, stampWidth)
                                    else:
                                        return False
                                elif grid[i - 1][j] == 1 and grid[i][j - 1] == 0:
                                    if i + stampHeight <= m:
                                        fill(i, j, stampHeight, 1)
                                    else:
                                        return False
                                elif grid[i - 1][j] == 0 and grid[i][j - 1] == 1:
                                    if j + stampWidth <= n:
                                        fill(i, j, 1, stampWidth)
                                    else:
                                        return False
                                else:
                                    fillGrid[i][j] == 1
                            elif i - 1 >= 0 and j == 0:
                                if grid[i - 1][j] == 1:
                                    if i + stampHeight <= m and j + stampWidth <= n:
                                        fill(i, j, stampHeight, stampWidth)
                                    else:
                                        return False
                                else:
                                    if j + stampWidth <= n:
                                        fill(i, j, 1, stampWidth)
                                    else:
                                        return False
                            elif j - 1 >= 0 and i == 0:
                                if grid[i][j - 1] == 1:
                                    if i + stampHeight <= m and j + stampWidth <= n:
                                        fill(i, j, stampHeight, stampWidth)
                                    else:
                                        return False
                                else:
                                    if i + stampHeight <= m:
                                        fill(i, j, stampHeight, 1)
                                    else:
                                        return False
                            else:
                                if i + stampHeight <= m and j + stampWidth <= n:
                                    fill(i, j, stampHeight, stampWidth)
                                else:
                                    return False
            return True
        if not check(grid):
            return False
        else:
            fillGrid = [[0] * n for _ in range(m)]
            grid1 = [[0] * n for _ in range(m)]
            for i in range(m):
                for j in range(n):
                    grid1[i][j] = grid[m - 1 - i][n - 1 - j]
            return check(grid1)


if __name__ == "__main__":
    grid = [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 1, 0, 0], [0, 0, 0, 0, 1], [0, 0, 0, 1, 1]]
    stampHeight = 2
    stampWidth = 2
    test = Solution().possibleToStamp(grid, stampHeight, stampWidth)
    print(test)
