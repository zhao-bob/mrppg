import collections
import heapq
import math
from bisect import bisect_right
from collections import Counter, deque
from functools import cache
from itertools import product
from typing import List, Optional


# 1448. 统计二叉树中好节点的数目
# 中等
# 给你一棵根为 root 的二叉树，请你返回二叉树中好节点的数目。
#
# 「好节点」X 定义为：从根到该节点 X 所经过的节点中，没有任何节点的值大于 X 的值。
#
#
#
# 示例 1：
#
#
#
# 输入：root = [3,1,4,3,null,1,5]
# 输出：4
# 解释：图中蓝色节点为好节点。
# 根节点 (3) 永远是个好节点。
# 节点 4 -> (3,4) 是路径中的最大值。
# 节点 5 -> (3,4,5) 是路径中的最大值。
# 节点 3 -> (3,1,3) 是路径中的最大值。
# 示例 2：
#
#
#
# 输入：root = [3,3,null,4,2]
# 输出：3
# 解释：节点 2 -> (3, 3, 2) 不是好节点，因为 "3" 比它大。
# 示例 3：
#
# 输入：root = [1]
# 输出：1
# 解释：根节点是好节点。

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def dfs(r, mv):
            res = 0
            if r:
                if r.val >= mv:
                    res += 1
                    mv = r.val
                if r.left:
                    res += dfs(r.left, max(r.left.val, mv))
                if r.right:
                    res += dfs(r.right, max(r.right.val, mv))
            return res

        return dfs(root, -math.inf)




if __name__ == "__main__":
    root = [3,1,4,2,3,1,5]

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

    test = Solution().goodNodes(r)

    print(test)
