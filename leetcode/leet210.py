import collections
import heapq
import math
from bisect import bisect_right
from collections import Counter, deque
from functools import cache
from itertools import product
from typing import List, Optional


# 210. 课程表 II
# 提示
# 中等
# 827
# 相关企业
# 现在你总共有 numCourses 门课需要选，记为 0 到 numCourses - 1。给你一个数组 prerequisites ，其中 prerequisites[i] = [ai, bi] ，表示在选修课程 ai 前 必须 先选修 bi 。
#
# 例如，想要学习课程 0 ，你需要先完成课程 1 ，我们用一个匹配来表示：[0,1] 。
# 返回你为了学完所有课程所安排的学习顺序。可能会有多个正确的顺序，你只要返回 任意一种 就可以了。如果不可能完成所有课程，返回 一个空数组 。
#
#
#
# 示例 1：
#
# 输入：numCourses = 2, prerequisites = [[1,0]]
# 输出：[0,1]
# 解释：总共有 2 门课程。要学习课程 1，你需要先完成课程 0。因此，正确的课程顺序为 [0,1] 。
# 示例 2：
#
# 输入：numCourses = 4, prerequisites = [[1,0],[2,0],[3,1],[3,2]]
# 输出：[0,2,1,3]
# 解释：总共有 4 门课程。要学习课程 3，你应该先完成课程 1 和课程 2。并且课程 1 和课程 2 都应该排在课程 0 之后。
# 因此，一个正确的课程顺序是 [0,1,2,3] 。另一个正确的排序是 [0,2,1,3] 。
# 示例 3：
#
# 输入：numCourses = 1, prerequisites = []
# 输出：[0]

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        d = [0] * numCourses
        o = {}

        for p in prerequisites:
            d[p[0]] += 1
            if p[1] in o:
                o[p[1]].add(p[0])
            else:
                o[p[1]] = {p[0]}

        q = [u for u in range(numCourses) if d[u] == 0]
        res = []
        while len(q) > 0:
            u = q[0]
            q = q[1:]
            res.append(u)
            if u in o:
                for k in o[u]:
                    d[k] -= 1
                    if d[k] == 0:
                        q.append(k)
        if len(res) == numCourses:
            return res
        else:
            return []
        # s = set()
        # while len(s) < numCourses:
        #     for i in range(numCourses):
        #         if d[i] == 0 and i not in s:
        #             s.add(i)
        #             if i in o:
        #                 for k in o[i]:
        #                     d[k] -= 1
        #             break
        #     else:
        #         return False
        # return True


if __name__ == "__main__":
    numCourses = 1
    prerequisites = []

    test = Solution().findOrder(numCourses, prerequisites)

    print(test)
