import heapq
import math
from collections import Counter
from functools import cache
from typing import List, Optional
from sortedcontainers import SortedList


# 2336. 无限集中的最小数字
# 提示
# 中等
# 46
# 相关企业
# 现有一个包含所有正整数的集合 [1, 2, 3, 4, 5, ...] 。
#
# 实现 SmallestInfiniteSet 类：
#
# SmallestInfiniteSet() 初始化 SmallestInfiniteSet 对象以包含 所有 正整数。
# int popSmallest() 移除 并返回该无限集中的最小整数。
# void addBack(int num) 如果正整数 num 不 存在于无限集中，则将一个 num 添加 到该无限集中。
#
#
# 示例：
#
# 输入
# ["SmallestInfiniteSet", "addBack", "popSmallest", "popSmallest", "popSmallest", "addBack", "popSmallest", "popSmallest", "popSmallest"]
# [[], [2], [], [], [], [1], [], [], []]
# 输出
# [null, null, 1, 2, 3, null, 1, 4, 5]
#
# 解释
# SmallestInfiniteSet smallestInfiniteSet = new SmallestInfiniteSet();
# smallestInfiniteSet.addBack(2);    // 2 已经在集合中，所以不做任何变更。
# smallestInfiniteSet.popSmallest(); // 返回 1 ，因为 1 是最小的整数，并将其从集合中移除。
# smallestInfiniteSet.popSmallest(); // 返回 2 ，并将其从集合中移除。
# smallestInfiniteSet.popSmallest(); // 返回 3 ，并将其从集合中移除。
# smallestInfiniteSet.addBack(1);    // 将 1 添加到该集合中。
# smallestInfiniteSet.popSmallest(); // 返回 1 ，因为 1 在上一步中被添加到集合中，
#                                    // 且 1 是最小的整数，并将其从集合中移除。
# smallestInfiniteSet.popSmallest(); // 返回 4 ，并将其从集合中移除。
# smallestInfiniteSet.popSmallest(); // 返回 5 ，并将其从集合中移除。
#

class SmallestInfiniteSet:

    def __init__(self):
        self.rs = set()
        self.smallest = 1


    def popSmallest(self) -> int:
        r = self.smallest
        self.smallest += 1
        while self.smallest in self.rs:
            self.smallest += 1
        self.rs.add(r)
        return r


    def addBack(self, num: int) -> None:
        if num in self.rs:
            self.rs.discard(num)
            if num < self.smallest:
                self.smallest = num



# Your SmallestInfiniteSet object will be instantiated and called as such:
# obj = SmallestInfiniteSet()
# param_1 = obj.popSmallest()
# obj.addBack(num)


if __name__ == "__main__":
    ops = ["SmallestInfiniteSet", "addBack", "popSmallest", "popSmallest", "popSmallest", "addBack", "popSmallest", "popSmallest", "popSmallest"]
    par = [[], [2], [], [], [], [1], [], [], []]
    sis = SmallestInfiniteSet()
    res = []
    for i in range(1, len(par)):
        if ops[i] == "popSmallest":
            res.append(sis.popSmallest())
        elif ops[i] == "addBack":
            res.append(sis.addBack(par[i][0]))
    print(res)
