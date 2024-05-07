# 106. 从中序与后序遍历序列构造二叉树
# 中等
# 相关标签
# 相关企业
# 给定两个整数数组 inorder 和 postorder ，其中 inorder 是二叉树的中序遍历， postorder 是同一棵树的后序遍历，请你构造并返回这颗 二叉树 。
#
#
#
# 示例 1:
#
#
# 输入：inorder = [9,3,15,20,7], postorder = [9,15,7,20,3]
# 输出：[3,9,20,null,null,15,7]
# 示例 2:
#
# 输入：inorder = [-1], postorder = [-1]
# 输出：[-1]
#
#
# 提示:
#
# 1 <= inorder.length <= 3000
# postorder.length == inorder.length
# -3000 <= inorder[i], postorder[i] <= 3000
# inorder 和 postorder 都由 不同 的值组成
# postorder 中每一个值都在 inorder 中
# inorder 保证是树的中序遍历
# postorder 保证是树的后序遍历
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
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        il = {}
        for i, n in enumerate(inorder):
            il[n] = i
        res = TreeNode(postorder[-1])
        i = len(postorder) - 2
        p = res
        stk = []
        while i >= 0:
            d = il[postorder[i]] - il[p.val]
            if d >= 1:
                stk.append(p)
                p.right = TreeNode(postorder[i])
                p = p.right
            elif d < 0:
                while stk and d < 0:
                    a = stk.pop()
                    d = il[postorder[i]] - il[a.val]
                    if d < 0:
                        p = a
                    else:
                        stk.append(a)
                        break
                p.left = TreeNode(postorder[i])
                p = p.left
            i -= 1
        return res


if __name__ == "__main__":
    inorder = [9,3,15,20,7]
    postorder = [9,15,7,20,3]
    test = Solution().buildTree(inorder, postorder)
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
