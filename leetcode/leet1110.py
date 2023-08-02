import heapq
import math
from typing import List, Optional


# 1110. 删点成林
# 给出二叉树的根节点 root，树上每个节点都有一个不同的值。
#
# 如果节点值在 to_delete 中出现，我们就把该节点从树上删去，最后得到一个森林（一些不相交的树构成的集合）。
#
# 返回森林中的每棵树。你可以按任意顺序组织答案。
#
#
#
# 示例 1：
#
#
#
# 输入：root = [1,2,3,4,5,6,7], to_delete = [3,5]
# 输出：[[1,2,null,4],[6],[7]]
# 示例 2：
#
# 输入：root = [1,2,4,null,3], to_delete = [3]
# 输出：[[1,2,4]]
#

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def delNodes(self, root: Optional[TreeNode], to_delete: List[int]) -> List[TreeNode]:
        res = []
        ds = set(to_delete)
        queue = [root]

        while len(queue) > 0:
            node = queue[0]
            queue = queue[1:]

            if node.val in ds:
                if node.left is not None:
                    if node.left.val not in ds:
                        res.append(node.left)
                    queue.append(node.left)
                if node.right is not None:
                    if node.right.val not in ds:
                        res.append(node.right)
                    queue.append(node.right)
            else:
                if node.left is not None:
                    queue.append(node.left)
                if node.right is not None:
                    queue.append(node.right)
            if node.left is not None and node.left.val in ds:
                node.left = None
            if node.right is not None and node.right.val in ds:
                node.right = None
        if root.val not in ds:
            res.append(root)
        return res



if __name__ == "__main__":
    root = [1,2,3,4,5,6,7]
    to_delete = [1,2,3,4,5,6,7]
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

    test = Solution().delNodes(r, to_delete)
    print(test)
