import collections
import heapq
import math
from bisect import bisect_right
from collections import Counter, deque
from functools import cache
from itertools import product
from typing import List, Optional


# 56. 合并区间
# 中等
# 以数组 intervals 表示若干个区间的集合，其中单个区间为 intervals[i] = [starti, endi] 。请你合并所有重叠的区间，并返回 一个不重叠的区间数组，该数组需恰好覆盖输入中的所有区间 。
#
#
#
# 示例 1：
#
# 输入：intervals = [[1,3],[2,6],[8,10],[15,18]]
# 输出：[[1,6],[8,10],[15,18]]
# 解释：区间 [1,3] 和 [2,6] 重叠, 将它们合并为 [1,6].
# 示例 2：
#
# 输入：intervals = [[1,4],[4,5]]
# 输出：[[1,5]]
# 解释：区间 [1,4] 和 [4,5] 可被视为重叠区间。

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if len(intervals) <= 1:
            return intervals
        intervals.sort(key=lambda x: x[0])
        res = []
        s = intervals[0][0]
        e = intervals[0][1]
        for i in range(1, len(intervals)):
            if intervals[i][0] > e:
                res.append([s, e])
                s = intervals[i][0]
                e = intervals[i][1]
            elif intervals[i][1] > e:
                e = intervals[i][1]
        res.append([s, e])
        return res


if __name__ == "__main__":
    intervals = [[1, 4], [4, 5]]

    test = Solution().merge(intervals)

    print(test)
