# 235. 二叉搜索树的最近公共祖先
# 中等
# 相关标签
# 相关企业
# 给定一个二叉搜索树, 找到该树中两个指定节点的最近公共祖先。
#
# 百度百科中最近公共祖先的定义为：“对于有根树 T 的两个结点 p、q，最近公共祖先表示为一个结点 x，满足 x 是 p、q 的祖先且 x 的深度尽可能大（一个节点也可以是它自己的祖先）。”
#
# 例如，给定如下二叉搜索树:  root = [6,2,8,0,4,7,9,null,null,3,5]
#
#
#
#
#
# 示例 1:
#
# 输入: root = [6,2,8,0,4,7,9,null,null,3,5], p = 2, q = 8
# 输出: 6
# 解释: 节点 2 和节点 8 的最近公共祖先是 6。
# 示例 2:
#
# 输入: root = [6,2,8,0,4,7,9,null,null,3,5], p = 2, q = 4
# 输出: 2
# 解释: 节点 2 和节点 4 的最近公共祖先是 2, 因为根据定义最近公共祖先节点可以为节点本身。
#
#
# 说明:
#
# 所有节点的值都是唯一的。
# p、q 为不同节点且均存在于给定的二叉搜索树中。
#

import heapq
import math
from collections import Counter, deque, defaultdict
from datetime import date
from functools import cache
from typing import List, Optional

from sortedcontainers import SortedList


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':

        def search(r, p, l):
            l.append(r)
            if r.val == p.val:
                return
            if r.val > p.val:
                search(r.left, p, l)
            else:
                search(r.right, p, l)
        l1 = []
        search(root, p, l1)
        l2 = []
        search(root, q, l2)
        n = 0
        while n < min(len(l1), len(l2)) and l1[n].val == l2[n].val:
            n += 1
        return l1[n - 1]


if __name__ == "__main__":
    root = [6,2,8,0,4,7,9,None,None,3,5]
    p = 2
    q = 4
    r = TreeNode(root[0])
    l = [r]
    i = 1
    while i < len(root) - len(root) % 2:
        x = l[0]
        if root[i] is not None:
            n = TreeNode(root[i])
            x.left = n
            l.append(n)
        if i + 1 < len(root) and root[i + 1] is not None:
            n = TreeNode(root[i + 1])
            x.right = n
            l.append(n)
        l = l[1:]
        i += 2
    test = Solution().lowestCommonAncestor(r, TreeNode(p),TreeNode(q))
    print(test.val)
