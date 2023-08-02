import heapq
import math
from collections import Counter, deque
from functools import cache
from itertools import product
from typing import List, Optional

# 874. 模拟行走机器人
# 机器人在一个无限大小的 XY 网格平面上行走，从点 (0, 0) 处开始出发，面向北方。该机器人可以接收以下三种类型的命令 commands ：
#
# -2 ：向左转 90 度
# -1 ：向右转 90 度
# 1 <= x <= 9 ：向前移动 x 个单位长度
# 在网格上有一些格子被视为障碍物 obstacles 。第 i 个障碍物位于网格点  obstacles[i] = (xi, yi) 。
#
# 机器人无法走到障碍物上，它将会停留在障碍物的前一个网格方块上，但仍然可以继续尝试进行该路线的其余部分。
#
# 返回从原点到机器人所有经过的路径点（坐标为整数）的最大欧式距离的平方。（即，如果距离为 5 ，则返回 25 ）
#
#
# 注意：
#
# 北表示 +Y 方向。
# 东表示 +X 方向。
# 南表示 -Y 方向。
# 西表示 -X 方向。
#
#
# 示例 1：
#
# 输入：commands = [4,-1,3], obstacles = []
# 输出：25
# 解释：
# 机器人开始位于 (0, 0)：
# 1. 向北移动 4 个单位，到达 (0, 4)
# 2. 右转
# 3. 向东移动 3 个单位，到达 (3, 4)
# 距离原点最远的是 (3, 4) ，距离为 32 + 42 = 25
# 示例 2：
#
# 输入：commands = [4,-1,4,-2,4], obstacles = [[2,4]]
# 输出：65
# 解释：机器人开始位于 (0, 0)：
# 1. 向北移动 4 个单位，到达 (0, 4)
# 2. 右转
# 3. 向东移动 1 个单位，然后被位于 (2, 4) 的障碍物阻挡，机器人停在 (1, 4)
# 4. 左转
# 5. 向北走 4 个单位，到达 (1, 8)
# 距离原点最远的是 (1, 8) ，距离为 12 + 82 = 65
#

class Solution:
    def robotSim(self, commands: List[int], obstacles: List[List[int]]) -> int:
        xo = {}
        yo = {}
        obstacles.sort(key=lambda x:(x[0],x[1]))
        for o in obstacles:
            if o[0] in xo:
                xo[o[0]].append(o[1])
            else:
                xo[o[0]] = [o[1]]
            if o[1] in yo:
                yo[o[1]].append(o[0])
            else:
                yo[o[1]] = [o[0]]
        pos = [0, 0]
        di = 0
        res = 0
        for c in commands:
            if c == -1:
                di = (di - 1) % 4
            elif c == -2:
                di = (di + 1) % 4
            else:
                if di == 0:
                    y1 = pos[1]
                    y2 = pos[1] + c
                    if pos[0] in xo:
                        for i in xo[pos[0]]:
                            if y1 < i <= y2:
                                y2 = i - 1
                                break
                    pos[1] = y2
                elif di == 1:
                    x1 = pos[0]
                    x2 = pos[0] - c
                    if pos[1] in yo:
                        for i in yo[pos[1]]:
                            if x2 <= i < x1:
                                x2 = i + 1
                                break
                    pos[0] = x2
                elif di == 2:
                    y1 = pos[1]
                    y2 = pos[1] - c
                    if pos[0] in xo:
                        for i in xo[pos[0]]:
                            if y2 <= i < y1:
                                y2 = i + 1
                                break
                    pos[1] = y2
                elif di == 3:
                    x1 = pos[0]
                    x2 = pos[0] + c
                    if pos[1] in yo:
                        for i in yo[pos[1]]:
                            if x1 < i <= x2:
                                x2 = i - 1
                                break
                    pos[0] = x2
                d = pos[0] * pos[0] + pos[1] * pos[1]
                if d > res:
                    res = d
        return res

if __name__ == "__main__":
    commands = [7,-2,-2,7,5]
    obstacles = [[-3,2],[-2,1],[0,1],[-2,4],[-1,0],[-2,-3],[0,-3],[4,4],[-3,3],[2,2]]

    test = Solution().robotSim(commands, obstacles)
    print(test)
