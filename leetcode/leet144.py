# 144. 二叉树的前序遍历
# 简单
# 相关标签
# 相关企业
# 给你二叉树的根节点 root ，返回它节点值的 前序 遍历。
#
#
#
# 示例 1：
#
#
# 输入：root = [1,null,2,3]
# 输出：[1,2,3]
# 示例 2：
#
# 输入：root = []
# 输出：[]
# 示例 3：
#
# 输入：root = [1]
# 输出：[1]
# 示例 4：
#
#
# 输入：root = [1,2]
# 输出：[1,2]
# 示例 5：
#
#
# 输入：root = [1,null,2]
# 输出：[1,2]
#
#
# 提示：
#
# 树中节点数目在范围 [0, 100] 内
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
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        stk = []
        # def preorder(n):
        #     if n is None:
        #         return
        #     res.append(n.val)
        #     preorder(n.left)
        #     preorder(n.right)
        #
        # preorder(root)
        while root or stk:
            if root is None:
               root = stk.pop()
            res.append(root.val)
            if root.right:
               stk.append(root.right)
            root = root.left
        return res


if __name__ == "__main__":
    root = [1,4,3,2]
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
    test = Solution().preorderTraversal(r)
    print(test)
