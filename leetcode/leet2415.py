import heapq
import math
from typing import List, Optional


# 2415. 反转二叉树的奇数层
# 提示
# 中等
# 36
# 相关企业
# 给你一棵 完美 二叉树的根节点 root ，请你反转这棵树中每个 奇数 层的节点值。
#
# 例如，假设第 3 层的节点值是 [2,1,3,4,7,11,29,18] ，那么反转后它应该变成 [18,29,11,7,4,3,1,2] 。
# 反转后，返回树的根节点。
#
# 完美 二叉树需满足：二叉树的所有父节点都有两个子节点，且所有叶子节点都在同一层。
#
# 节点的 层数 等于该节点到根节点之间的边数。
#
#
#
# 示例 1：
#
#
# 输入：root = [2,3,5,8,13,21,34]
# 输出：[2,5,3,8,13,21,34]
# 解释：
# 这棵树只有一个奇数层。
# 在第 1 层的节点分别是 3、5 ，反转后为 5、3 。
# 示例 2：
#
#
# 输入：root = [7,13,11]
# 输出：[7,11,13]
# 解释：
# 在第 1 层的节点分别是 13、11 ，反转后为 11、13 。
# 示例 3：
#
# 输入：root = [0,1,2,0,0,0,0,1,1,1,1,2,2,2,2]
# 输出：[0,2,1,0,0,0,0,2,2,2,2,1,1,1,1]
# 解释：奇数层由非零值组成。
# 在第 1 层的节点分别是 1、2 ，反转后为 2、1 。
# 在第 3 层的节点分别是 1、1、1、1、2、2、2、2 ，反转后为 2、2、2、2、1、1、1、1 。
#


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def reverseOddLevels(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # stk = []
        # l = 0
        # tl = []
        #
        # q = [(root, 0)]
        #
        # while q:
        #     n = q[0]
        #     q = q[1:]
        #     if n[1] == l + 1 and l % 2 == 0:
        #         for i in range(len(stk)):
        #             val = stk.pop()
        #             k = tl.pop(0)
        #             k.val = val
        #
        #     if n[0].left:
        #         if n[1] % 2 == 0:
        #             stk.append(n[0].left.val)
        #             tl.append(n[0].left)
        #         q.append((n[0].left, n[1] + 1))
        #     if n[0].right:
        #         if n[1] % 2 == 0:
        #             stk.append(n[0].right.val)
        #             tl.append(n[0].right)
        #         q.append((n[0].right, n[1] + 1))
        #     l = n[1]
        # return root

        def dfs(root1: Optional[TreeNode], root2: Optional[TreeNode], isOdd: bool) -> None:
            if root1 is None:
                return
            if isOdd:
                root1.val, root2.val = root2.val, root1.val
            dfs(root1.left, root2.right, not isOdd)
            dfs(root1.right, root2.left, not isOdd)

        dfs(root.left, root.right, True)
        return root


if __name__ == "__main__":
    root = [0,1,2,0,0,0,0,1,1,1,1,2,2,2,2]

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

    test = Solution().reverseOddLevels(r)
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
