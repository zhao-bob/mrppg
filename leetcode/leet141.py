import heapq
import math
from collections import Counter, deque
from functools import cache
from itertools import product
from typing import List, Optional


# 141. 环形链表
# 简单
# 给你一个链表的头节点 head ，判断链表中是否有环。
#
# 如果链表中有某个节点，可以通过连续跟踪 next 指针再次到达，则链表中存在环。 为了表示给定链表中的环，评测系统内部使用整数 pos 来表示链表尾连接到链表中的位置（索引从 0 开始）。注意：pos 不作为参数进行传递 。仅仅是为了标识链表的实际情况。
#
# 如果链表中存在环 ，则返回 true 。 否则，返回 false 。
#
#
#
# 示例 1：
#
#
#
# 输入：head = [3,2,0,-4], pos = 1
# 输出：true
# 解释：链表中有一个环，其尾部连接到第二个节点。
# 示例 2：
#
#
#
# 输入：head = [1,2], pos = 0
# 输出：true
# 解释：链表中有一个环，其尾部连接到第一个节点。
# 示例 3：
#
#
#
# 输入：head = [1], pos = -1
# 输出：false
# 解释：链表中没有环。
#
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        hashset = set()
        h = head
        hashset.add(h.__hash__())
        while h is not None:
            if h.next is None:
                return False
            else:
                if h.next.__hash__() in hashset:
                    return True
            h = h.next
            hashset.add(h.__hash__())
        return False


if __name__ == "__main__":
    head = [3,2,0,-4]
    pos = 1
    node = ListNode(head[0])
    n = node
    p = None
    if pos == 0:
        p = node
    for i in range(1, len(head)):
        no = ListNode(head[i])
        if i == pos:
            p = no
        n.next = no
        n = n.next
    n.next = p

    test = Solution().hasCycle(node)
    print(test)
