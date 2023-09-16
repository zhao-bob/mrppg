import collections
import heapq
import math
from bisect import bisect_right
from collections import Counter, deque
from functools import cache
from itertools import product
from typing import List, Optional


# 1123. 最深叶节点的最近公共祖先
# 中等
# 给你一个有根节点 root 的二叉树，返回它 最深的叶节点的最近公共祖先 。
#
# 回想一下：
#
# 叶节点 是二叉树中没有子节点的节点
# 树的根节点的 深度 为 0，如果某一节点的深度为 d，那它的子节点的深度就是 d+1
# 如果我们假定 A 是一组节点 S 的 最近公共祖先，S 中的每个节点都在以 A 为根节点的子树中，且 A 的深度达到此条件下可能的最大值。
#
#
# 示例 1：
#
#
# 输入：root = [3,5,1,6,2,0,8,null,null,7,4]
# 输出：[2,7,4]
# 解释：我们返回值为 2 的节点，在图中用黄色标记。
# 在图中用蓝色标记的是树的最深的节点。
# 注意，节点 6、0 和 8 也是叶节点，但是它们的深度是 2 ，而节点 7 和 4 的深度是 3 。
# 示例 2：
#
# 输入：root = [1]
# 输出：[1]
# 解释：根节点是树中最深的节点，它是它本身的最近公共祖先。
# 示例 3：
#
# 输入：root = [0,1,3,null,2]
# 输出：[2]
# 解释：树中最深的叶节点是 2 ，最近公共祖先是它自己。

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def lcaDeepestLeaves(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def dfs(r, n):
            if r.left is None and r.right is None:
                r.height = n
                return
            if r.left:
                dfs(r.left, n + 1)
            if r.right:
                dfs(r.right, n + 1)
            left = 0
            right = 0
            if r.left:
                left = r.left.height
            if r.right:
                right = r.right.height
            r.height = max(left, right)
        dfs(root, 0)

        q = [root]
        while len(q) > 0:
            n = q[0]
            q = q[1:]
            l = 0
            r = 0
            if n.left:
                l = n.left.height
            if n.right:
                r = n.right.height
            if l == r:
                return n
            if l > r:
                q.append(n.left)
            if r > l:
                q.append(n.right)


if __name__ == "__main__":
    root = [0,1,3,None,2]

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

    test = Solution().lcaDeepestLeaves(r)

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
