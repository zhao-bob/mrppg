import heapq
import math
from collections import Counter, deque
from functools import cache
from itertools import product
from typing import List, Optional


# 21. 合并两个有序链表
# 简单
# 3.2K
# 相关企业
# 将两个升序链表合并为一个新的 升序 链表并返回。新链表是通过拼接给定的两个链表的所有节点组成的。
#
#
#
# 示例 1：
#
#
# 输入：l1 = [1,2,4], l2 = [1,3,4]
# 输出：[1,1,2,3,4,4]
# 示例 2：
#
# 输入：l1 = [], l2 = []
# 输出：[]
# 示例 3：
#
# 输入：l1 = [], l2 = [0]
# 输出：[0]

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        l1 = list1
        l2 = list2
        n = ListNode()
        l = n
        while l1 is not None or l2 is not None:
            if l1 is None:
                l.next = l2
                break
            elif l2 is None:
                l.next = l1
                break
            else:
                if l1.val <= l2.val:
                    l.next = l1
                    l1 = l1.next
                else:
                    l.next = l2
                    l2 = l2.next
            l = l.next
        return n.next


if __name__ == "__main__":
    l1 = []
    l2 = []
    n1 = None
    if len(l1) > 0:
        n1 = ListNode(l1[0])
        n = n1
        for i in l1[1:]:
            no = ListNode(i)
            n.next = no
            n = n.next
    n2 = None
    if len(l2) > 0:
        n2 = ListNode(l2[0])
        n = n2
        for i in l2[1:]:
            no = ListNode(i)
            n.next = no
            n = n.next
    test = Solution().mergeTwoLists(n1, n2)
    while test is not None:
        print(test.val)
        test = test.next
