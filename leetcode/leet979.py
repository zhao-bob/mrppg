import heapq
import math
from collections import Counter, deque
from functools import cache
from itertools import product
from typing import List, Optional

# 979. Distribute Coins in Binary Tree
# Medium
# 4.7K
# 153
# Companies
# You are given the root of a binary tree with n nodes where each node in the tree has node.val coins. There are n coins in total throughout the whole tree.
#
# In one move, we may choose two adjacent nodes and move one coin from one node to another. A move may be from parent to child, or from child to parent.
#
# Return the minimum number of moves required to make every node have exactly one coin.
#
#
#
# Example 1:
#
#
# Input: root = [3,0,0]
# Output: 2
# Explanation: From the root of the tree, we move one coin to its left child, and one coin to its right child.
# Example 2:
#
#
# Input: root = [0,3,0]
# Output: 3
# Explanation: From the left child of the root, we move two coins to the root [taking two moves]. Then, we move one coin from the root of the tree to the right child.

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    move = 0

    def distributeCoins(self, root: Optional[TreeNode]) -> int:
        def dfs(root):
            moveleft = 0
            moveright = 0
            if root is None:
                return 0
            if root.left is not None:
                moveleft = dfs(root.left)
            if root.right is not None:
                moveright = dfs(root.right)
            self.move += abs(moveleft) + abs(moveright)
            return moveleft + moveright + root.val - 1

        dfs(root)
        return self.move

if __name__ == "__main__":
    root = [3,0,0]
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

    test = Solution().distributeCoins(r)
    print(test)
