# 1349. 参加考试的最大学生数
# 提示
# 困难
# 170
# 相关企业
# 给你一个 m * n 的矩阵 seats 表示教室中的座位分布。如果座位是坏的（不可用），就用 '#' 表示；否则，用 '.' 表示。
#
# 学生可以看到左侧、右侧、左上、右上这四个方向上紧邻他的学生的答卷，但是看不到直接坐在他前面或者后面的学生的答卷。请你计算并返回该考场可以容纳的同时参加考试且无法作弊的 最大 学生人数。
#
# 学生必须坐在状况良好的座位上。
#
#
#
# 示例 1：
#
#
#
# 输入：seats = [["#",".","#","#",".","#"],
#               [".","#","#","#","#","."],
#               ["#",".","#","#",".","#"]]
# 输出：4
# 解释：教师可以让 4 个学生坐在可用的座位上，这样他们就无法在考试中作弊。
# 示例 2：
#
# 输入：seats = [[".","#"],
#               ["#","#"],
#               ["#","."],
#               ["#","#"],
#               [".","#"]]
# 输出：3
# 解释：让所有学生坐在可用的座位上。
# 示例 3：
#
# 输入：seats = [["#",".",".",".","#"],
#               [".","#",".","#","."],
#               [".",".","#",".","."],
#               [".","#",".","#","."],
#               ["#",".",".",".","#"]]
# 输出：10
# 解释：让学生坐在第 1、3 和 5 列的可用座位上。
#
import heapq
import math
from typing import List


class Solution:
    def maxStudents(self, seats: List[List[str]]) -> int:
        m = len(seats)
        n = len(seats[0])
        sq = [0] * n
        for i in range(n):
            s = 0
            a = 1
            for j in range(m):
                if seats[j][i] == '.':
                    s |= a
                a <<= 1
            sq[i] = s
        states = [[0] * (2 ** m) for _ in range(n)]
        for i in range(n):
            sub = valid = sq[i]
            while sub:
                if i == 0:
                    states[i][sub] = sub.bit_count()
                else:
                    t = sub
                    mask = 2 ** m - 1
                    j = -1
                    bc = 0
                    while t:
                        b = t & 1
                        if b == 1:
                            if j == -1:
                                mask &= ~0b11
                            else:
                                mask &= ~(7 << j)
                            bc += 1
                        j += 1
                        t >>= 1
                    ss = v = mask & sq[i - 1]
                    while ss:
                        states[i][sub] = max(states[i][sub], bc + states[i - 1][ss])
                        ss = (ss - 1) & v
                    else:
                        states[i][sub] = max(states[i][sub], bc + states[i - 1][ss])
                sub = (sub - 1) & valid
            else:
                if i > 0:
                    states[i][sub] = max(states[i - 1])
        return max(states[-1])


if __name__ == "__main__":
    seats = [["#","#",".",".","."],["#",".",".","#","."],[".","#",".",".","#"],[".","#","#","#","#"],[".",".","#",".","."]]
    test = Solution().maxStudents(seats)
    print(test)
