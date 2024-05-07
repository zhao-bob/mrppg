# 236. 二叉树的最近公共祖先
# 中等
# 相关标签
# 相关企业
# 给定一个二叉树, 找到该树中两个指定节点的最近公共祖先。
#
# 百度百科中最近公共祖先的定义为：“对于有根树 T 的两个节点 p、q，最近公共祖先表示为一个节点 x，满足 x 是 p、q 的祖先且 x 的深度尽可能大（一个节点也可以是它自己的祖先）。”
#
#
#
# 示例 1：
#
#
# 输入：root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 1
# 输出：3
# 解释：节点 5 和节点 1 的最近公共祖先是节点 3 。
# 示例 2：
#
#
# 输入：root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 4
# 输出：5
# 解释：节点 5 和节点 4 的最近公共祖先是节点 5 。因为根据定义最近公共祖先节点可以为节点本身。
# 示例 3：
#
# 输入：root = [1,2], p = 1, q = 2
# 输出：1
#
#
# 提示：
#
# 树中节点数目在范围 [2, 105] 内。
# -109 <= Node.val <= 109
# 所有 Node.val 互不相同 。
# p != q
# p 和 q 均存在于给定的二叉树中。
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
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        def dfs(r, p, l):
            if r is None:
                return False
            if p.val == r.val:
                return True
            if dfs(r.left, p, l) or dfs(r.right, p, l):
                l.append(r)
                return True
            else:
                return False

        l1 =[p]
        l2 = [q]
        dfs(root, p, l1)
        dfs(root, q, l2)




if __name__ == "__main__":
    root = [3,5,1,6,2,0,8,None,None,7,4]
    x = 5
    y = 4
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
    test = Solution().lowestCommonAncestor(r, TreeNode(val=x), TreeNode(val=y))
    print(test.val)
