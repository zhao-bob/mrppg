from typing import List

# 1139. 最大的以 1 为边界的正方形

# 给你一个由若干 0 和 1 组成的二维网格grid，请你找出边界全部由 1 组成的最大 正方形 子网格，并返回该子网格中的元素数量。如果不存在，则返回 0。
#
#
# 示例 1：
#
# 输入：grid = [[1,1,1],[1,0,1],[1,1,1]]
# 输出：9
# 示例 2：
#
# 输入：grid = [[1,1,0,0]]
# 输出：1


class Solution:
    def largest1BorderedSquare(self, grid: List[List[int]]) -> int:
        width = len(grid)
        length = len(grid[0])
        lData = [[0] * length for _ in range(width)]
        for i in range(width):
            l = 0
            for j in range(length):
                if grid[i][length - 1- j] == 1:
                    l += 1
                else:
                    l = 0
                lData[i][length - 1 - j] = l
        wData = [[0] * length for _ in range(width)]
        for i in range(length):
            l = 0
            for j in range(width):
                if grid[width - 1 - j][i] == 1:
                    l += 1
                else:
                    l = 0
                wData[width - 1 - j][i] = l
        print(lData)
        print(wData)

        res = 0
        for i in range(width):
            for j in range(length):
                print(i, j)
                s = min(lData[i][j], wData[i][j])
                r = 0
                if s > 1:
                    for k in range(s - 1):
                        if lData[i + k +1][j + k + 1] != 0 and lData[i + k + 1][j] > k and wData[i][j + k + 1] >k:
                            r = (k+2) * (k+2)
                else:
                    r = s
                if r > res:
                    res = r
        return res


if __name__ == "__main__":
    grid = [[0,0],[0,1]]
    test = Solution().largest1BorderedSquare(grid)
    print(test)
