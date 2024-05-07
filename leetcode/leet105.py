# 105. 从前序与中序遍历序列构造二叉树
# 中等
# 相关标签
# 相关企业
# 给定两个整数数组 preorder 和 inorder ，其中 preorder 是二叉树的先序遍历， inorder 是同一棵树的中序遍历，请构造二叉树并返回其根节点。
#
#
#
# 示例 1:
#
#
# 输入: preorder = [3,9,20,15,7], inorder = [9,3,15,20,7]
# 输出: [3,9,20,null,null,15,7]
# 示例 2:
#
# 输入: preorder = [-1], inorder = [-1]
# 输出: [-1]
#
#
# 提示:
#
# 1 <= preorder.length <= 3000
# inorder.length == preorder.length
# -3000 <= preorder[i], inorder[i] <= 3000
# preorder 和 inorder 均 无重复 元素
# inorder 均出现在 preorder
# preorder 保证 为二叉树的前序遍历序列
# inorder 保证 为二叉树的中序遍历序列
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
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        il = {}
        for i, n in enumerate(inorder):
            il[n] = i
        res = TreeNode(preorder[0])
        i = 1
        p = res
        stk = []
        while i < len(preorder):
            d = il[p.val] - il[preorder[i]]
            if d >= 1:
                stk.append(p)
                p.left = TreeNode(preorder[i])
                p = p.left
            elif d < 0:
                while stk and d < 0:
                    a = stk.pop()
                    d = il[a.val] - il[preorder[i]]
                    if d < 0:
                        p = a
                    else:
                        stk.append(a)
                        break
                p.right = TreeNode(preorder[i])
                p = p.right
            i += 1
        return res


if __name__ == "__main__":
    preorder = [4,1,3,2]
    inorder = [1,2,3,4]
    test = Solution().buildTree(preorder, inorder)
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
