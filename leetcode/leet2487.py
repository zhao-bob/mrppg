# 2487. 从链表中移除节点
# 提示
# 中等
# 49
# 相关企业
# 给你一个链表的头节点 head 。
#
# 移除每个右侧有一个更大数值的节点。
#
# 返回修改后链表的头节点 head 。
#
#
#
# 示例 1：
#
#
#
# 输入：head = [5,2,13,3,8]
# 输出：[13,8]
# 解释：需要移除的节点是 5 ，2 和 3 。
# - 节点 13 在节点 5 右侧。
# - 节点 13 在节点 2 右侧。
# - 节点 8 在节点 3 右侧。
# 示例 2：
#
# 输入：head = [1,1,1,1]
# 输出：[1,1,1,1]
# 解释：每个节点的值都是 1 ，所以没有需要移除的节点。
#

import heapq
import math
from collections import Counter
from datetime import date
from typing import List, Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        stk = []
        h = head
        res = ListNode()
        res.next = head
        while h is not None:
            if stk and stk[-1].val < h.val:
                while stk and stk[-1].val < h.val:
                    stk.pop()
                if stk:
                    stk[-1].next = h
                else:
                    res.next = h
            stk.append(h)
            h = h.next
        return res.next


if __name__ == "__main__":
    head = [1,1,1,1]

    node = ListNode(head[0])
    n = node
    for i in head[1:]:
        no = ListNode(i)
        n.next = no
        n = n.next

    test = Solution().removeNodes(node)

    while test is not None:
        print(test.val)
        test = test.next

