# 2583. 二叉树中的第 K 大层和
# 中等
# 相关标签
# 相关企业
# 提示
# 给你一棵二叉树的根节点 root 和一个正整数 k 。
#
# 树中的 层和 是指 同一层 上节点值的总和。
#
# 返回树中第 k 大的层和（不一定不同）。如果树少于 k 层，则返回 -1 。
#
# 注意，如果两个节点与根节点的距离相同，则认为它们在同一层。
#
#
#
# 示例 1：
#
#
#
# 输入：root = [5,8,9,2,1,3,7,4,6], k = 2
# 输出：13
# 解释：树中每一层的层和分别是：
# - Level 1: 5
# - Level 2: 8 + 9 = 17
# - Level 3: 2 + 1 + 3 + 7 = 13
# - Level 4: 4 + 6 = 10
# 第 2 大的层和等于 13 。
# 示例 2：
#
#
#
# 输入：root = [1,2,null,3], k = 1
# 输出：3
# 解释：最大的层和是 3 。
#
#
# 提示：
#
# 树中的节点数为 n
# 2 <= n <= 105
# 1 <= Node.val <= 106
# 1 <= k <= n
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
    def kthLargestLevelSum(self, root: Optional[TreeNode], k: int) -> int:
        q = [root]

        sq = []
        while q:
            nq = []
            s = 0
            for n in q:
                s += n.val
                if n.left:
                    nq.append(n.left)
                if n.right:
                    nq.append(n.right)
            if len(sq) < k:
                heapq.heappush(sq, s)
            else:
                heapq.heappushpop(sq, s)
            q = nq
        if len(sq) < k:
            return -1
        else:
            return heapq.heappop(sq)


if __name__ == "__main__":
    root = [1,2,None,3]
    k = 1
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
    test = Solution().kthLargestLevelSum(r, k)
    print(test)
