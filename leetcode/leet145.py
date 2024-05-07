# 145. 二叉树的后序遍历
# 简单
# 相关标签
# 相关企业
# 给你一棵二叉树的根节点 root ，返回其节点值的 后序遍历 。
#
#
#
# 示例 1：
#
#
# 输入：root = [1,null,2,3]
# 输出：[3,2,1]
# 示例 2：
#
# 输入：root = []
# 输出：[]
# 示例 3：
#
# 输入：root = [1]
# 输出：[1]
#
#
# 提示：
#
# 树中节点的数目在范围 [0, 100] 内
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
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []

        # def postorder(n):
        #     if n is None:
        #         return
        #     postorder(n.left)
        #     postorder(n.right)
        #     res.append(n.val)
        # 
        # postorder(root)
        stk = []
        searched = set()
        while root or stk:
            while root and root not in searched:
                stk.append(root)
                searched.add(root)
                root = root.left
            root = stk[-1]
            if stk[-1].right and stk[-1].right not in searched:
                root = root.right
            else:
                res.append(root.val)
                stk.pop()
                if stk:
                    root = stk[-1]
                else:
                    root = None
        return res


if __name__ == "__main__":
    root = [1,2,3,None,5,6,7,8,9]
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
    test = Solution().postorderTraversal(r)
    print(test)
