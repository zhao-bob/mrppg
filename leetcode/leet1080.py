import math
from typing import List, Optional


# 1080. 根到叶路径上的不足节点
# 给你二叉树的根节点 root 和一个整数 limit ，请你同时删除树中所有 不足节点 ，并返回最终二叉树的根节点。
#
# 假如通过节点 node 的每种可能的 “根-叶” 路径上值的总和全都小于给定的 limit，则该节点被称之为 不足节点 ，需要被删除。
#
# 叶子节点，就是没有子节点的节点。
#
#
#
# 示例 1：
#
#
# 输入：root = [1,2,3,4,-99,-99,7,8,9,-99,-99,12,13,-99,14], limit = 1
# 输出：[1,2,3,4,None,None,7,8,9,None,14]
# 示例 2：
#
#
# 输入：root = [5,4,8,11,None,17,4,7,1,None,None,5,3], limit = 22
# 输出：[5,4,8,11,None,17,4,7,None,None,None,5]
# 示例 3：
#
#
# 输入：root = [1,2,-3,-5,None,4,None], limit = -1
# 输出：[1,None,-3,4]
#

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sufficientSubset(self, root: Optional[TreeNode], limit: int) -> Optional[TreeNode]:
        # val = []
        # stk = [[root, root.val]]
        # while len(stk) > 0:
        #     n = stk[0]
        #     stk = stk[1:]
        #     if n is not None:
        #         if n[0].left is not None:
        #             stk.append([n[0].left, n[1] + n[0].left.val])
        #         if n[0].right is not None:
        #             stk.append([n[0].right, n[1] + n[0].right.val])
        #         if n[0].left is None and n[0].right is None:
        #             val.append(n[1])
        il, mp = self.dfs(root, 0)
        if mp < limit:
            return None
        return root

    def dfs(self, node, val):
        if node is None:
            return True, val
        le, lmp = self.dfs(node.left, node.val + val)
        re, rmp = self.dfs(node.right, node.val + val)

        if le:
            mp = rmp
        elif re:
            mp = lmp
        else:
            mp = max(lmp, rmp)
            if lmp < limit:
                node.left = None
            if rmp < limit:
                node.right = None
        return False, mp

if __name__ == "__main__":
    root = [10,5,10]
    limit = 21
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

    test = Solution().sufficientSubset(r, limit)
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
