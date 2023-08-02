import heapq
import math
from collections import Counter, deque
from functools import cache
from itertools import product
from typing import List, Optional


# 2. 两数相加
# 给你两个 非空 的链表，表示两个非负的整数。它们每位数字都是按照 逆序 的方式存储的，并且每个节点只能存储 一位 数字。
#
# 请你将两个数相加，并以相同形式返回一个表示和的链表。
#
# 你可以假设除了数字 0 之外，这两个数都不会以 0 开头。
#
#
#
# 示例 1：
#
#
# 输入：l1 = [2,4,3], l2 = [5,6,4]
# 输出：[7,0,8]
# 解释：342 + 465 = 807.
# 示例 2：
#
# 输入：l1 = [0], l2 = [0]
# 输出：[0]
# 示例 3：
#
# 输入：l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
# 输出：[8,9,9,9,0,0,0,1]
#

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carry = 0
        p1 = l1
        p2 = l2
        r = ListNode()
        i = r
        while p1 is not None or p2 is not None:
            a = 0
            b = 0
            if p1 is not None:
                a = p1.val
            if p2 is not None:
                b = p2.val
            val = (a + b + carry) % 10
            carry = (a + b + carry) // 10

            ln = ListNode(val=val)
            i.next = ln
            i = i.next
            if p1 is not None:
                p1 = p1.next
            if p2 is not None:
                p2 = p2.next
        if carry != 0:
            ln = ListNode(val=carry)
            i.next = ln
        return r.next


if __name__ == "__main__":
    l1 = [9,9,9,9,9,9,9]
    l2 = [9,9,9,9]

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
