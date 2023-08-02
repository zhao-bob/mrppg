import heapq
import math
from collections import Counter, deque
from typing import List, Optional


# LCP 41. 黑白翻转棋
# 在 n*m 大小的棋盘中，有黑白两种棋子，黑棋记作字母 "X", 白棋记作字母 "O"，空余位置记作 "."。当落下的棋子与其他相同颜色的棋子在行、列或对角线完全包围（中间不存在空白位置）另一种颜色的棋子，则可以翻转这些棋子的颜色。
#
# 1.gif2.gif3.gif
#
# 「力扣挑战赛」黑白翻转棋项目中，将提供给选手一个未形成可翻转棋子的棋盘残局，其状态记作 chessboard。若下一步可放置一枚黑棋，请问选手最多能翻转多少枚白棋。
#
# 注意：
#
# 若翻转白棋成黑棋后，棋盘上仍存在可以翻转的白棋，将可以 继续 翻转白棋
# 输入数据保证初始棋盘状态无可以翻转的棋子且存在空余位置
# 示例 1：
#
# 输入：chessboard = ["....X.","....X.","XOOO..","......","......"]
#
# 输出：3
#
# 解释：
# 可以选择下在 [2,4] 处，能够翻转白方三枚棋子。
#
# 示例 2：
#
# 输入：chessboard = [".X.",".O.","XO."]
#
# 输出：2
#
# 解释：
# 可以选择下在 [2,2] 处，能够翻转白方两枚棋子。
# 2126c1d21b1b9a9924c639d449cc6e65.gif
#
# 示例 3：
#
# 输入：chessboard = [".......",".......",".......","X......",".O.....","..O....","....OOX"]
#
# 输出：4
#
# 解释：
# 可以选择下在 [6,3] 处，能够翻转白方四枚棋子。
#

class Solution:
    def flipChess(self, chessboard: List[str]) -> int:
        def judge(chessboard: List[List[str]], x: int, y: int, dx: int, dy: int) -> bool:
            x += dx
            y += dy
            while 0 <= x < len(chessboard) and 0 <= y < len(chessboard[0]):
                if chessboard[x][y] == "X":
                    return True
                elif chessboard[x][y] == ".":
                    return False
                x += dx
                y += dy
            return False

        def bfs(chessboard: List[str], px: int, py: int) -> int:
            chessboard = [list(row) for row in chessboard]
            cnt = 0
            q = deque([(px, py)])
            chessboard[px][py] = "X"

            while q:
                tx, ty = q.popleft()
                for dx in [-1, 0, 1]:
                    for dy in [-1, 0, 1]:
                        if dx == dy == 0:
                            continue
                        if judge(chessboard, tx, ty, dx, dy):
                            x, y = tx + dx, ty + dy
                            while chessboard[x][y] != "X":
                                q.append((x, y))
                                chessboard[x][y] = "X"
                                x += dx
                                y += dy
                                cnt += 1
            return cnt

        res = 0
        for i in range(len(chessboard)):
            for j in range(len(chessboard[0])):
                if chessboard[i][j] == ".":
                    res = max(res, bfs(chessboard, i, j))
        return res


if __name__ == "__main__":
    chessboard = ["....X.","....X.","XOOO..","......","......"]

    test = Solution().flipChess(chessboard)
    print(test)
