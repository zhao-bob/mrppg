# 98. 验证二叉搜索树
# 中等
# 相关标签
# 相关企业
# 给你一个二叉树的根节点 root ，判断其是否是一个有效的二叉搜索树。
#
# 有效 二叉搜索树定义如下：
#
# 节点的左
# 子树
# 只包含 小于 当前节点的数。
# 节点的右子树只包含 大于 当前节点的数。
# 所有左子树和右子树自身必须也是二叉搜索树。
#
#
# 示例 1：
#
#
# 输入：root = [2,1,3]
# 输出：true
# 示例 2：
#
#
# 输入：root = [5,1,4,null,null,3,6]
# 输出：false
# 解释：根节点的值是 5 ，但是右子节点的值是 4 。
#
#
# 提示：
#
# 树中节点数目范围在[1, 104] 内
# -231 <= Node.val <= 231 - 1
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
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def dfs(r, mn, mx):
            if r is None:
                return True
            if mn < r.val < mx:
                return dfs(r.left, mn, r.val) and dfs(r.right, r.val, mx)
            else:
                return False
        return dfs(root, -math.inf, math.inf)


if __name__ == "__main__":
    root = [3,None,30,10,None,None,15,None,45]

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

    test = Solution().isValidBST(r)
    print(test)
