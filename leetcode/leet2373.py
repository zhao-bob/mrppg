from typing import List


# 2373. 矩阵中的局部最大值

# 给你一个大小为 n x n 的整数矩阵 grid 。
#
# 生成一个大小为 (n - 2) x (n - 2) 的整数矩阵  maxLocal ，并满足：
#
# maxLocal[i][j] 等于 grid 中以 i + 1 行和 j + 1 列为中心的 3 x 3 矩阵中的 最大值 。
# 换句话说，我们希望找出 grid 中每个 3 x 3 矩阵中的最大值。
#
# 返回生成的矩阵。
#
#  
#
# 示例 1：
#
#
#
# 输入：grid = [[9,9,8,1],[5,6,2,6],[8,2,6,4],[6,2,2,2]]
# 输出：[[9,9],[8,6]]
# 解释：原矩阵和生成的矩阵如上图所示。
# 注意，生成的矩阵中，每个值都对应 grid 中一个相接的 3 x 3 矩阵的最大值。
# 示例 2：
#
#
#
# 输入：grid = [[1,1,1,1,1],[1,1,1,1,1],[1,1,2,1,1],[1,1,1,1,1],[1,1,1,1,1]]
# 输出：[[2,2,2],[2,2,2],[2,2,2]]
# 解释：注意，2 包含在 grid 中每个 3 x 3 的矩阵中。
#


class Solution:
    def largestLocal(self, grid: List[List[int]]) -> List[List[int]]:
        length = len(grid)
        width = len(grid[0])

        res = [[0 for _ in range((length - 2))] for _ in range(width - 2)]

        for i in range(length - 2):
            for j in range(width - 2):
                res[i][j] = max([grid[k][l] for k in range(i, i + 3) for l in range(j, j + 3)])
        return res


if __name__ == "__main__":
    #
    grid = [[20, 8, 20, 6, 16, 16, 7, 16, 8, 10], [12, 15, 13, 10, 20, 9, 6, 18, 17, 6],
            [12, 4, 10, 13, 20, 11, 15, 5, 17, 1], [7, 10, 14, 14, 16, 5, 1, 7, 3, 11],
            [16, 2, 9, 15, 9, 8, 6, 1, 7, 15], [18, 15, 18, 8, 12, 17, 19, 7, 7, 8],
            [19, 11, 15, 16, 1, 3, 7, 4, 7, 11], [11, 6, 5, 14, 12, 18, 3, 20, 14, 6],
            [4, 4, 19, 6, 17, 12, 8, 8, 18, 8], [19, 15, 14, 11, 11, 13, 12, 6, 16, 19]]
    test = Solution().largestLocal(grid)
    print(test)
