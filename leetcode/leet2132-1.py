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
        m, n = len(grid), len(grid[0])
        psum = [[0] * (n + 2) for _ in range(m + 2)]
        diff = [[0] * (n + 2) for _ in range(m + 2)]
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                psum[i][j] = psum[i - 1][j] + psum[i][j - 1] - psum[i - 1][j - 1] + grid[i - 1][j - 1]

        for i in range(1, m + 2 - stampHeight):
            for j in range(1, n + 2 - stampWidth):
                x = i + stampHeight - 1
                y = j + stampWidth - 1
                if psum[x][y] - psum[x][j - 1] - psum[i - 1][y] + psum[i - 1][j - 1] == 0:
                    diff[i][j] += 1
                    diff[i][y + 1] -= 1
                    diff[x + 1][j] -= 1
                    diff[x + 1][y + 1] += 1
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                diff[i][j] += diff[i - 1][j] + diff[i][j - 1] - diff[i - 1][j - 1]
                if diff[i][j] == 0 and grid[i - 1][j - 1] == 0:
                    return False
        return True


if __name__ == "__main__":
    grid = [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 1, 0, 0], [0, 0, 0, 0, 1], [0, 0, 0, 1, 1]]
    stampHeight = 2
    stampWidth = 2
    test = Solution().possibleToStamp(grid, stampHeight, stampWidth)
    print(test)
