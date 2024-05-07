import heapq
import math
from typing import List, Optional


# 2276. 统计区间中的整数数目
# 提示
# 困难
# 57
# 相关企业
# 给你区间的 空 集，请你设计并实现满足要求的数据结构：
#
# 新增：添加一个区间到这个区间集合中。
# 统计：计算出现在 至少一个 区间中的整数个数。
# 实现 CountIntervals 类：
#
# CountIntervals() 使用区间的空集初始化对象
# void add(int left, int right) 添加区间 [left, right] 到区间集合之中。
# int count() 返回出现在 至少一个 区间中的整数个数。
# 注意：区间 [left, right] 表示满足 left <= x <= right 的所有整数 x 。
#
#
#
# 示例 1：
#
# 输入
# ["CountIntervals", "add", "add", "count", "add", "count"]
# [[], [2, 3], [7, 10], [], [5, 8], []]
# 输出
# [null, null, null, 6, null, 8]
#
# 解释
# CountIntervals countIntervals = new CountIntervals(); // 用一个区间空集初始化对象
# countIntervals.add(2, 3);  // 将 [2, 3] 添加到区间集合中
# countIntervals.add(7, 10); // 将 [7, 10] 添加到区间集合中
# countIntervals.count();    // 返回 6
#                            // 整数 2 和 3 出现在区间 [2, 3] 中
#                            // 整数 7、8、9、10 出现在区间 [7, 10] 中
# countIntervals.add(5, 8);  // 将 [5, 8] 添加到区间集合中
# countIntervals.count();    // 返回 8
#                            // 整数 2 和 3 出现在区间 [2, 3] 中
#                            // 整数 5 和 6 出现在区间 [5, 8] 中
#                            // 整数 7 和 8 出现在区间 [5, 8] 和区间 [7, 10] 中
#                            // 整数 9 和 10 出现在区间 [7, 10] 中
#


class CountIntervals:

    def __init__(self):
        self.intervals = []
        self.c = 0


    def add(self, left: int, right: int) -> None:
        if self.intervals:
            li = self.search(left, 0)
            ri = self.search(right, 1)
            if li == len(self.intervals):
                if left > self.intervals[-1][1]:
                    self.intervals.append((left, right))
                    self.c += (right - left + 1)
                else:
                    if right > self.intervals[-1][1]:
                        self.c += right - self.intervals[-1][1]
                        self.intervals[-1] = (self.intervals[-1][0], right)
                return

            if ri == 0:
                if right < self.intervals[0][0]:
                    self.intervals = [(left, right)] + self.intervals
                    self.c += (right - left + 1)
                else:
                    if self.intervals[0][0] > left:
                        self.c += (self.intervals[0][0] - left)
                        self.intervals[0] = (left, self.intervals[0][1])
                return
            if li > 0:
                if self.intervals[li - 1][1] < left:
                    nl = left
                else:
                    nl = self.intervals[li - 1][0]
                    li -= 1
            else:
                nl = left
            if ri < len(self.intervals):
                if self.intervals[ri][0] > right:
                    nr = right
                    ri -= 1
                else:
                    nr = self.intervals[ri][1]
            else:
                nr = right
                ri -= 1
            self.c += (nr - nl + 1) - sum(self.intervals[i][1] - self.intervals[i][0] + 1 for i in range(li, ri + 1))
            self.intervals = self.intervals[:li] + [(nl, nr)] + self.intervals[ri + 1:]
        else:
            self.intervals.append((left, right))
            self.c += (right - left + 1)


    def search(self, val, left):
        l = 0
        r = len(self.intervals) - 1
        while l <= r:
            mid = (l + r) // 2
            if self.intervals[mid][left] < val:
                l = mid + 1
            elif self.intervals[mid][left] > val:
                r = mid - 1
            else:
                return mid
        return l


    def count(self) -> int:
        return self.c



# Your CountIntervals object will be instantiated and called as such:
# obj = CountIntervals()
# obj.add(left,right)
# param_2 = obj.count()


if __name__ == "__main__":
    ops = ["CountIntervals","add","add","add","add","add","add","count"]
    par = [[],[10,27],[46,50],[15,35],[12,32],[7,15],[49,49],[]]
    ci = CountIntervals()
    res = []
    for i in range(1, len(par)):
        if ops[i] == "add":
            res.append(ci.add(par[i][0], par[i][1]))
        elif ops[i] == "count":
            res.append(ci.count())
    print(res)
