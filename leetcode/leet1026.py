import math
from bisect import bisect_right, bisect_left
from collections import defaultdict
from functools import lru_cache
from random import randint
from typing import List, Optional


# 1026. 节点与其祖先之间的最大差值
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
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        nl = []
        diff = 0
        nl.append([root, root.val, root.val])

        while len(nl) > 0:
            n = nl[0]
            if n[0].left is not None:
                a = min(n[1], n[0].left.val)
                b = max(n[2], n[0].left.val)
                diff = max(diff, b - a)
                nl.append([n[0].left, a, b])
            if n[0].right is not None:
                a = min(n[1], n[0].right.val)
                b = max(n[2], n[0].right.val)
                diff = max(diff, b - a)
                nl.append([n[0].right, a, b])
            nl = nl[1:]
        return diff


if __name__ == "__main__":
    root = [1,None,2,None,0,3]

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
