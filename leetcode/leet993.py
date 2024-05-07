# 993. 二叉树的堂兄弟节点
# 简单
# 相关标签
# 相关企业
# 在二叉树中，根节点位于深度 0 处，每个深度为 k 的节点的子节点位于深度 k+1 处。
#
# 如果二叉树的两个节点深度相同，但 父节点不同 ，则它们是一对堂兄弟节点。
#
# 我们给出了具有唯一值的二叉树的根节点 root ，以及树中两个不同节点的值 x 和 y 。
#
# 只有与值 x 和 y 对应的节点是堂兄弟节点时，才返回 true 。否则，返回 false。
#
#
#
# 示例 1：
#
#
# 输入：root = [1,2,3,4], x = 4, y = 3
# 输出：false
# 示例 2：
#
#
# 输入：root = [1,2,3,null,4,null,5], x = 5, y = 4
# 输出：true
# 示例 3：
#
#
#
# 输入：root = [1,2,3,null,4], x = 2, y = 3
# 输出：false
#
#
# 提示：
#
# 二叉树的节点数介于 2 到 100 之间。
# 每个节点的值都是唯一的、范围为 1 到 100 的整数。
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
    def isCousins(self, root: Optional[TreeNode], x: int, y: int) -> bool:

        def dfs(r, n, k):
            if r:
                if r.left and r.left.val == n or r.right and r.right.val == n:
                    return r, k + 1
                else:
                    return dfs(r.left, n, k + 1) or dfs(r.right, n, k + 1)
        r = TreeNode(left = root)
        p1, k1 = dfs(r, x, 0)
        p2, k2 = dfs(r, y, 0)
        if k1 == k2 and p1 != p2:
            return True
        else:
            return False



if __name__ == "__main__":
    root = [1,None,2,3,None,None,4,None,5]
    x = 1
    y = 3
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
    test = Solution().isCousins(r, x, y)
    print(test)
