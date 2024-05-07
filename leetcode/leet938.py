# 938. 二叉搜索树的范围和
# 简单
# 相关标签
# 相关企业
# 给定二叉搜索树的根结点 root，返回值位于范围 [low, high] 之间的所有结点的值的和。
#
#
#
# 示例 1：
#
#
# 输入：root = [10,5,15,3,7,null,18], low = 7, high = 15
# 输出：32
# 示例 2：
#
#
# 输入：root = [10,5,15,3,7,13,18,1,null,6], low = 6, high = 10
# 输出：23
#
#
# 提示：
#
# 树中节点数目在范围 [1, 2 * 104] 内
# 1 <= Node.val <= 105
# 1 <= low <= high <= 105
# 所有 Node.val 互不相同
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
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        res = 0

        def search(r, low, high):
            nonlocal res
            if r is None:
                return
            if low <= r.val <= high:
                res += r.val
                if r.val > low:
                    search(r.left, low, r.val)
                if r.val < high:
                    search(r.right, r.val, high)
            elif r.val < low:
                search(r.right, low, high)
            elif r.val > high:
                search(r.left, low, high)

        search(root, low, high)
        return res


if __name__ == "__main__":
    root = [10, 5, 15, 3, 7, None, 18]
    low = 6
    high = 10
    r = TreeNode(root[0])
    l = [r]
    i = 1
    while i < len(root) - len(root) % 2:
        x = l[0]
        if root[i] is not None:
            n = TreeNode(root[i])
            x.left = n
            l.append(n)
        if i + 1 < len(root) and root[i + 1] is not None:
            n = TreeNode(root[i + 1])
            x.right = n
            l.append(n)
        l = l[1:]
        i += 2
    test = Solution().rangeSumBST(r, low, high)
    print(test)
