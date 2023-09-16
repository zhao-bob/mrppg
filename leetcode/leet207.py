import collections
import heapq
import math
from bisect import bisect_right
from collections import Counter, deque
from functools import cache
from itertools import product
from typing import List, Optional


# 207. 课程表
# 提示
# 中等
# 1.7K
# 相关企业
# 你这个学期必须选修 numCourses 门课程，记为 0 到 numCourses - 1 。
#
# 在选修某些课程之前需要一些先修课程。 先修课程按数组 prerequisites 给出，其中 prerequisites[i] = [ai, bi] ，表示如果要学习课程 ai 则 必须 先学习课程  bi 。
#
# 例如，先修课程对 [0, 1] 表示：想要学习课程 0 ，你需要先完成课程 1 。
# 请你判断是否可能完成所有课程的学习？如果可以，返回 true ；否则，返回 false 。
#
#
#
# 示例 1：
#
# 输入：numCourses = 2, prerequisites = [[1,0]]
# 输出：true
# 解释：总共有 2 门课程。学习课程 1 之前，你需要完成课程 0 。这是可能的。
# 示例 2：
#
# 输入：numCourses = 2, prerequisites = [[1,0],[0,1]]
# 输出：false
# 解释：总共有 2 门课程。学习课程 1 之前，你需要先完成​课程 0 ；并且学习课程 0 之前，你还应先完成课程 1 。这是不可能的。

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        d = [0] * numCourses
        o = {}

        for p in prerequisites:
            d[p[1]] += 1
            if p[0] in o:
                o[p[0]].add(p[1])
            else:
                o[p[0]] = {p[1]}

        q = [u for u in range(numCourses) if d[u] == 0]
        s = set()
        while len(q) > 0:
            u = q[0]
            q = q[1:]
            if u not in s:
                s.add(u)
                if u in o:
                    for k in o[u]:
                        d[k] -= 1
                        if d[k] == 0:
                            q.append(k)
            else:
                return False
        if len(s) == numCourses:
            return True
        else:
            return False
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
        return True


if __name__ == "__main__":
    numCourses = 2
    prerequisites = [[1, 0], [0, 1]]

    test = Solution().canFinish(numCourses, prerequisites)

    print(test)
