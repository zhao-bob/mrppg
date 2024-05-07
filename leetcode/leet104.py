# 104. 二叉树的最大深度
# 简单
# 相关标签
# 相关企业
# 给定一个二叉树 root ，返回其最大深度。
#
# 二叉树的 最大深度 是指从根节点到最远叶子节点的最长路径上的节点数。
#
#
#
# 示例 1：
#
#
#
#
#
# 输入：root = [3,9,20,null,null,15,7]
# 输出：3
# 示例 2：
#
# 输入：root = [1,null,2]
# 输出：2
# 提示：
#
# 树中节点的数量在 [0, 104] 区间内。
# -100 <= Node.val <= 100
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
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        def dfs(r, n):
            if r is None:
                return n
            return max(dfs(r.left, n + 1), dfs(r.right, n + 1))
        return dfs(root, 0)


if __name__ == "__main__":
    root = [3,9,20,None,None,15,7]

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

    test = Solution().maxDepth(r)
    print(test)
