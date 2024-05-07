# 2671. 频率跟踪器
# 中等
# 相关标签
# 相关企业
# 提示
# 请你设计并实现一个能够对其中的值进行跟踪的数据结构，并支持对频率相关查询进行应答。
#
# 实现 FrequencyTracker 类：
#
# FrequencyTracker()：使用一个空数组初始化 FrequencyTracker 对象。
# void add(int number)：添加一个 number 到数据结构中。
# void deleteOne(int number)：从数据结构中删除一个 number 。数据结构 可能不包含 number ，在这种情况下不删除任何内容。
# bool hasFrequency(int frequency): 如果数据结构中存在出现 frequency 次的数字，则返回 true，否则返回 false。
#
#
# 示例 1：
#
# 输入
# ["FrequencyTracker", "add", "add", "hasFrequency"]
# [[], [3], [3], [2]]
# 输出
# [null, null, null, true]
#
# 解释
# FrequencyTracker frequencyTracker = new FrequencyTracker();
# frequencyTracker.add(3); // 数据结构现在包含 [3]
# frequencyTracker.add(3); // 数据结构现在包含 [3, 3]
# frequencyTracker.hasFrequency(2); // 返回 true ，因为 3 出现 2 次
# 示例 2：
#
# 输入
# ["FrequencyTracker", "add", "deleteOne", "hasFrequency"]
# [[], [1], [1], [1]]
# 输出
# [null, null, null, false]
#
# 解释
# FrequencyTracker frequencyTracker = new FrequencyTracker();
# frequencyTracker.add(1); // 数据结构现在包含 [1]
# frequencyTracker.deleteOne(1); // 数据结构现在为空 []
# frequencyTracker.hasFrequency(1); // 返回 false ，因为数据结构为空
# 示例 3：
#
# 输入
# ["FrequencyTracker", "hasFrequency", "add", "hasFrequency"]
# [[], [2], [3], [1]]
# 输出
# [null, false, null, true]
#
# 解释
# FrequencyTracker frequencyTracker = new FrequencyTracker();
# frequencyTracker.hasFrequency(2); // 返回 false ，因为数据结构为空
# frequencyTracker.add(3); // 数据结构现在包含 [3]
# frequencyTracker.hasFrequency(1); // 返回 true ，因为 3 出现 1 次
#
#
# 提示：
#
# 1 <= number <= 105
# 1 <= frequency <= 105
# 最多调用 add、deleteOne 和 hasFrequency 共计 2 * 105 次
#

import heapq
import math
from collections import Counter, deque, defaultdict
from datetime import date
from functools import cache
from typing import List, Optional

from sortedcontainers import SortedList


class FrequencyTracker:

    def __init__(self):
        self.ns = {}
        self.fs = {}

    def add(self, number: int) -> None:
        if number in self.ns:
            self.fs[self.ns[number]] -= 1
            self.ns[number] += 1
            if self.ns[number] in self.fs:
                self.fs[self.ns[number]] += 1
            else:
                self.fs[self.ns[number]] = 1
        else:
            self.ns[number] = 1
            if self.ns[number] in self.fs:
                self.fs[self.ns[number]] += 1
            else:
                self.fs[self.ns[number]] = 1

    def deleteOne(self, number: int) -> None:
        if number in self.ns and self.ns[number] > 0:
            self.fs[self.ns[number]] -= 1
            self.ns[number] -= 1
            if self.ns[number] in self.fs:
                self.fs[self.ns[number]] += 1
            else:
                self.fs[self.ns[number]] = 1

    def hasFrequency(self, frequency: int) -> bool:
        return frequency in self.fs and self.fs[frequency] != 0

# Your FrequencyTracker object will be instantiated and called as such:
# obj = FrequencyTracker()
# obj.add(number)
# obj.deleteOne(number)
# param_3 = obj.hasFrequency(frequency)


if __name__ == "__main__":
    ops = ["FrequencyTracker","deleteOne","deleteOne","deleteOne","deleteOne","hasFrequency","add","deleteOne","hasFrequency","deleteOne","deleteOne","deleteOne","hasFrequency","add","hasFrequency","deleteOne","hasFrequency","hasFrequency","add","hasFrequency","add","deleteOne","hasFrequency","add","hasFrequency","hasFrequency","add"]
    par = [[],[9],[8],[1],[4],[1],[10],[5],[1],[10],[9],[10],[1],[4],[1],[4],[1],[1],[10],[1],[2],[1],[2],[7],[1],[1],[6]]
    ft = FrequencyTracker()
    res = []
    for i in range(1, len(par)):
        if ops[i] == "add":
            res.append(ft.add(par[i][0]))
        elif ops[i] == "hasFrequency":
            res.append(ft.hasFrequency(par[i][0]))
        elif ops[i] == "deleteOne":
            res.append(ft.deleteOne(par[i][0]))
    print(res)
