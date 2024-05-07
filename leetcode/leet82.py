# 82. 删除排序链表中的重复元素 II
# 中等
# 相关标签
# 相关企业
# 给定一个已排序的链表的头 head ， 删除原始链表中所有重复数字的节点，只留下不同的数字 。返回 已排序的链表 。
#
#
#
# 示例 1：
#
#
# 输入：head = [1,2,3,3,4,4,5]
# 输出：[1,2,5]
# 示例 2：
#
#
# 输入：head = [1,1,1,2,3]
# 输出：[2,3]
#
#
# 提示：
#
# 链表中节点数目在范围 [0, 300] 内
# -100 <= Node.val <= 100
# 题目数据保证链表已经按升序 排列
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
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(101, head)
        pre = dummy
        cur = dummy.next
        while cur.next:
            nxt = cur.next
            if nxt.val == cur.val:
                while nxt and nxt.val == cur.val:
                    nxt = nxt.next
                if nxt:
                    pre.next = nxt
                    cur = nxt
                else:
                    pre.next = nxt
                    break
            else:
                pre = cur
                cur = nxt
        return dummy.next




if __name__ == "__main__":
    head = [1,1,1,2,3]

    node = ListNode(head[0])
    n = node
    for i in head[1:]:
        no = ListNode(i)
        n.next = no
        n = n.next

    test = Solution().deleteDuplicates(node)

    while test is not None:
        print(test.val)
        test = test.next
