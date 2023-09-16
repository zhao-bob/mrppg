import collections
import heapq
import math
from bisect import bisect_right
from collections import Counter, deque
from functools import cache
from itertools import product
from typing import List, Optional


# 1222. 可以攻击国王的皇后
# 提示
# 中等
# 64
# 相关企业
# 在一个 8x8 的棋盘上，放置着若干「黑皇后」和一个「白国王」。
#
# 给定一个由整数坐标组成的数组 queens ，表示黑皇后的位置；以及一对坐标 king ，表示白国王的位置，返回所有可以攻击国王的皇后的坐标(任意顺序)。
#
#
#
# 示例 1：
#
#
#
# 输入：queens = [[0,1],[1,0],[4,0],[0,4],[3,3],[2,4]], king = [0,0]
# 输出：[[0,1],[1,0],[3,3]]
# 解释：
# [0,1] 的皇后可以攻击到国王，因为他们在同一行上。
# [1,0] 的皇后可以攻击到国王，因为他们在同一列上。
# [3,3] 的皇后可以攻击到国王，因为他们在同一条对角线上。
# [0,4] 的皇后无法攻击到国王，因为她被位于 [0,1] 的皇后挡住了。
# [4,0] 的皇后无法攻击到国王，因为她被位于 [1,0] 的皇后挡住了。
# [2,4] 的皇后无法攻击到国王，因为她和国王不在同一行/列/对角线上。
# 示例 2：
#
#
#
# 输入：queens = [[0,0],[1,1],[2,2],[3,4],[3,5],[4,4],[4,5]], king = [3,3]
# 输出：[[2,2],[3,4],[4,4]]
# 示例 3：
#
#
#
# 输入：queens = [[5,6],[7,7],[2,1],[0,7],[1,6],[5,1],[3,7],[0,3],[4,0],[1,2],[6,3],[5,0],[0,4],[2,2],[1,1],[6,4],[5,4],[0,0],[2,6],[4,5],[5,2],[1,4],[7,5],[2,3],[0,5],[4,2],[1,0],[2,7],[0,1],[4,6],[6,1],[0,6],[4,3],[1,7]], king = [3,4]
# 输出：[[2,3],[1,4],[1,6],[3,7],[4,3],[5,4],[4,5]]

class Solution:
    def queensAttacktheKing(self, queens: List[List[int]], king: List[int]) -> List[List[int]]:
        res = []
        q = {(q[0], q[1]) for q in queens}
        k = 1
        d = set()
        while k < 8:
            for i in [-1, 0, 1]:
                for j in [-1, 0, 1]:
                    if (i != 0 or j != 0) and (i, j) not in d:
                        if 0 <= king[0] + i * k < 8 and 0 <= king[1] + j * k < 8 and (king[0] + i * k, king[1] + j * k) in q:
                            res.append([king[0] + i * k, king[1] + j * k])
                            d.add((i, j))
            k += 1
        return res


if __name__ == "__main__":
    queens = [[5,6],[7,7],[2,1],[0,7],[1,6],[5,1],[3,7],[0,3],[4,0],[1,2],[6,3],[5,0],[0,4],[2,2],[1,1],[6,4],[5,4],[0,0],[2,6],[4,5],[5,2],[1,4],[7,5],[2,3],[0,5],[4,2],[1,0],[2,7],[0,1],[4,6],[6,1],[0,6],[4,3],[1,7]]
    king = [3,4]
    test = Solution().queensAttacktheKing(queens, king)

    print(test)
