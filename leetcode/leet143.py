import heapq
import math
from collections import Counter, deque
from functools import cache
from itertools import product
from typing import List, Optional


# 143. 重排链表
# 中等
# 给定一个单链表 L 的头节点 head ，单链表 L 表示为：
#
# L0 → L1 → … → Ln - 1 → Ln
# 请将其重新排列后变为：
#
# L0 → Ln → L1 → Ln - 1 → L2 → Ln - 2 → …
# 不能只是单纯的改变节点内部的值，而是需要实际的进行节点交换。
#
#
#
# 示例 1：
#
#
#
# 输入：head = [1,2,3,4]
# 输出：[1,4,2,3]
# 示例 2：
#
#
#
# 输入：head = [1,2,3,4,5]
# 输出：[1,5,2,4,3]
#
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        s = head
        f = head
        while f.next and f.next.next:
            s = s.next
            f = f.next.next
        f = None
        while s is not None:
            p = s.next
            s.next = f
            f = s
            s = p
        s = head
        while f is not None:
            p = s.next
            s.next = f
            q = f.next
            if q is None:
                if p is not None:
                    f.next = p
                    p.next = None
                return
            f.next = p
            s = p
            f = q

    # s = head
    # f = head
    # while f.next and f.next.next:
    #     s = s.next
    #     f = f.next.next
    # f = None
    # while s:
    #     p = s.next
    #     s.next = f
    #     f = s
    #     s = p
    # s = head
    # while f and s:
    #     p = s.next
    #     s.next = f
    #     q = f.next
    #     f.next = p
    #     s = p
    #     f = q


if __name__ == "__main__":
    head = [1,2,3,4,5]
    node = ListNode(head[0])
    n = node
    p = None
    for i in range(1, len(head)):
        no = ListNode(head[i])
        n.next = no
        n = n.next
    n.next = p

    Solution().reorderList(node)
    # print(test)
