import heapq
import math
from collections import Counter, deque
from functools import cache
from itertools import product
from typing import List, Optional


# 2236. 判断根结点是否等于子结点之和
# 简单
# 42
# 相关企业
# 给你一个 二叉树 的根结点 root，该二叉树由恰好 3 个结点组成：根结点、左子结点和右子结点。
#
# 如果根结点值等于两个子结点值之和，返回 true ，否则返回 false 。
#
#
#
# 示例 1：
#
#
# 输入：root = [10,4,6]
# 输出：true
# 解释：根结点、左子结点和右子结点的值分别是 10 、4 和 6 。
# 由于 10 等于 4 + 6 ，因此返回 true 。
# 示例 2：
#
#
# 输入：root = [5,3,1]
# 输出：false
# 解释：根结点、左子结点和右子结点的值分别是 5 、3 和 1 。
# 由于 5 不等于 3 + 1 ，因此返回 false 。

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def checkTree(self, root: Optional[TreeNode]) -> bool:
        if root is None:
            return True
        if root.right is None and root.left is None:
            return False
        a = root.val
        if root.right and root.left is None:
            b = root.right.val
        elif root.left and root.right is None:
            b = root.left.val
        else:
            b = root.left.val + root.right.val
        return a == b

if __name__ == "__main__":
    root = [10,4,6]

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

    test = Solution().checkTree(r)

    print(test)
