# 590. N 叉树的后序遍历
# 简单
# 相关标签
# 相关企业
# 给定一个 n 叉树的根节点 root ，返回 其节点值的 后序遍历 。
#
# n 叉树 在输入中按层序遍历进行序列化表示，每组子节点由空值 null 分隔（请参见示例）。
#
#
#
# 示例 1：
#
#
#
# 输入：root = [1,null,3,2,4,null,5,6]
# 输出：[5,6,3,2,4,1]
# 示例 2：
#
#
#
# 输入：root = [1,null,2,3,4,5,null,null,6,7,null,8,null,9,10,null,null,11,null,12,null,13,null,null,14]
# 输出：[2,6,14,11,7,3,12,8,4,13,9,10,5,1]
#
#
# 提示：
#
# 节点总数在范围 [0, 104] 内
# 0 <= Node.val <= 104
# n 叉树的高度小于或等于 1000
#

import heapq
import math
from collections import Counter, deque, defaultdict
from datetime import date
from functools import cache
from typing import List, Optional

from sortedcontainers import SortedList


# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children


class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        res = []

        def post(root):
            if not root:
                return
            if root.children:
                for c in root.children:
                    post(c)
            res.append(root.val)

        post(root)
        return res
        # if root is None:
        #     return []
        # ans = []
        # st = []
        # nextIndex = defaultdict(int)
        # node = root
        # while st or node:
        #     while node:
        #         ans.append(node.val)
        #         st.append(node)
        #         if not node.children:
        #             break
        #         nextIndex[node] = 1
        #         node = node.children[0]
        #     node = st[-1]
        #     i = nextIndex[node]
        #     if node.children and i < len(node.children):
        #         nextIndex[node] = i + 1
        #         node = node.children[i]
        #     else:
        #         st.pop()
        #         del nextIndex[node]
        #         node = None
        # return ans


if __name__ == "__main__":
    root = [1,None,3,2,4,None,5,6]
    r = Node(root[0])
    p = [r]
    i = 1
    while i < len(root):
        np = []
        for n in p:
            if i < len(root) and root[i] is None:
                j = i + 1
                if root[j] is not None:
                    n.children = []
                    while j < len(root) and root[j] is not None:
                        n.children.append(Node(root[j]))
                        j += 1
                np.extend(n.children)
                p = np
                i = j
    test = Solution().postorder(r)
    print(test)
