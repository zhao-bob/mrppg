# 987. 二叉树的垂序遍历
# 困难
# 相关标签
# 相关企业
# 给你二叉树的根结点 root ，请你设计算法计算二叉树的 垂序遍历 序列。
#
# 对位于 (row, col) 的每个结点而言，其左右子结点分别位于 (row + 1, col - 1) 和 (row + 1, col + 1) 。树的根结点位于 (0, 0) 。
#
# 二叉树的 垂序遍历 从最左边的列开始直到最右边的列结束，按列索引每一列上的所有结点，形成一个按出现位置从上到下排序的有序列表。如果同行同列上有多个结点，则按结点的值从小到大进行排序。
#
# 返回二叉树的 垂序遍历 序列。
#
#
#
# 示例 1：
#
#
# 输入：root = [3,9,20,null,null,15,7]
# 输出：[[9],[3,15],[20],[7]]
# 解释：
# 列 -1 ：只有结点 9 在此列中。
# 列  0 ：只有结点 3 和 15 在此列中，按从上到下顺序。
# 列  1 ：只有结点 20 在此列中。
# 列  2 ：只有结点 7 在此列中。
# 示例 2：
#
#
# 输入：root = [1,2,3,4,5,6,7]
# 输出：[[4],[2],[1,5,6],[3],[7]]
# 解释：
# 列 -2 ：只有结点 4 在此列中。
# 列 -1 ：只有结点 2 在此列中。
# 列  0 ：结点 1 、5 和 6 都在此列中。
#           1 在上面，所以它出现在前面。
#           5 和 6 位置都是 (2, 0) ，所以按值从小到大排序，5 在 6 的前面。
# 列  1 ：只有结点 3 在此列中。
# 列  2 ：只有结点 7 在此列中。
# 示例 3：
#
#
# 输入：root = [1,2,3,4,6,5,7]
# 输出：[[4],[2],[1,5,6],[3],[7]]
# 解释：
# 这个示例实际上与示例 2 完全相同，只是结点 5 和 6 在树中的位置发生了交换。
# 因为 5 和 6 的位置仍然相同，所以答案保持不变，仍然按值从小到大排序。
#
#
# 提示：
#
# 树中结点数目总数在范围 [1, 1000] 内
# 0 <= Node.val <= 1000
#

import heapq
import math
from collections import Counter, deque
from datetime import date
from functools import cache
from typing import List, Optional

from sortedcontainers import SortedList


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        l = {}

        q = [(root, 0, 0)]

        while q:
            nq = []
            for n in q:
                if n[2] in l:
                    l[n[2]].append((n[1], n[0].val))
                else:
                    l[n[2]] = [(n[1], n[0].val)]
                if n[0].left:
                    nq.append((n[0].left, n[1] + 1, n[2] - 1))
                if n[0].right:
                    nq.append((n[0].right, n[1] + 1, n[2] + 1))
            q = nq
        res = []
        for k in sorted(l):
            l[k].sort(key=lambda x: (x[0], x[1]))
            res.append([i[1] for i in l[k]])
        return res


if __name__ == "__main__":
    root = [3,9,20,None,None,15,7]
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
    test = Solution().verticalTraversal(r)
    print(test)
