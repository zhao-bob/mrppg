import heapq
import math
from collections import Counter
from typing import List, Optional


# 1483. 树节点的第 K 个祖先
# 给你一棵树，树上有 n 个节点，按从 0 到 n-1 编号。树以父节点数组的形式给出，其中 parent[i] 是节点 i 的父节点。树的根节点是编号为 0 的节点。
#
# 树节点的第 k 个祖先节点是从该节点到根节点路径上的第 k 个节点。
#
# 实现 TreeAncestor 类：
#
# TreeAncestor（int n， int[] parent） 对树和父数组中的节点数初始化对象。
# getKthAncestor(int node, int k) 返回节点 node 的第 k 个祖先节点。如果不存在这样的祖先节点，返回 -1 。
#
#
# 示例 1：
#
#
#
# 输入：
# ["TreeAncestor","getKthAncestor","getKthAncestor","getKthAncestor"]
# [[7,[-1,0,0,1,1,2,2]],[3,1],[5,2],[6,3]]
#
# 输出：
# [null,1,0,-1]
#
# 解释：
# TreeAncestor treeAncestor = new TreeAncestor(7, [-1, 0, 0, 1, 1, 2, 2]);
#
# treeAncestor.getKthAncestor(3, 1);  // 返回 1 ，它是 3 的父节点
# treeAncestor.getKthAncestor(5, 2);  // 返回 0 ，它是 5 的祖父节点
# treeAncestor.getKthAncestor(6, 3);  // 返回 -1 因为不存在满足要求的祖先节点
#

class TreeAncestor:

    # def __init__(self, n: int, parent: List[int]):
    #     self.tree_list = [[] for _ in range(n)]
    #     neighbor = {}
    #
    #     for i in range(n):
    #         if parent[i] in neighbor:
    #             neighbor[parent[i]].add(i)
    #         else:
    #             neighbor[parent[i]] = {i}
    #     i = -1
    #     searched = set()
    #     while i < n:
    #         if i not in searched:
    #             tl = []
    #             if i != -1 and parent[i] != -1:
    #                 self.tree_list[i].extend(self.tree_list[parent[i]])
    #                 self.tree_list[i].append(parent[i])
    #                 tl = self.tree_list[i]
    #             if i in neighbor:
    #                 for x in neighbor[i]:
    #                     self.tree_list[x].extend(tl)
    #                     self.tree_list[x].append(i)
    #                     searched.add(x)
    #         i += 1
    #
    #
    # def getKthAncestor(self, node: int, k: int) -> int:
    #     l = self.tree_list[node]
    #     if k > len(l):
    #         return -1
    #     else:
    #         return l[len(l) - k]
    def __init__(self, n: int, parent: List[int]):
        self.log = 16
        self.ancestors = [[-1] * self.log for _ in range(n)]
        for i in range(n):
            self.ancestors[i][0] = parent[i]
        for j in range(1, self.log):
            for i in range(n):
                if self.ancestors[i][j - 1] != -1:
                    self.ancestors[i][j] = self.ancestors[self.ancestors[i][j - 1]][j - 1]

    def getKthAncestor(self, node: int, k: int) -> int:
        for j in range(self.log):
            if (k >> j) & 1:
                node = self.ancestors[node][j]
                if node == -1:
                    return -1
        return node



if __name__ == "__main__":
    c = [[5,[-1,0,0,0,3]],[1,5],[3,2],[0,1],[3,1],[3,5]]

    tree = TreeAncestor(c[0][0], c[0][1])

    for i in range(1, len(c)):
        test = tree.getKthAncestor(c[i][0], c[i][1])
        print(test)
