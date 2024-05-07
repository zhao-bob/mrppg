# 2476. 二叉搜索树最近节点查询
# 中等
# 相关标签
# 相关企业
# 提示
# 给你一个 二叉搜索树 的根节点 root ，和一个由正整数组成、长度为 n 的数组 queries 。
#
# 请你找出一个长度为 n 的 二维 答案数组 answer ，其中 answer[i] = [mini, maxi] ：
#
# mini 是树中小于等于 queries[i] 的 最大值 。如果不存在这样的值，则使用 -1 代替。
# maxi 是树中大于等于 queries[i] 的 最小值 。如果不存在这样的值，则使用 -1 代替。
# 返回数组 answer 。
#
#
#
# 示例 1 ：
#
#
#
# 输入：root = [6,2,13,1,4,9,15,null,null,null,null,null,null,14], queries = [2,5,16]
# 输出：[[2,2],[4,6],[15,-1]]
# 解释：按下面的描述找出并返回查询的答案：
# - 树中小于等于 2 的最大值是 2 ，且大于等于 2 的最小值也是 2 。所以第一个查询的答案是 [2,2] 。
# - 树中小于等于 5 的最大值是 4 ，且大于等于 5 的最小值是 6 。所以第二个查询的答案是 [4,6] 。
# - 树中小于等于 16 的最大值是 15 ，且大于等于 16 的最小值不存在。所以第三个查询的答案是 [15,-1] 。
# 示例 2 ：
#
#
#
# 输入：root = [4,null,9], queries = [3]
# 输出：[[-1,4]]
# 解释：树中不存在小于等于 3 的最大值，且大于等于 3 的最小值是 4 。所以查询的答案是 [-1,4] 。
#
#
# 提示：
#
# 树中节点的数目在范围 [2, 105] 内
# 1 <= Node.val <= 106
# n == queries.length
# 1 <= n <= 105
# 1 <= queries[i] <= 106
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
    def closestNodes(self, root: Optional[TreeNode], queries: List[int]) -> List[List[int]]:
        l = []

        def mid(r):
            if r is None:
                return
            mid(r.left)
            l.append(r.val)
            mid(r.right)

        def search(n, right):
            left = 0

            while left <= right:
                mid = (left + right) // 2
                if l[mid] == n:
                    return [n, n]
                elif l[mid] < n:
                    left = mid + 1
                else:
                    right = mid - 1
            return [l[right], l[left]]

        mid(root)
        q = [(n, i) for i, n in enumerate(queries)]
        q.sort()
        res = [0] * len(queries)
        for i in range(len(queries)):
            if q[i][0] < l[0]:
                res[q[i][1]] = [-1, l[0]]
            elif q[i][0] > l[-1]:
                res[q[i][1]] = [l[-1], -1]
            else:
                if i == 0:
                    res[q[i][1]] = search(q[i][0], len(l))
                else:
                    pre = res[i - 1]
                    if q[i][0] < pre[1]:
                        res[q[i][1]] = pre
                    elif q[i][0] == pre[1]:
                        res[q[i][1]] = [pre[1], pre[1]]
                    else:
                        res[q[i][1]] = search(q[i][0], len(l))

        return res


if __name__ == "__main__":
    root = [6, 2, 13, 1, 4, 9, 15, None, None, None, None, None, None, 14]
    queries = [3]
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
    test = Solution().closestNodes(r, queries)
    print(test)
