# 1379. 找出克隆二叉树中的相同节点
# 简单
# 相关标签
# 相关企业
# 给你两棵二叉树，原始树 original 和克隆树 cloned，以及一个位于原始树 original 中的目标节点 target。
#
# 其中，克隆树 cloned 是原始树 original 的一个 副本 。
#
# 请找出在树 cloned 中，与 target 相同 的节点，并返回对该节点的引用（在 C/C++ 等有指针的语言中返回 节点指针，其他语言返回节点本身）。
#
#
#
# 注意：你 不能 对两棵二叉树，以及 target 节点进行更改。只能 返回对克隆树 cloned 中已有的节点的引用。
#
#
#
# 示例 1:
#
#
#
# 输入: tree = [7,4,3,null,null,6,19], target = 3
# 输出: 3
# 解释: 上图画出了树 original 和 cloned。target 节点在树 original 中，用绿色标记。答案是树 cloned 中的黄颜色的节点（其他示例类似）。
# 示例 2:
#
#
#
# 输入: tree = [7], target =  7
# 输出: 7
# 示例 3:
#
#
#
# 输入: tree = [8,null,6,null,5,null,4,null,3,null,2,null,1], target = 4
# 输出: 4
#
#
# 提示：
#
# 树中节点的数量范围为 [1, 104] 。
# 同一棵树中，没有值相同的节点。
# target 节点是树 original 中的一个节点，并且不会是 null 。
#
#
# 进阶：如果树中允许出现值相同的节点，将如何解答？
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
    def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:
        # def dfs(r, t):
        #     if r is None:
        #         return None
        #     if r.val == t:
        #         return r
        #     l = dfs(r.left, t)
        #     r = dfs(r.right, t)
        #     if l:
        #         return l
        #     if r:
        #         return r
        #     else:
        #         return None
        q = deque()
        q1 = deque()
        q.append(original)
        q1.append(cloned)
        while q:
            n = q.popleft()
            n1 = q1.popleft()
            if n == target:
                return n1
            if n.left:
                q.append(n.left)
                q1.append(n1.left)
            if n.right:
                q.append(n.right)
                q1.append(n1.right)
        return None

    # def dfs(r, t):
    #     if r is None:
    #         return None
    #     if r.val == t:
    #         return r
    #     l = dfs(r.left, t)
    #     r = dfs(r.right, t)
    #     if l:
    #         return l
    #     if r:
    #         return r
    #     else:
    #         return None
    #
    # return dfs(cloned, target.val)


if __name__ == "__main__":
    tree = [7,4,3,None,None,6,19]
    target = 3
    r = TreeNode(tree[0])
    c = TreeNode(tree[0])
    l = [r]
    l1 = [c]
    i = 1
    while i < len(tree) - len(tree) % 2:
        p = l[0]
        if tree[i] is not None:
            n = TreeNode(tree[i])
            p.left = n
            l.append(n)
        if i + 1 < len(tree) and tree[i + 1] is not None:
            n = TreeNode(tree[i + 1])
            p.right = n
            l.append(n)
        l = l[1:]
        i += 2
    i = 1
    while i < len(tree) - len(tree) % 2:
        p = l1[0]
        if tree[i] is not None:
            n = TreeNode(tree[i])
            p.left = n
            l1.append(n)
        if i + 1 < len(tree) and tree[i + 1] is not None:
            n = TreeNode(tree[i + 1])
            p.right = n
            l1.append(n)
        l1 = l1[1:]
        i += 2
    test = Solution().getTargetCopy(r, c, TreeNode(target))
    print(test.val)
