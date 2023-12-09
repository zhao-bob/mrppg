from typing import List


# 1138. 字母板上的路径
# 提示
# 中等
# 121
# 相关企业
# 我们从一块字母板上的位置 (0, 0) 出发，该坐标对应的字符为 board[0][0]。
#
# 在本题里，字母板为board = ["abcde", "fghij", "klmno", "pqrst", "uvwxy", "z"]，如下所示。
#
#
#
# 我们可以按下面的指令规则行动：
#
# 如果方格存在，'U' 意味着将我们的位置上移一行；
# 如果方格存在，'D' 意味着将我们的位置下移一行；
# 如果方格存在，'L' 意味着将我们的位置左移一列；
# 如果方格存在，'R' 意味着将我们的位置右移一列；
# '!' 会把在我们当前位置 (r, c) 的字符 board[r][c] 添加到答案中。
# （注意，字母板上只存在有字母的位置。）
#
# 返回指令序列，用最小的行动次数让答案和目标 target 相同。你可以返回任何达成目标的路径。
#
#
#
# 示例 1：
#
# 输入：target = "leet"
# 输出："DDR!UURRR!!DDD!"
# 示例 2：
#
# 输入：target = "code"
# 输出："RR!DDRR!UUL!R!"
#


class Solution:
    def alphabetBoardPath(self, target: str) -> str:
        board = ["abcde", "fghij", "klmno", "pqrst", "uvwxy", "z"]
        m = {}
        for i in range(len(board)):
            for j in range(len(board[i])):
                m[board[i][j]] = (i, j)

        def move(p1, p2):
            s = ''
            if p1 != p2:
                if p1[0] < p2[0]:
                    s += 'D' * (p2[0] - p1[0])
                elif p1[0] > p2[0]:
                    s += 'U' * (p1[0] - p2[0])
                if p1[1] < p2[1]:
                    s += 'R' * (p2[1] - p1[1])
                elif p1[1] > p2[1]:
                    s += 'L' * (p1[1] - p2[1])
            s += '!'
            return s

        def movez(p):
            return 'L' * p[1] + 'D' * (5 - p[0]) + '!'

        s = (0, 0)
        res = ''
        for x in target:
            p = m[x]
            if x == 'z':
                res += movez(s)
            else:
                res += move(s, p)
            s = p
        return res



if __name__ == "__main__":
    target = "zdz"
    test = Solution().alphabetBoardPath(target)
    print(test)
