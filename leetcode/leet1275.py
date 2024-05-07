# 1275. 找出井字棋的获胜者
# 简单
# 相关标签
# 相关企业
# 提示
# A 和 B 在一个 3 x 3 的网格上玩井字棋。
#
# 井字棋游戏的规则如下：
#
# 玩家轮流将棋子放在空方格 (" ") 上。
# 第一个玩家 A 总是用 "X" 作为棋子，而第二个玩家 B 总是用 "O" 作为棋子。
# "X" 和 "O" 只能放在空方格中，而不能放在已经被占用的方格上。
# 只要有 3 个相同的（非空）棋子排成一条直线（行、列、对角线）时，游戏结束。
# 如果所有方块都放满棋子（不为空），游戏也会结束。
# 游戏结束后，棋子无法再进行任何移动。
# 给你一个数组 moves，其中每个元素是大小为 2 的另一个数组（元素分别对应网格的行和列），它按照 A 和 B 的行动顺序（先 A 后 B）记录了两人各自的棋子位置。
#
# 如果游戏存在获胜者（A 或 B），就返回该游戏的获胜者；如果游戏以平局结束，则返回 "Draw"；如果仍会有行动（游戏未结束），则返回 "Pending"。
#
# 你可以假设 moves 都 有效（遵循井字棋规则），网格最初是空的，A 将先行动。
#
#
#
# 示例 1：
#
# 输入：moves = [[0,0],[2,0],[1,1],[2,1],[2,2]]
# 输出："A"
# 解释："A" 获胜，他总是先走。
# "X  "    "X  "    "X  "    "X  "    "X  "
# "   " -> "   " -> " X " -> " X " -> " X "
# "   "    "O  "    "O  "    "OO "    "OOX"
# 示例 2：
#
# 输入：moves = [[0,0],[1,1],[0,1],[0,2],[1,0],[2,0]]
# 输出："B"
# 解释："B" 获胜。
# "X  "    "X  "    "XX "    "XXO"    "XXO"    "XXO"
# "   " -> " O " -> " O " -> " O " -> "XO " -> "XO "
# "   "    "   "    "   "    "   "    "   "    "O  "
# 示例 3：
#
# 输入：moves = [[0,0],[1,1],[2,0],[1,0],[1,2],[2,1],[0,1],[0,2],[2,2]]
# 输出："Draw"
# 解释：由于没有办法再行动，游戏以平局结束。
# "XXO"
# "OOX"
# "XOX"
# 示例 4：
#
# 输入：moves = [[0,0],[1,1]]
# 输出："Pending"
# 解释：游戏还没有结束。
# "X  "
# " O "
# "   "
#
#
# 提示：
#
# 1 <= moves.length <= 9
# moves[i].length == 2
# 0 <= moves[i][j] <= 2
# moves 里没有重复的元素。
# moves 遵循井字棋的规则。
#

import heapq
import math
from collections import Counter, deque, defaultdict
from datetime import date
from functools import cache
from typing import List, Optional

from sortedcontainers import SortedList


class Solution:
    def tictactoe(self, moves: List[List[int]]) -> str:
        b = [["0"] * 3 for _ in range(3)]

        for i in range(len(moves)):
            if i % 2 == 0:
                b[moves[i][0]][moves[i][1]] = "A"
            else:
                b[moves[i][0]][moves[i][1]] = "B"

        for i in range(8):
            if i < 3:
                if b[i][0] != '0' and b[i][0] == b[i][1] == b[i][2]:
                    return b[i][0]
            elif 3 <= i < 6:
                if b[0][i - 3] != '0' and b[0][i - 3] == b[1][i - 3] == b[2][i - 3]:
                    return b[0][i % 3]
            else:
                if b[1][1] != '0':
                    if i == 6 and b[0][0] == b[1][1] == b[2][2]:
                        return b[1][1]
                    if i == 7 and b[0][2] == b[1][1] == b[2][0]:
                        return b[1][1]
        if len(moves) != 9:
            return "Pending"
        else:
            return "Draw"


if __name__ == "__main__":
    moves = [[0,0],[1,1],[0,1],[0,2],[1,0],[2,0]]
    test = Solution().tictactoe(moves)
    print(test)
