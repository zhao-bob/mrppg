import heapq
import math
from collections import deque, Counter
from itertools import count
from typing import List, Optional


# 2385. 感染二叉树需要的总时间
# 中等
# 相关标签
# 相关企业
# 提示
# 给你一棵二叉树的根节点 root ，二叉树中节点的值 互不相同 。另给你一个整数 start 。在第 0 分钟，感染 将会从值为 start 的节点开始爆发。
#
# 每分钟，如果节点满足以下全部条件，就会被感染：
#
# 节点此前还没有感染。
# 节点与一个已感染节点相邻。
# 返回感染整棵树需要的分钟数。
#
#
#
# 示例 1：
#
#
# 输入：root = [1,5,3,null,4,10,6,9,2], start = 3
# 输出：4
# 解释：节点按以下过程被感染：
# - 第 0 分钟：节点 3
# - 第 1 分钟：节点 1、10、6
# - 第 2 分钟：节点5
# - 第 3 分钟：节点 4
# - 第 4 分钟：节点 9 和 2
# 感染整棵树需要 4 分钟，所以返回 4 。
# 示例 2：
#
#
# 输入：root = [1], start = 1
# 输出：0
# 解释：第 0 分钟，树中唯一一个节点处于感染状态，返回 0 。
#
#
# 提示：
#
# 树中节点的数目在范围 [1, 105] 内
# 1 <= Node.val <= 105
# 每个节点的值 互不相同
# 树中必定存在值为 start 的节点
#

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def amountOfTime(self, root: Optional[TreeNode], start: int) -> int:
        path = {}

        def find(r, k):
            if r is None:
                return False
            if r.val == start:
                path[r.val] = k
                return True
            if find(r.left, k + 1) or find(r.right, k + 1):
                path[r.val] = k
                return True
            else:
                return False

        def dfs(r, k):
            if r is None:
                return k
            if r.val in path:
                l = dfs(r.left, path[r.val])
                r = dfs(r.right, path[r.val])
            else:
                l = dfs(r.left, k + 1)
                r = dfs(r.right, k + 1)
            return max(l, r)

        find(root, 0)
        k = path[start]
        for p in path:
            path[p] = k - path[p]
        return dfs(root, 0)


if __name__ == "__main__":
    root = [1, 5, 3, None, 4, 10, 6, 9, 2]
    start = 3
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

    test = Solution().amountOfTime(r, start)
    print(test)
