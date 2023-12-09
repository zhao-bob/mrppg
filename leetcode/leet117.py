import heapq
import math
from collections import Counter
from functools import cache
from typing import List, Optional
from sortedcontainers import SortedList


# 117. 填充每个节点的下一个右侧节点指针 II
# 中等
# 773
# 相关企业
# 给定一个二叉树：
#
# struct Node {
#   int val;
#   Node *left;
#   Node *right;
#   Node *next;
# }
# 填充它的每个 next 指针，让这个指针指向其下一个右侧节点。如果找不到下一个右侧节点，则将 next 指针设置为 NULL 。
#
# 初始状态下，所有 next 指针都被设置为 NULL 。
#
#
#
# 示例 1：
#
#
# 输入：root = [1,2,3,4,5,null,7]
# 输出：[1,#,2,3,#,4,5,7,#]
# 解释：给定二叉树如图 A 所示，你的函数应该填充它的每个 next 指针，以指向其下一个右侧节点，如图 B 所示。序列化输出按层序遍历顺序（由 next 指针连接），'#' 表示每层的末尾。
# 示例 2：
#
# 输入：root = []
# 输出：[]
#
#
# 提示：
#
# 树中的节点数在范围 [0, 6000] 内
# -100 <= Node.val <= 100
# 进阶：
#
# 你只能使用常量级额外空间。
# 使用递归解题也符合要求，本题中递归程序的隐式栈空间不计入额外空间复杂度。
#


# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next

class Solution:
    def connect(self, root: Optional[Node]) -> Optional[Node]:
        if root is None:
            return root
        q = [(root, 0)]
        while q:
            n, l = q[0]
            q = q[1:]
            if q and q[0][1] == l:
                n.next = q[0][0]
            if n.left is not None:
                q.append((n.left, l + 1))
            if n.right is not None:
                q.append((n.right, l + 1))
        return root

#     cur = root
#         while cur:
#             nxt = dummy = ListNode()  # 下一层的链表
#             while cur:  # 遍历当前层的链表
#                 if cur.left:
#                     nxt.next = cur.left  # 下一层的相邻节点连起来
#                     nxt = cur.left
#                 if cur.right:
#                     nxt.next = cur.right  # 下一层的相邻节点连起来
#                     nxt = cur.right
#                 cur = cur.next  # 当前层链表的下一个节点
#             cur = dummy.next  # 下一层链表的头节点
#         return root


if __name__ == "__main__":
    root = []
    r = Node(root[0])
    l = [r]
    i = 1
    while i < len(root) - len(root) % 2:
        p = l[0]
        if root[i] is not None:
            n = Node(root[i])
            p.left = n
            l.append(n)
        if i + 1 < len(root) and root[i + 1] is not None:
            n = Node(root[i + 1])
            p.right = n
            l.append(n)
        l = l[1:]
        i += 2
    test = Solution().connect(r)
    print(test)
