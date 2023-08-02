import math
from functools import lru_cache
from typing import List, Optional


# 1019. 链表中的下一个更大节点
# 给定一个长度为 n 的链表 head
#
# 对于列表中的每个节点，查找下一个 更大节点 的值。也就是说，对于每个节点，找到它旁边的第一个节点的值，这个节点的值 严格大于 它的值。
#
# 返回一个整数数组 answer ，其中 answer[i] 是第 i 个节点( 从1开始 )的下一个更大的节点的值。如果第 i 个节点没有下一个更大的节点，设置 answer[i] = 0 。
#
#
#
# 示例 1：
#
#
#
# 输入：head = [2,1,5]
# 输出：[5,5,0]
# 示例 2：
#
#
#
# 输入：head = [2,7,4,3,5]
# 输出：[7,0,5,5,0]
#
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def nextLargerNodes(self, head:Optional[ListNode]) -> List[int]:
        stk = []
        cur = head
        res = []

        i = 0
        while cur is not None:
            while len(stk) > 0:
                a = stk[len(stk) - 1][0]
                if a.val < cur.val:
                    res[stk[len(stk) - 1][1]] = cur.val
                    stk.pop()
                else:
                    break
            stk.append([cur, i])
            res.append(0)
            i += 1
            cur = cur.next
        return res

    def next(self, head):
        l = len(head)
        res = [0] * l
        if l == 1:
            return res
        for i in range(l - 2, -1, -1):
            if head[i] < head[i + 1]:
                res[i] = i + 1
            else:
                j = res[i + 1]
                while j != 0 and head[i] >= head[j]:
                    j = res[j]
                res[i] = j
        return [head[i] if i > 0 else 0 for i in res]


if __name__ == "__main__":
    head = [2,7,4,3,5]
    node = ListNode(head[0])
    n = node
    for i in head[1:]:
        no = ListNode(i)
        n.next = no
        n = n.next
    # test = Solution().next(head)
    test = Solution().nextLargerNodes(node)
    print(test)
