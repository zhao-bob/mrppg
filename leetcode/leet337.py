import collections
import heapq
import math
from bisect import bisect_right
from collections import Counter, deque
from functools import cache
from itertools import product
from typing import List, Optional


# 337. 打家劫舍 III
# 中等
# 1.8K
# 相关企业
# 小偷又发现了一个新的可行窃的地区。这个地区只有一个入口，我们称之为 root 。
#
# 除了 root 之外，每栋房子有且只有一个“父“房子与之相连。一番侦察之后，聪明的小偷意识到“这个地方的所有房屋的排列类似于一棵二叉树”。 如果 两个直接相连的房子在同一天晚上被打劫 ，房屋将自动报警。
#
# 给定二叉树的 root 。返回 在不触动警报的情况下 ，小偷能够盗取的最高金额 。
#
#
#
# 示例 1:
#
#
#
# 输入: root = [3,2,3,null,3,null,1]
# 输出: 7
# 解释: 小偷一晚能够盗取的最高金额 3 + 3 + 1 = 7
# 示例 2:
#
#
#
# 输入: root = [3,4,5,1,3,null,1]
# 输出: 9
# 解释: 小偷一晚能够盗取的最高金额 4 + 5 = 9

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        def dfs(node):
            if node is None:
                return [0, 0]
            l = dfs(node.left)
            r = dfs(node.right)

            s = node.val + l[1] + r[1]
            ns = max(l) + max(r)
            return [s, ns]
        return max(dfs(root))


if __name__ == "__main__":
    root = [3,4,5,1,3,None,1]

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

    test = Solution().rob(r)

    print(test)
