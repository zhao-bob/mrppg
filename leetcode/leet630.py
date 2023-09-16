import collections
import heapq
import math
from bisect import bisect_right
from collections import Counter, deque
from functools import cache
from itertools import product
from typing import List, Optional


# 630. 课程表 III
# 提示
# 困难
# 447
# 相关企业
# 这里有 n 门不同的在线课程，按从 1 到 n 编号。给你一个数组 courses ，其中 courses[i] = [durationi, lastDayi] 表示第 i 门课将会 持续 上 durationi 天课，并且必须在不晚于 lastDayi 的时候完成。
#
# 你的学期从第 1 天开始。且不能同时修读两门及两门以上的课程。
#
# 返回你最多可以修读的课程数目。
#
#
#
# 示例 1：
#
# 输入：courses = [[100, 200], [200, 1300], [1000, 1250], [2000, 3200]]
# 输出：3
# 解释：
# 这里一共有 4 门课程，但是你最多可以修 3 门：
# 首先，修第 1 门课，耗费 100 天，在第 100 天完成，在第 101 天开始下门课。
# 第二，修第 3 门课，耗费 1000 天，在第 1100 天完成，在第 1101 天开始下门课程。
# 第三，修第 2 门课，耗时 200 天，在第 1300 天完成。
# 第 4 门课现在不能修，因为将会在第 3300 天完成它，这已经超出了关闭日期。
# 示例 2：
#
# 输入：courses = [[1,2]]
# 输出：1
# 示例 3：
#
# 输入：courses = [[3,2],[4,3]]
# 输出：0

class Solution:
    def scheduleCourse(self, courses: List[List[int]]) -> int:
        courses.sort(key=lambda x: x[1])

        res = 0
        t = [0] * (len(courses) + 1)
        h = []
        for i in range(1, len(courses) + 1):
            if courses[i - 1][1] >= courses[i - 1][0] + t[i - 1]:
                res += 1
                t[i] = t[i - 1] + courses[i - 1][0]
                heapq.heappush(h, - courses[i - 1][0])
            else:
                if h:
                    a = -h[0]
                    if a > courses[i - 1][0]:
                        t[i] = t[i - 1] - a + courses[i - 1][0]
                        heapq.heapreplace(h, - courses[i - 1][0])
                    else:
                        t[i] = t[i - 1]
        return res


if __name__ == "__main__":
    courses = [[7,16],[2,3],[3,12],[3,14],[10,19],[10,16],[6,8],[6,11],[3,13],[6,16]]

    test = Solution().scheduleCourse(courses)

    print(test)
