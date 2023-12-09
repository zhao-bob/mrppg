import heapq
import math
from collections import Counter
from functools import cache
from typing import List
from sortedcontainers import SortedList


# 2127. 参加会议的最多员工数
# 提示
# 困难
# 96
# 相关企业
# 一个公司准备组织一场会议，邀请名单上有 n 位员工。公司准备了一张 圆形 的桌子，可以坐下 任意数目 的员工。
#
# 员工编号为 0 到 n - 1 。每位员工都有一位 喜欢 的员工，每位员工 当且仅当 他被安排在喜欢员工的旁边，他才会参加会议。每位员工喜欢的员工 不会 是他自己。
#
# 给你一个下标从 0 开始的整数数组 favorite ，其中 favorite[i] 表示第 i 位员工喜欢的员工。请你返回参加会议的 最多员工数目 。
#
#
#
# 示例 1：
#
#
#
# 输入：favorite = [2,2,1,2]
# 输出：3
# 解释：
# 上图展示了公司邀请员工 0，1 和 2 参加会议以及他们在圆桌上的座位。
# 没办法邀请所有员工参与会议，因为员工 2 没办法同时坐在 0，1 和 3 员工的旁边。
# 注意，公司也可以邀请员工 1，2 和 3 参加会议。
# 所以最多参加会议的员工数目为 3 。
# 示例 2：
#
# 输入：favorite = [1,2,0]
# 输出：3
# 解释：
# 每个员工都至少是另一个员工喜欢的员工。所以公司邀请他们所有人参加会议的前提是所有人都参加了会议。
# 座位安排同图 1 所示：
# - 员工 0 坐在员工 2 和 1 之间。
# - 员工 1 坐在员工 0 和 2 之间。
# - 员工 2 坐在员工 1 和 0 之间。
# 参与会议的最多员工数目为 3 。
# 示例 3：
#
#
#
# 输入：favorite = [3,0,1,4,1]
# 输出：4
# 解释：
# 上图展示了公司可以邀请员工 0，1，3 和 4 参加会议以及他们在圆桌上的座位。
# 员工 2 无法参加，因为他喜欢的员工 0 旁边的座位已经被占领了。
# 所以公司只能不邀请员工 2 。
# 参加会议的最多员工数目为 4 。
#


class Solution:
    def maximumInvitations(self, favorite: List[int]) -> int:
        n = len(favorite)
        s = {}
        for i in range(n):
            if favorite[i] in s:
                s[favorite[i]].add(i)
            else:
                s[favorite[i]] = {i}

        res = 0
        loop = []
        searched = set()
        for i in s:
            if i not in searched:
                l = 1
                searched.add(i)
                c = {i: l}
                ne = favorite[i]
                while ne not in searched and ne != i:
                    searched.add(ne)
                    l += 1
                    c[ne] = l
                    ne = favorite[ne]
                if ne in c:
                    cl = l - c[ne] + 1
                    if cl > 2:
                        res = max(res, cl)
                    else:
                        s[ne].discard(favorite[ne])
                        s[favorite[ne]].discard(ne)
                        loop.append([ne, favorite[ne]])

        def dfs(i):
            if i not in s:
                return 1
            l = 0
            for k in s[i]:
                l = max(dfs(k), l)
            return l + 1

        a = 0
        # lv = 0
        for i, j in loop:
            # if dfs(i) + dfs(j) == 2:
            #     a += 2
            # else:
            a += (dfs(i) + dfs(j))
        return max(res, a)


if __name__ == "__main__":
    favorite = [7,0,7,13,11,6,8,5,9,8,9,14,15,7,11,6]
    test = Solution().maximumInvitations(favorite)
    print(test)
