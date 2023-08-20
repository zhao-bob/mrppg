import heapq
import math
from collections import Counter, deque
from functools import cache
from itertools import product
from typing import List, Optional


# 23. 合并 K 个升序链表
# 困难
# 给你一个链表数组，每个链表都已经按升序排列。
#
# 请你将所有链表合并到一个升序链表中，返回合并后的链表。
#
#
#
# 示例 1：
#
# 输入：lists = [[1,4,5],[1,3,4],[2,6]]
# 输出：[1,1,2,3,4,4,5,6]
# 解释：链表数组如下：
# [
#   1->4->5,
#   1->3->4,
#   2->6
# ]
# 将它们合并到一个有序链表中得到。
# 1->1->2->3->4->4->5->6
# 示例 2：
#
# 输入：lists = []
# 输出：[]
# 示例 3：
#
# 输入：lists = [[]]
# 输出：[]

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        class CListNode:
            def __init__(self, ln=None):
                self.node = ln

            def __lt__(self, other):
                if self.node.val < other.node.val:
                    return True
                else:
                    return False
        h = []
        for i in range(len(lists)):
            if lists[i] is not None:
                heapq.heappush(h, CListNode(lists[i]))
        if len(h) == 0:
            return None
        res = ListNode()
        p = res
        while h:
            n = heapq.heappop(h)
            p.next = n.node
            p = p.next
            if n.node.next is not None:
                heapq.heappush(h, CListNode(n.node.next))
        return res.next


if __name__ == "__main__":
    lists = [[1,4,5],[1,3,4],[2,6]]
    nl = [None] * len(lists)
    for i in range(len(lists)):
        if len(lists[i]) > 0:
            nl[i] = ListNode(lists[i][0])
            n = nl[i]
            for j in lists[i][1:]:
                no = ListNode(j)
                n.next = no
                n = n.next

    test = Solution().mergeKLists(nl)
    while test is not None:
        print(test.val)
        test = test.next
