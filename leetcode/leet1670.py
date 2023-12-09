import heapq
import math
from collections import Counter
from functools import cache
from typing import List, Optional
from sortedcontainers import SortedList


# 1670. 设计前中后队列
# 提示
# 中等
# 42
# 相关企业
# 请你设计一个队列，支持在前，中，后三个位置的 push 和 pop 操作。
#
# 请你完成 FrontMiddleBack 类：
#
# FrontMiddleBack() 初始化队列。
# void pushFront(int val) 将 val 添加到队列的 最前面 。
# void pushMiddle(int val) 将 val 添加到队列的 正中间 。
# void pushBack(int val) 将 val 添加到队里的 最后面 。
# int popFront() 将 最前面 的元素从队列中删除并返回值，如果删除之前队列为空，那么返回 -1 。
# int popMiddle() 将 正中间 的元素从队列中删除并返回值，如果删除之前队列为空，那么返回 -1 。
# int popBack() 将 最后面 的元素从队列中删除并返回值，如果删除之前队列为空，那么返回 -1 。
# 请注意当有 两个 中间位置的时候，选择靠前面的位置进行操作。比方说：
#
# 将 6 添加到 [1, 2, 3, 4, 5] 的中间位置，结果数组为 [1, 2, 6, 3, 4, 5] 。
# 从 [1, 2, 3, 4, 5, 6] 的中间位置弹出元素，返回 3 ，数组变为 [1, 2, 4, 5, 6] 。
#
#
# 示例 1：
#
# 输入：
# ["FrontMiddleBackQueue", "pushFront", "pushBack", "pushMiddle", "pushMiddle", "popFront", "popMiddle", "popMiddle", "popBack", "popFront"]
# [[], [1], [2], [3], [4], [], [], [], [], []]
# 输出：
# [null, null, null, null, null, 1, 3, 4, 2, -1]
#
# 解释：
# FrontMiddleBackQueue q = new FrontMiddleBackQueue();
# q.pushFront(1);   // [1]
# q.pushBack(2);    // [1, 2]
# q.pushMiddle(3);  // [1, 3, 2]
# q.pushMiddle(4);  // [1, 4, 3, 2]
# q.popFront();     // 返回 1 -> [4, 3, 2]
# q.popMiddle();    // 返回 3 -> [4, 2]
# q.popMiddle();    // 返回 4 -> [2]
# q.popBack();      // 返回 2 -> []
# q.popFront();     // 返回 -1 -> [] （队列为空）
#

class Node:
    def __init__(self, val: int = 0, next: 'Node'=None, previous: 'Node'=None):
        self.val = val
        self.next = next
        self.previous = previous


class FrontMiddleBackQueue:

    def __init__(self):
        self.front = None
        self.back = None
        self.middle = None
        self.num = 0


    def pushFront(self, val: int) -> None:
        n = Node(val)
        self.num += 1
        if self.front:
            n.next = self.front
            self.front.previous = n
            self.front = n
            if self.num % 2 != 0:
                self.middle = self.middle.previous
        else:
            self.front = n
            self.back = n
            self.middle = n


    def pushMiddle(self, val: int) -> None:
        n = Node(val)
        self.num += 1
        if self.middle:
            p = self.middle.previous
            n.next = self.middle
            self.middle.previous = n
            if p:
                p.next = n
                n.previous = p
            else:
                self.front = n
            if self.num % 2 != 0:
                self.middle = n
        else:
            self.front = n
            self.back = n
            self.middle = n


    def pushBack(self, val: int) -> None:
        n = Node(val)
        self.num += 1
        if self.back:
            self.back.next = n
            n.previous = self.back
            self.back = n
            if self.num % 2 == 0:
                self.middle = self.middle.next
        else:
            self.front = n
            self.back = n
            self.middle = n


    def popFront(self) -> int:
        if self.num == 0:
            return -1
        else:
            res = self.front.val
            self.num -= 1
            if self.num == 0:
                self.front = None
                self.back = None
                self.middle = None
            else:
                self.front = self.front.next
                self.front.previous = None
                if self.num % 2 == 0:
                    self.middle = self.middle.next
            return res


    def popMiddle(self) -> int:
        if self.num == 0:
            return -1
        else:
            self.num -= 1
            if self.num % 2 == 0:
                res = self.middle.val
                if self.num == 0:
                    self.front = None
                    self.back = None
                    self.middle = None
                else:
                    p = self.middle.previous
                    n = self.middle.next
                    p.next = n
                    n.previous = p
                    self.middle = n
            else:
                res = self.middle.previous.val
                if self.num == 1:
                    self.front = self.middle
                    self.middle.previous = None
                else:
                    p = self.middle.previous.previous
                    p.next = self.middle
                    self.middle.previous = p
            return res

    def popBack(self) -> int:
        if self.num == 0:
            return -1
        else:
            res = self.back.val
            self.num -= 1
            if self.num == 0:
                self.front = None
                self.back = None
                self.middle = None
            else:
                self.back = self.back.previous
                self.back.next = None
                if self.num % 2 != 0:
                    self.middle = self.middle.previous
            return res


if __name__ == "__main__":
    ops = ["FrontMiddleBackQueue","pushMiddle","pushMiddle","popMiddle","pushMiddle","pushFront","pushMiddle","popMiddle","pushMiddle","pushMiddle","popMiddle","pushFront","pushMiddle","pushMiddle","popMiddle","popBack","popBack","popBack","popMiddle","popMiddle","pushMiddle","popBack","popMiddle","popMiddle","pushMiddle","pushMiddle","pushMiddle","popMiddle"]
    par = [[],[636844],[469298],[],[902622],[86119],[714413],[],[508692],[936365],[],[233476],[640498],[462491],[],[],[],[],[],[],[903385],[],[],[],[762740],[676159],[639276],[]]
    fmbq = FrontMiddleBackQueue()
    res = []
    for i in range(1, len(par)):
        if ops[i] == "pushFront":
            res.append(fmbq.pushFront(par[i][0]))
        elif ops[i] == "pushBack":
            res.append(fmbq.pushBack(par[i][0]))
        elif ops[i] == "pushMiddle":
            res.append(fmbq.pushMiddle(par[i][0]))
        elif ops[i] == "popFront":
            res.append(fmbq.popFront())
        elif ops[i] == "popMiddle":
            res.append(fmbq.popMiddle())
        elif ops[i] == "popBack":
            res.append(fmbq.popBack())
    print(res)
