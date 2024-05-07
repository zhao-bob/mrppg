# 889. 根据前序和后序遍历构造二叉树
# 中等
# 相关标签
# 相关企业
# 给定两个整数数组，preorder 和 postorder ，其中 preorder 是一个具有 无重复 值的二叉树的前序遍历，postorder 是同一棵树的后序遍历，重构并返回二叉树。
#
# 如果存在多个答案，您可以返回其中 任何 一个。
#
#
#
# 示例 1：
#
#
#
# 输入：preorder = [1,2,4,5,3,6,7], postorder = [4,5,2,6,7,3,1]
# 输出：[1,2,3,4,5,6,7]
# 示例 2:
#
# 输入: preorder = [1], postorder = [1]
# 输出: [1]
#
#
# 提示：
#
# 1 <= preorder.length <= 30
# 1 <= preorder[i] <= preorder.length
# preorder 中所有值都 不同
# postorder.length == preorder.length
# 1 <= postorder[i] <= postorder.length
# postorder 中所有值都 不同
# 保证 preorder 和 postorder 是同一棵二叉树的前序遍历和后序遍历
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
    def constructFromPrePost(self, preorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        n = len(preorder)
        res = TreeNode()
        pl = {}
        il = {}
        for i in range(n):
            pl[postorder[i]] = i
            il[preorder[i]] = i
        seen = set()

        def build(p, pre, post):
            if preorder[pre] in seen or postorder[post] in seen:
                return
            if preorder[pre] == postorder[post]:
                p.left = TreeNode(preorder[pre])
                seen.add(preorder[pre])
                if pre + 1 < n and post - 1 >= 0:
                    build(p.left, pre + 1, post - 1)
            else:
                p.left = TreeNode(preorder[pre])
                p.right = TreeNode(postorder[post])
                seen.add(preorder[pre])
                seen.add(postorder[post])
                prei = il[postorder[post]]
                posti = pl[preorder[pre]]
                if pre + 1 < n and posti - 1 >= 0:
                    build(p.left, pre + 1, posti - 1)
                if prei + 1 < n and post - 1 >= 0:
                    build(p.right, prei + 1, post - 1)

        build(res, 0, n - 1)
        return res.left


if __name__ == "__main__":
    preorder = [1, 2, 4, 5, 3, 6, 7]
    postorder = [4, 5, 2, 6, 7, 3, 1]
    test = Solution().constructFromPrePost(preorder, postorder)
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
