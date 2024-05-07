# 894. 所有可能的真二叉树
# 中等
# 相关标签
# 相关企业
# 给你一个整数 n ，请你找出所有可能含 n 个节点的 真二叉树 ，并以列表形式返回。答案中每棵树的每个节点都必须符合 Node.val == 0 。
#
# 答案的每个元素都是一棵真二叉树的根节点。你可以按 任意顺序 返回最终的真二叉树列表。
#
# 真二叉树 是一类二叉树，树中每个节点恰好有 0 或 2 个子节点。
#
#
#
# 示例 1：
#
#
# 输入：n = 7
# 输出：[[0,0,0,null,null,0,0,null,null,0,0],[0,0,0,null,null,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,null,null,null,null,0,0],[0,0,0,0,0,null,null,0,0]]
# 示例 2：
#
# 输入：n = 3
# 输出：[[0,0,0]]
#
#
# 提示：
#
# 1 <= n <= 20
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
    def allPossibleFBT(self, n: int) -> List[Optional[TreeNode]]:
        if n % 2 == 0:
            return []

        dp = [[] for _ in range(n + 1)]
        dp[1] = [TreeNode(0)]
        for i in range(3, n + 1, 2):
            for j in range(1, i, 2):
                for leftSubtree in dp[j]:
                    for rightSubtree in dp[i - 1 - j]:
                        root = TreeNode(0, leftSubtree, rightSubtree)
                        dp[i].append(root)
        return dp[n]



if __name__ == "__main__":
    n = 7
    test = Solution().allPossibleFBT(n)
    for t in test:
        res = []
        stk = [t]
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
