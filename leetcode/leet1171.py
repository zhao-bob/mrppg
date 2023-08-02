import heapq
import math
from collections import Counter
from typing import List, Optional


# 1171. 从链表中删去总和值为零的连续节点
# 给你一个链表的头节点 head，请你编写代码，反复删去链表中由 总和 值为 0 的连续节点组成的序列，直到不存在这样的序列为止。
#
# 删除完毕后，请你返回最终结果链表的头节点。
#
#
#
# 你可以返回任何满足题目要求的答案。
#
# （注意，下面示例中的所有序列，都是对 ListNode 对象序列化的表示。）
#
# 示例 1：
#
# 输入：head = [1,2,-3,3,1]
# 输出：[3,1]
# 提示：答案 [1,2,1] 也是正确的。
# 示例 2：
#
# 输入：head = [1,2,3,-3,4]
# 输出：[1,2,4]
# 示例 3：
#
# 输入：head = [1,2,3,-3,-2]
# 输出：[1]
#

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeZeroSumSublists(self, head: Optional[ListNode]) -> Optional[ListNode]:
        s = head
        t = head
        cs = 0

        while t is not None:
            if cs + t.val == 0:
                s = t.next
                cs = 0
            else:
                c = s
                cs += t.val
                ss = cs
                ns = 0
                while c != t:
                    ss -= c.val
                    ns += c.val
                    if ss == 0:
                        c.next = t.next
                        cs = ns
                        break
                    else:
                        c = c.next
            t = t.next

        return s

    def removeZeroSumSublists1(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prefix = 0
        seen = {}
        seen[0] = dummy = ListNode(0)
        dummy.next = head
        while head:
            prefix += head.val
            seen[prefix] = head
            head = head.next
        head = dummy
        prefix = 0
        while head:
            prefix += head.val
            head.next = seen[prefix].next
            head = head.next
        return dummy.next



if __name__ == "__main__":
    head = [1,2,1,-2,0,0]

    node = ListNode(head[0])
    n = node
    for i in head[1:]:
        no = ListNode(i)
        n.next = no
        n = n.next

    test = Solution().removeZeroSumSublists(node)

    while test is not None:
        print(test.val)
        test = test.next
