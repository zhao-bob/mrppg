import heapq
import math
from collections import Counter, deque
from functools import cache
from itertools import product
from typing import List, Optional


# 24. 两两交换链表中的节点
# 中等
# 给你一个链表，两两交换其中相邻的节点，并返回交换后链表的头节点。你必须在不修改节点内部的值的情况下完成本题（即，只能进行节点交换）。
#
#
#
# 示例 1：
#
#
# 输入：head = [1,2,3,4]
# 输出：[2,1,4,3]
# 示例 2：
#
# 输入：head = []
# 输出：[]
# 示例 3：
#
# 输入：head = [1]
# 输出：[1]

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next is None:
            return head
        h = ListNode()
        h.next = head
        f = h
        s = f.next
        while s is not None and s.next is not None:
            n = s.next
            f.next = n
            s.next = n.next
            n.next = s
            f = s
            s = f.next
        return h.next


if __name__ == "__main__":
    head = [1,2,3,4,5,6]
    h = None
    if len(head) > 0:
        h = ListNode(head[0])
        n = h
        for i in head[1:]:
            no = ListNode(i)
            n.next = no
            n = n.next

    test = Solution().swapPairs(h)
    while test is not None:
        print(test.val)
        test = test.next
