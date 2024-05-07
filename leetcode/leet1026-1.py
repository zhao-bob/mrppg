# 1026. 节点与其祖先之间的最大差值
# 已解答
# 中等
# 相关标签
# 相关企业
# 提示
# 给定二叉树的根节点 root，找出存在于 不同 节点 A 和 B 之间的最大值 V，其中 V = |A.val - B.val|，且 A 是 B 的祖先。
#
# （如果 A 的任何子节点之一为 B，或者 A 的任何子节点是 B 的祖先，那么我们认为 A 是 B 的祖先）
#
#
#
# 示例 1：
#
#
#
# 输入：root = [8,3,10,1,6,null,14,null,null,4,7,13]
# 输出：7
# 解释：
# 我们有大量的节点与其祖先的差值，其中一些如下：
# |8 - 3| = 5
# |3 - 7| = 4
# |8 - 1| = 7
# |10 - 13| = 3
# 在所有可能的差值中，最大值 7 由 |8 - 1| = 7 得出。
# 示例 2：
#
#
# 输入：root = [1,null,2,null,0,3]
# 输出：3
#
#
# 提示：
#
# 树中的节点数在 2 到 5000 之间。
# 0 <= Node.val <= 105
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
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        # res = 0
        #
        # def dfs(r, mn, mx):
        #     if r is None:
        #         return
        #     nonlocal res
        #     res = max(res, mx - mn)
        #     if r.left:
        #         nmx = mx
        #         nmn = mn
        #         if r.left.val > mx:
        #             nmx = r.left.val
        #         elif r.left.val < mn:
        #             nmn = r.left.val
        #         dfs(r.left, nmn, nmx)
        #     if r.right:
        #         nmx = mx
        #         nmn = mn
        #         if r.right.val > mx:
        #             nmx = r.right.val
        #         elif r.right.val < mn:
        #             nmn = r.right.val
        #         dfs(r.right, nmn, nmx)
        # dfs(root, root.val, root.val)
        # return res
        ans = 0

        def dfs(node: Optional[TreeNode], mn: int, mx: int) -> None:
            if node is None:
                nonlocal ans
                ans = max(ans, mx - mn)
                return
            mn = min(mn, node.val)
            mx = max(mx, node.val)
            dfs(node.left, mn, mx)
            dfs(node.right, mn, mx)

        dfs(root, root.val, root.val)
        return ans

if __name__ == "__main__":
    root = [8,3,10,1,6,None,14,None,None,4,7,13]

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

    test = Solution().maxAncestorDiff(r)
    print(test)
