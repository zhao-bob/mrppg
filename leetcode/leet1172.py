import math
from typing import List


# 1172. 餐盘栈
# 我们把无限数量 ∞ 的栈排成一行，按从左到右的次序从 0 开始编号。每个栈的的最大容量 capacity 都相同。
#
# 实现一个叫「餐盘」的类 DinnerPlates：
#
# DinnerPlates(int capacity) - 给出栈的最大容量 capacity。
# void push(int val) - 将给出的正整数 val 推入 从左往右第一个 没有满的栈。
# int pop() - 返回 从右往左第一个 非空栈顶部的值，并将其从栈中删除；如果所有的栈都是空的，请返回 -1。
# int popAtStack(int index) - 返回编号 index 的栈顶部的值，并将其从栈中删除；如果编号 index 的栈是空的，请返回 -1。
#
#
# 示例：
#
# 输入：
# ["DinnerPlates","push","push","push","push","push","popAtStack","push","push","popAtStack","popAtStack","pop","pop","pop","pop","pop"]
# [[2],[1],[2],[3],[4],[5],[0],[20],[21],[0],[2],[],[],[],[],[]]
# 输出：
# [null,null,null,null,null,null,2,null,null,20,21,5,4,3,1,-1]
#
# 解释：
# DinnerPlates D = DinnerPlates(2);  // 初始化，栈最大容量 capacity = 2
# D.push(1);
# D.push(2);
# D.push(3);
# D.push(4);
# D.push(5);         // 栈的现状为：    2  4
#                                     1  3  5
#                                     ﹈ ﹈ ﹈
# D.popAtStack(0);   // 返回 2。栈的现状为：      4
#                                           1  3  5
#                                           ﹈ ﹈ ﹈
# D.push(20);        // 栈的现状为：  20  4
#                                    1  3  5
#                                    ﹈ ﹈ ﹈
# D.push(21);        // 栈的现状为：  20  4 21
#                                    1  3  5
#                                    ﹈ ﹈ ﹈
# D.popAtStack(0);   // 返回 20。栈的现状为：       4 21
#                                             1  3  5
#                                             ﹈ ﹈ ﹈
# D.popAtStack(2);   // 返回 21。栈的现状为：       4
#                                             1  3  5
#                                             ﹈ ﹈ ﹈
# D.pop()            // 返回 5。栈的现状为：        4
#                                             1  3
#                                             ﹈ ﹈
# D.pop()            // 返回 4。栈的现状为：    1  3
#                                            ﹈ ﹈
# D.pop()            // 返回 3。栈的现状为：    1
#                                            ﹈
# D.pop()            // 返回 1。现在没有栈。
# D.pop()            // 返回 -1。仍然没有栈。
#

class DinnerPlates:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.stack = []
        self.state = []

    def push(self, val: int) -> None:
        if len(self.state) == 0:
            self.stack.append([val])
            state = 1
            if state < self.capacity:
                self.state.append([len(self.stack) - 1, 1])
        else:
            s = self.state[0]
            self.stack[s[0]].append(val)
            s[1] += 1
            if s[1] == self.capacity:
                self.state = self.state[1:]

    def pop(self) -> int:
        if len(self.stack) == 0:
            return -1
        i = len(self.stack) - 1
        p = self.stack[i]
        while len(p) == 0:
            self.stack.pop()
            p = self.stack[-1]
        if len(self.state) == 0 or self.state[-1][0] < i:
            if self.capacity - 1 > 0:
                self.state.append([i, self.capacity - 1])
        else:
            self.state[-1][1] -= 1
            if self.state[-1][1] <= 0:
                self.state.pop()
        v = p.pop()
        if len(p) == 0:
            self.stack.pop()
        return v

    def popAtStack(self, index: int) -> int:
        if index >= len(self.stack):
            return -1
        p = self.stack[index]
        if len(p) == 0:
            return -1
        v = p.pop()
        if len(self.state) == 0:
            self.state.append([index, self.capacity - 1])
        else:
            if self.state[0][0] > index:
                self.state = [[index, self.capacity - 1]] + self.state
            elif self.state[-1][0] < index:
                if self.capacity - 1 > 0:
                    self.state.append([index, self.capacity - 1])
            else:
                for i in range(len(self.state)):
                    if self.state[i][0] == index:
                        self.state[i][1] -= 1
                    else:
                        if self.state[i][0] > index:
                            self.state = self.state[:i - 1] + [[index, self.capacity - 1]] + self.state[i:]
                            break
        if len(p) == 0 and index == len(self.stack) - 1:
            self.stack.pop()
            self.state.pop()
        return v

        # def __init__(self, capacity: int):
        #     self.capacity = capacity
        #     self.stack = []
        #     self.top = []
        #     self.poppedPos = SortedSet()
        #
        # def push(self, val: int) -> None:
        #     if not self.poppedPos:
        #         pos = len(self.stack)
        #         self.stack.append(val)
        #         if pos % self.capacity == 0:
        #             self.top.append(0)
        #         else:
        #             stackPos = len(self.top) - 1
        #             stackTop = self.top[stackPos]
        #             self.top[stackPos] = stackTop + 1
        #     else:
        #         pos = self.poppedPos.pop(0)
        #         self.stack[pos] = val
        #         index = pos // self.capacity
        #         stackTop = self.top[index]
        #         self.top[index] = stackTop + 1
        #
        # def pop(self) -> int:
        #     while self.stack and self.poppedPos and self.poppedPos[-1] == len(self.stack) - 1:
        #         self.stack.pop()
        #         pos = self.poppedPos.pop()
        #         if pos % self.capacity == 0:
        #             self.top.pop()
        #     if not self.stack:
        #         return -1
        #     else:
        #         pos = len(self.stack) - 1
        #         val = self.stack[pos]
        #         self.stack.pop()
        #         if pos % self.capacity == 0 and self.top:
        #             self.top.pop()
        #         elif self.top:
        #             self.top[-1] -= 1
        #         return val
        #
        # def popAtStack(self, index: int) -> int:
        #     if index >= len(self.top):
        #         return -1
        #     stackTop = self.top[index]
        #     if stackTop < 0:
        #         return -1
        #     self.top[index] = stackTop - 1
        #     pos = index * self.capacity + stackTop
        #     self.poppedPos.add(pos)
        #     return self.stack[pos]


if __name__ == "__main__":
    op = ["DinnerPlates","push","push","push","push","push","push","push","push","popAtStack","popAtStack","popAtStack","popAtStack","popAtStack","popAtStack","popAtStack","popAtStack","popAtStack","popAtStack","push","push","push","push","push","push","push","push","pop","pop","pop","pop","pop","pop","pop","pop","pop","pop"]
    l= [[2],[472],[106],[497],[498],[73],[115],[437],[461],[3],[3],[1],[3],[0],[2],[2],[1],[1],[3],[197],[239],[129],[449],[460],[240],[386],[343],[],[],[],[],[],[],[],[],[],[]]
    dp = DinnerPlates(l[0][0])

    res = [None] * len(op)
    for i in range(1, len(l)):
        if op[i] == "push":
            res[i] = dp.push(l[i][0])
        elif op[i] == "popAtStack":
            res[i] = dp.popAtStack(l[i][0])
        elif op[i] == "pop":
            res[i] = dp.pop()
    print(res)
