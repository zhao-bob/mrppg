# 429. N 叉树的层序遍历
# 中等
# 相关标签
# 相关企业
# 给定一个 N 叉树，返回其节点值的层序遍历。（即从左到右，逐层遍历）。
#
# 树的序列化输入是用层序遍历，每组子节点都由 null 值分隔（参见示例）。
#
#
#
# 示例 1：
#
#
#
# 输入：root = [1,null,3,2,4,null,5,6]
# 输出：[[1],[3,2,4],[5,6]]
# 示例 2：
#
#
#
# 输入：root = [1,null,2,3,4,5,null,null,6,7,null,8,null,9,10,null,null,11,null,12,null,13,null,null,14]
# 输出：[[1],[2,3,4,5],[6,7,8,9,10],[11,12,13],[14]]
#
#
# 提示：
#
# 树的高度不会超过 1000
# 树的节点总数在 [0, 10^4] 之间
#

import heapq
import math
from collections import Counter, deque
from datetime import date
from functools import cache
from typing import List, Optional

from sortedcontainers import SortedList


# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children


class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        res = []
        if root is None:
            return res
        q = [(root, 0)]
        pre = -1
        l = []
        start = True
        while q:
            n = q[0]
            q = q[1:]
            if n[1] != pre:
                if l:
                    res.append(l)
                l = [n[0].val]
                start = not start
            else:
                l.append(n[0].val)
                if start:
                    start = False
            pre = n[1]
            if n[0].children:
                for c in n[0].children:
                    q.append((c, n[1] + 1))
        if l:
            res.append(l)
        return res


if __name__ == "__main__":
    root = [3,None,1,None,5]
    r = Node(root[0])
    p = [r]
    i = 1
    while i < len(root):
        np = []
        for n in p:
            if i < len(root) and root[i] is None:
                j = i + 1
                if root[j] is not None:
                    n.children = []
                    while j < len(root) and root[j] is not None:
                        n.children.append(Node(root[j]))
                        j += 1
                np.extend(n.children)
                p = np
                i = j
    test = Solution().levelOrder(r)
    print(test)
