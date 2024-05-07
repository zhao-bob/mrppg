# 102. 二叉树的层序遍历
# 中等
# 相关标签
# 相关企业
# 给你二叉树的根节点 root ，返回其节点值的 层序遍历 。 （即逐层地，从左到右访问所有节点）。
#
#
#
# 示例 1：
#
#
# 输入：root = [3,9,20,null,null,15,7]
# 输出：[[3],[9,20],[15,7]]
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
# -1000 <= Node.val <= 1000
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
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []
        q = [root]

        while q:
            nq = []
            l = []
            for n in q:
                l.append(n.val)
                if n.left:
                    nq.append(n.left)
                if n.right:
                    nq.append(n.right)
            q = nq
            res.append(l)
        return res


if __name__ == "__main__":
    root = []
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
    test = Solution().levelOrder(r)
    print(test)
