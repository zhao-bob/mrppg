# 2641. 二叉树的堂兄弟节点 II
# 中等
# 相关标签
# 相关企业
# 提示
# 给你一棵二叉树的根 root ，请你将每个节点的值替换成该节点的所有 堂兄弟节点值的和 。
#
# 如果两个节点在树中有相同的深度且它们的父节点不同，那么它们互为 堂兄弟 。
#
# 请你返回修改值之后，树的根 root 。
#
# 注意，一个节点的深度指的是从树根节点到这个节点经过的边数。
#
#
#
# 示例 1：
#
#
#
# 输入：root = [5,4,9,1,10,null,7]
# 输出：[0,0,0,7,7,null,11]
# 解释：上图展示了初始的二叉树和修改每个节点的值之后的二叉树。
# - 值为 5 的节点没有堂兄弟，所以值修改为 0 。
# - 值为 4 的节点没有堂兄弟，所以值修改为 0 。
# - 值为 9 的节点没有堂兄弟，所以值修改为 0 。
# - 值为 1 的节点有一个堂兄弟，值为 7 ，所以值修改为 7 。
# - 值为 10 的节点有一个堂兄弟，值为 7 ，所以值修改为 7 。
# - 值为 7 的节点有两个堂兄弟，值分别为 1 和 10 ，所以值修改为 11 。
# 示例 2：
#
#
#
# 输入：root = [3,1,2]
# 输出：[0,0,0]
# 解释：上图展示了初始的二叉树和修改每个节点的值之后的二叉树。
# - 值为 3 的节点没有堂兄弟，所以值修改为 0 。
# - 值为 1 的节点没有堂兄弟，所以值修改为 0 。
# - 值为 2 的节点没有堂兄弟，所以值修改为 0 。
#
#
# 提示：
#
# 树中节点数目的范围是 [1, 105] 。
# 1 <= Node.val <= 104
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
    def replaceValueInTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        s = [(root, 0)]
        k = -1
        while s:
            ns = []
            v = {}
            p = -1
            t = 0
            a = 0
            for i in range(len(s)):
                k += 1
                t += s[i][0].val
                if s[i][1] != p:
                    if p != -1:
                        v[p] = a
                    a = s[i][0].val
                else:
                    a += s[i][0].val
                if s[i][0].left:
                    ns.append((s[i][0].left, k))
                if s[i][0].right:
                    ns.append((s[i][0].right, k))
                p = s[i][1]
            v[p] = a
            for i in range(len(s)):
                s[i][0].val = t - v[s[i][1]]
            s = ns
        return root



if __name__ == "__main__":
    root = [5,4,9,1,10,None,7]
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
    test = Solution().replaceValueInTree(r)
    res = []
    stk = [test]
    while len(stk) > 0:
        n = stk[0]
        stk = stk[1:]
        if n is not None:
            res.append(n.val)
            if n.left is not None or n.right is not None:
                stk.append(n.left)
                stk.append(n.right)
        else:
            res.append(None)
    print(res)
