from typing import List
from functools import cache


# 1038. 从二叉搜索树到更大和树
# 提示
# 中等
# 236
# 相关企业
# 给定一个二叉搜索树 root (BST)，请将它的每个节点的值替换成树中大于或者等于该节点值的所有节点值之和。
#
# 提醒一下， 二叉搜索树 满足下列约束条件：
#
# 节点的左子树仅包含键 小于 节点键的节点。
# 节点的右子树仅包含键 大于 节点键的节点。
# 左右子树也必须是二叉搜索树。
#
#
# 示例 1：
#
#
#
# 输入：[4,1,6,0,2,5,7,None,None,None,3,None,None,None,8]
# 输出：[30,36,21,36,35,26,15,None,None,None,33,None,None,None,8]
# 示例 2：
#
# 输入：root = [0,None,1]
# 输出：[1,None,1]
#


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def bstToGst(self, root: TreeNode) -> TreeNode:
        def dfs(node, s):
            if not node:
                return 0
            a = node.val
            if node.right:
                a += dfs(node.right, s)
            left = 0
            if node.left:
                left = dfs(node.left, a + s)
            node.val = a + s
            return a + left
        dfs(root, 0)
        return root



if __name__ == "__main__":
    root = [0]
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

    test = Solution().bstToGst(r)
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
