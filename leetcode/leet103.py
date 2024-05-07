# 103. 二叉树的锯齿形层序遍历
# 中等
# 相关标签
# 相关企业
# 给你二叉树的根节点 root ，返回其节点值的 锯齿形层序遍历 。（即先从左往右，再从右往左进行下一层遍历，以此类推，层与层之间交替进行）。
#
#
#
# 示例 1：
#
#
# 输入：root = [3,9,20,null,null,15,7]
# 输出：[[3],[20,9],[15,7]]
# 示例 2：
#
# 输入：root = [1]
# 输出：[[1]]
# 示例 3：
#
# 输入：root = []
# 输出：[]
#
#
# 提示：
#
# 树中节点数目在范围 [0, 2000] 内
# -100 <= Node.val <= 100
#

import heapq
import math
from collections import Counter, deque
from datetime import date
from functools import cache
from typing import List, Optional

from sortedcontainers import SortedList


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []
        if root is None:
            return res
        q = [root]
        zig = True
        while q:
            nq = deque()
            l = []
            for n in q:
                l.append(n.val)
                if zig:
                    if n.left:
                        nq.appendleft(n.left)
                    if n.right:
                        nq.appendleft(n.right)
                else:
                    if n.right:
                        nq.appendleft(n.right)
                    if n.left:
                        nq.appendleft(n.left)
            zig = not zig
            q = nq
            res.append(l)
        return res


if __name__ == "__main__":
    root = [3,9,20,None,None,15,7,1,2,None,4,5]
    r = TreeNode(root[0])
    l = [r]
    i = 1
    while i < len(root) - len(root) % 2:
        p = l[0]
        if root[i] is not None:
            n = TreeNode(root[i])
            p.left = n
            l.append(n)
        if i + 1 < len(root) and root[i + 1] is not None:
            n = TreeNode(root[i + 1])
            p.right = n
            l.append(n)
        l = l[1:]
        i += 2
    test = Solution().zigzagLevelOrder(r)
    print(test)
