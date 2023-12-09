import heapq
import math
from collections import Counter
from functools import cache
from typing import List, Optional
from sortedcontainers import SortedList


# 1457. 二叉树中的伪回文路径
# 提示
# 中等
# 79
# 相关企业
# 给你一棵二叉树，每个节点的值为 1 到 9 。我们称二叉树中的一条路径是 「伪回文」的，当它满足：路径经过的所有节点值的排列中，存在一个回文序列。
#
# 请你返回从根到叶子节点的所有路径中 伪回文 路径的数目。
#
#
#
# 示例 1：
#
#
#
# 输入：root = [2,3,1,3,1,null,1]
# 输出：2
# 解释：上图为给定的二叉树。总共有 3 条从根到叶子的路径：红色路径 [2,3,3] ，绿色路径 [2,1,1] 和路径 [2,3,1] 。
#      在这些路径中，只有红色和绿色的路径是伪回文路径，因为红色路径 [2,3,3] 存在回文排列 [3,2,3] ，绿色路径 [2,1,1] 存在回文排列 [1,2,1] 。
# 示例 2：
#
#
#
# 输入：root = [2,1,1,1,3,null,null,null,null,null,1]
# 输出：1
# 解释：上图为给定二叉树。总共有 3 条从根到叶子的路径：绿色路径 [2,1,1] ，路径 [2,1,3,1] 和路径 [2,1] 。
#      这些路径中只有绿色路径是伪回文路径，因为 [2,1,1] 存在回文排列 [1,2,1] 。
# 示例 3：
#
# 输入：root = [9]
# 输出：1
#


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def pseudoPalindromicPaths (self, root: Optional[TreeNode]) -> int:
        om = set()

        def dfs(node):
            if not node:
                return 0
            if not node.left and not node.right:
                if node.val in om:
                    if len(om) <= 2:
                        return 1
                else:
                    if len(om) == 0:
                        return 1
                return 0
            res = 0
            if node.val in om:
                om.discard(node.val)
            else:
                om.add(node.val)
            res = dfs(node.left) + dfs(node.right)
            if node.val in om:
                om.discard(node.val)
            else:
                om.add(node.val)
            return res

        return dfs(root)


if __name__ == "__main__":
    root = [9,9,9,9,9]
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
    test = Solution().pseudoPalindromicPaths(r)
    print(test)
