import collections
import heapq
import math
from bisect import bisect_right
from collections import Counter, deque
from functools import cache
from itertools import product
from typing import List, Optional


# 57. 插入区间
# 中等
# 746
# 相关企业
# 给你一个 无重叠的 ，按照区间起始端点排序的区间列表。
#
# 在列表中插入一个新的区间，你需要确保列表中的区间仍然有序且不重叠（如果有必要的话，可以合并区间）。
#
#
#
# 示例 1：
#
# 输入：intervals = [[1,3],[6,9]], newInterval = [2,5]
# 输出：[[1,5],[6,9]]
# 示例 2：
#
# 输入：intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]], newInterval = [4,8]
# 输出：[[1,2],[3,10],[12,16]]
# 解释：这是因为新的区间 [4,8] 与 [3,5],[6,7],[8,10] 重叠。
# 示例 3：
#
# 输入：intervals = [], newInterval = [5,7]
# 输出：[[5,7]]
# 示例 4：
#
# 输入：intervals = [[1,5]], newInterval = [2,3]
# 输出：[[1,5]]
# 示例 5：
#
# 输入：intervals = [[1,5]], newInterval = [2,7]
# 输出：[[1,7]]

class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res = []
        if len(intervals) == 0:
            res.append(newInterval)
            return res
        i = 0
        j = 0
        while i < len(intervals):
            if intervals[i][0] < newInterval[0]:
                i += 1
            else:
                break
        while j < len(intervals):
            if intervals[j][1] < newInterval[1]:
                j += 1
            else:
                break
        s = -1
        e = -1
        if i == 0:
            s = newInterval[0]
        if j == len(intervals):
            e = newInterval[1]
        if s != -1 and e != -1:
            res.append([s, e])
            return res
        for k in range(len(intervals)):
            if k < i - 1 or k > j:
                res.append(intervals[k])
            else:
                if k == i - 1:
                    if intervals[i - 1][1] >= newInterval[0]:
                        s = intervals[i - 1][0]
                    else:
                        res.append(intervals[i - 1])
                        s = newInterval[0]
                    if e != -1:
                        res.append([s, e])
                        return res
                if k == j:
                    if intervals[j][0] <= newInterval[1]:
                        e = intervals[j][1]
                        res.append([s, e])
                    else:
                        e = newInterval[1]
                        res.append([s, e])
                        res.append(intervals[j])
        return res


if __name__ == "__main__":
    intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]]
    newInterval = [4,8]

    test = Solution().insert(intervals, newInterval)

    print(test)
