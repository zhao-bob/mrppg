import collections
import heapq
import math
from bisect import bisect_right
from collections import Counter, deque
from functools import cache
from itertools import product
from typing import List, Optional


# 449. Serialize and Deserialize BST
# 中等
# Serialization is converting a data structure or object into a sequence of bits so that it can be stored in a file or memory buffer, or transmitted across a network connection link to be reconstructed later in the same or another computer environment.
#
# Design an algorithm to serialize and deserialize a binary search tree. There is no restriction on how your serialization/deserialization algorithm should work. You need to ensure that a binary search tree can be serialized to a string, and this string can be deserialized to the original tree structure.
#
# The encoded string should be as compact as possible.
#
#
#
# Example 1:
#
# Input: root = [2,1,3]
# Output: [2,1,3]
# Example 2:
#
# Input: root = []
# Output: []

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Codec:

    def serialize(self, root: Optional[TreeNode]) -> str:
        """Encodes a tree to a single string.
        """
        res = ""
        stk = [root]
        while len(stk) > 0:
            n = stk[0]
            stk = stk[1:]
            if n is not None:
                res += (str(n.val) + ",")
                # if n.left is not None or n.right is not None:
                stk.append(n.left)
                stk.append(n.right)
            else:
                res += "n,"
        while res[-2:] == "n,":
            res = res[:-2]
        return res[0: -1]

    def deserialize(self, data: str) -> Optional[TreeNode]:
        """Decodes your encoded data to tree.
        """
        if data == "":
            return None
        root = data.split(",")
        if len(root) == 0 or root[0] == "n":
            return None

        r = TreeNode(int(root[0]))
        l = [r]
        i = 1
        while i < len(root) - len(root) % 2:
            p = l[0]
            if root[i] != "n":
                n = TreeNode(int(root[i]))
                p.left = n
                l.append(n)
            if i + 1 < len(root) and root[i + 1] != "n":
                n = TreeNode(int(root[i + 1]))
                p.right = n
                l.append(n)
            l = l[1:]
            i += 2
        return r


if __name__ == "__main__":
    root = []

    r = None
    if len(root) > 0:
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

    tree = Codec().serialize(r)
    ans = Codec().deserialize(tree)

    res = []
    stk = [ans]
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
