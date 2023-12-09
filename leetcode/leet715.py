import heapq
import math
from collections import Counter, deque, defaultdict
from functools import cache, reduce
from itertools import product
from typing import List, Optional


# 715. Range 模块
# 提示
# 困难
# 228
# 相关企业
# Range模块是跟踪数字范围的模块。设计一个数据结构来跟踪表示为 半开区间 的范围并查询它们。
#
# 半开区间 [left, right) 表示所有 left <= x < right 的实数 x 。
#
# 实现 RangeModule 类:
#
# RangeModule() 初始化数据结构的对象。
# void addRange(int left, int right) 添加 半开区间 [left, right)，跟踪该区间中的每个实数。添加与当前跟踪的数字部分重叠的区间时，应当添加在区间 [left, right) 中尚未跟踪的任何数字到该区间中。
# boolean queryRange(int left, int right) 只有在当前正在跟踪区间 [left, right) 中的每一个实数时，才返回 true ，否则返回 false 。
# void removeRange(int left, int right) 停止跟踪 半开区间 [left, right) 中当前正在跟踪的每个实数。
#
#
# 示例 1：
#
# 输入
# ["RangeModule", "addRange", "removeRange", "queryRange", "queryRange", "queryRange"]
# [[], [10, 20], [14, 16], [10, 14], [13, 15], [16, 17]]
# 输出
# [null, null, null, true, false, true]
#
# 解释
# RangeModule rangeModule = new RangeModule();
# rangeModule.addRange(10, 20);
# rangeModule.removeRange(14, 16);
# rangeModule.queryRange(10, 14); 返回 true （区间 [10, 14) 中的每个数都正在被跟踪）
# rangeModule.queryRange(13, 15); 返回 false（未跟踪区间 [13, 15) 中像 14, 14.03, 14.17 这样的数字）
# rangeModule.queryRange(16, 17); 返回 true （尽管执行了删除操作，区间 [16, 17) 中的数字 16 仍然会被跟踪）
#
#
from sortedcontainers import SortedDict


class RangeModule:

    def __init__(self):
        self.intervals = SortedDict()

    def addRange(self, left: int, right: int) -> None:
        itvs_ = self.intervals

        x = itvs_.bisect_right(left)
        if x != 0:
            start = x - 1
            if itvs_.values()[start] >= right:
                return
            if itvs_.values()[start] >= left:
                left = itvs_.keys()[start]
                itvs_.popitem(start)
                x -= 1

        while x < len(itvs_) and itvs_.keys()[x] <= right:
            right = max(right, itvs_.values()[x])
            itvs_.popitem(x)

        itvs_[left] = right

    def queryRange(self, left: int, right: int) -> bool:
        itvs_ = self.intervals

        x = itvs_.bisect_right(left)
        if x == 0:
            return False

        return right <= itvs_.values()[x - 1]

    def removeRange(self, left: int, right: int) -> None:
        itvs_ = self.intervals

        x = itvs_.bisect_right(left)
        if x != 0:
            start = x - 1
            if (ri := itvs_.values()[start]) >= right:
                if (li := itvs_.keys()[start]) == left:
                    itvs_.popitem(start)
                else:
                    itvs_[li] = left
                if right != ri:
                    itvs_[right] = ri
                return
            elif ri > left:
                if (li := itvs_.keys()[start]) == left:
                    itvs_.popitem(start)
                    x -= 1
                else:
                    itvs_[itvs_.keys()[start]] = left

        while x < len(itvs_) and itvs_.keys()[x] < right:
            if itvs_.values()[x] <= right:
                itvs_.popitem(x)
            else:
                itvs_[right] = itvs_.values()[x]
                itvs_.popitem(x)
                break



# Your RangeModule object will be instantiated and called as such:
# obj = RangeModule()
# obj.addRange(left,right)
# param_2 = obj.queryRange(left,right)
# obj.removeRange(left,right)


if __name__ == "__main__":
    ops = ["RangeModule", "addRange", "removeRange", "queryRange", "queryRange", "queryRange"]
    par = [[], [10, 20], [14, 16], [10, 14], [13, 15], [16, 17]]
    rm = RangeModule()
    res = []
    for i in range(1, len(par)):
        if ops[i] == "addRange":
            res.append(rm.addRange(par[i][0], par[i][1]))
        elif ops[i] == "removeRange":
            res.append(rm.removeRange(par[i][0], par[i][1]))
        elif ops[i] == "queryRange":
            res.append(rm.queryRange(par[i][0], par[i][1]))
    print(res)
