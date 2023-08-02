import heapq
import math
from collections import Counter, deque
from functools import cache
from itertools import product
from typing import List, Optional


# 445. 两数相加 II
# 给你两个 非空 链表来代表两个非负整数。数字最高位位于链表开始位置。它们的每个节点只存储一位数字。将这两数相加会返回一个新的链表。
#
# 你可以假设除了数字 0 之外，这两个数字都不会以零开头。
#
#
#
# 示例1：
#
#
#
# 输入：l1 = [7,2,4,3], l2 = [5,6,4]
# 输出：[7,8,0,7]
# 示例2：
#
# 输入：l1 = [2,4,3], l2 = [5,6,4]
# 输出：[8,0,7]
# 示例3：
#
# 输入：l1 = [0], l2 = [0]
# 输出：[0]
#

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        def convert_to_num(l):
            res = 0
            p = l
            while p is not None:
                res = res * 10 + p.val
                p = p.next
            return res

        def convert_to_list(num):
            l = []
            if num == 0:
                l.append(0)
            while num > 0:
                l.append(num % 10)
                num = num // 10
            l.reverse()
            li = ListNode(l[0])
            n = li
            for i in l[1:]:
                no = ListNode(i)
                n.next = no
                n = n.next
            return li
        num1 = convert_to_num(l1)
        num2 = convert_to_num(l2)
        num = num1 + num2
        return convert_to_list(num)


if __name__ == "__main__":
    l1 = [0]
    l2 = [0]

    list1 = ListNode(l1[0])
    list2 = ListNode(l2[0])
    n1 = list1
    for i in l1[1:]:
        no = ListNode(i)
        n1.next = no
        n1 = n1.next

    n2 = list2
    for i in l2[1:]:
        no = ListNode(i)
        n2.next = no
        n2 = n2.next

    test = Solution().addTwoNumbers(list1, list2)

    while test is not None:
        print(test.val)
        test = test.next
