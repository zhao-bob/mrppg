import heapq
import math
from collections import Counter, deque
from functools import cache
from itertools import product
from typing import List, Optional


# 617. 合并二叉树
# 简单
# 1.3K
# 相关企业
# 给你两棵二叉树： root1 和 root2 。
#
# 想象一下，当你将其中一棵覆盖到另一棵之上时，两棵树上的一些节点将会重叠（而另一些不会）。你需要将这两棵树合并成一棵新二叉树。合并的规则是：如果两个节点重叠，那么将这两个节点的值相加作为合并后节点的新值；否则，不为 None 的节点将直接作为新二叉树的节点。
#
# 返回合并后的二叉树。
#
# 注意: 合并过程必须从两个树的根节点开始。
#
#
#
# 示例 1：
#
#
# 输入：root1 = [1,3,2,5], root2 = [2,1,3,None,4,None,7]
# 输出：[3,4,5,5,4,None,7]
# 示例 2：
#
# 输入：root1 = [1], root2 = [1,2]
# 输出：[2,2]

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        # if root1 is None:
        #     return root2
        # if root2 is None:
        #     return root1
        #
        # res = TreeNode(root1.val + root2.val)
        # q1 = [root1]
        # q2 = [root2]
        # q3 = [res]
        # while len(q1) > 0 and len(q2) > 0:
        #     n1 = q1[0]
        #     q1 = q1[1:]
        #     n2 = q2[0]
        #     q2 = q2[1:]
        #     n3 = q3[0]
        #     q3 = q3[1:]
        #     if n1 or n2:
        #         a = math.inf
        #         b = math.inf
        #         if n1 and n1.left:
        #             a = n1.left.val
        #         if n2 and n2.left:
        #             b = n2.left.val
        #         if a == math.inf and b != math.inf:
        #             n3.left = TreeNode(b)
        #         elif a != math.inf and b == math.inf:
        #             n3.left = TreeNode(a)
        #         elif a != math.inf and a != math.inf:
        #             n3.left = TreeNode(a + b)
        #         if n3:
        #             q3.append(n3.left)
        #         a = math.inf
        #         b = math.inf
        #         if n1 and n1.right:
        #             a = n1.right.val
        #         if n2 and n2.right:
        #             b = n2.right.val
        #         if a == math.inf and b != math.inf:
        #             n3.right = TreeNode(b)
        #         elif a != math.inf and b == math.inf:
        #             n3.right = TreeNode(a)
        #         elif a != math.inf and a != math.inf:
        #             n3.right = TreeNode(a + b)
        #         if n3:
        #             q3.append(n3.right)
        #     if n1 is not None:
        #         q1.append(n1.left)
        #         q1.append(n1.right)
        #     if n2 is not None:
        #         q2.append(n2.left)
        #         q2.append(n2.right)
        # while len(q1) > 0:
        #     n1 = q1[0]
        #     q1 = q1[1:]
        #     n3 = q3[0]
        #     q3 = q3[1:]
        #     if n1 and n1.left:
        #         n3.left = TreeNode(n1.val)
        #         q1.append(n1.left)
        #         q3.append(n3.left)
        #     if n1 and n1.right:
        #         n3.right = TreeNode(n1.val)
        #         q1.append(n1.right)
        #         q3.append(n3.right)
        # while len(q2) > 0:
        #     n2 = q2[0]
        #     q2 = q2[1:]
        #     n3 = q3[0]
        #     q3 = q3[1:]
        #     if n2 and n2.left:
        #         n3.left = TreeNode(n2.val)
        #         q1.append(n2.left)
        #         q3.append(n3.left)
        #     if n2 and n2.right:
        #         n3.right = TreeNode(n2.val)
        #         q1.append(n2.right)
        #         q3.append(n3.right)
        #
        # return res

        def merge(r1, r2):
            if r1 is None:
                return r2
            if r2 is None:
                return r1
            r1.val = r1.val + r2.val
            r1.left = merge(r1.left, r2.left)
            r1.right = merge(r1.right, r2.right)
            return r1
        return merge(root1, root2)


if __name__ == "__main__":
    root1 = [1,None,1,None,1,2]
    root2 = [1,None,1,2]

    r1 = TreeNode(root1[0])
    l = [r1]
    i = 1
    while i < len(root1) - len(root1) % 2:
        p = l[0]
        if root1[i] is not None:
            n = TreeNode(root1[i])
            p.left = n
            l.append(n)
        if i + 1 < len(root1) and root1[i + 1] is not None:
            n = TreeNode(root1[i + 1])
            p.right = n
            l.append(n)
        l = l[1:]
        i += 2
    r2 = TreeNode(root2[0])
    l = [r2]
    i = 1
    while i < len(root2) - len(root2) % 2:
        p = l[0]
        if root2[i] is not None:
            n = TreeNode(root2[i])
            p.left = n
            l.append(n)
        if i + 1 < len(root2) and root2[i + 1] is not None:
            n = TreeNode(root2[i + 1])
            p.right = n
            l.append(n)
        l = l[1:]
        i += 2

    test = Solution().mergeTrees(r1, r2)

    res = []
    stk = [test]
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
