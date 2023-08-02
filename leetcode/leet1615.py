import math
from typing import List


# 1615. 最大网络秩

# n 座城市和一些连接这些城市的道路 roads 共同组成一个基础设施网络。每个 roads[i] = [ai, bi] 都表示在城市 ai 和 bi 之间有一条双向道路。
#
# 两座不同城市构成的 城市对 的 网络秩 定义为：与这两座城市 直接 相连的道路总数。如果存在一条道路直接连接这两座城市，则这条道路只计算 一次 。
#
# 整个基础设施网络的 最大网络秩 是所有不同城市对中的 最大网络秩 。
#
# 给你整数 n 和数组 roads，返回整个基础设施网络的 最大网络秩 。
#
#  
#
# 示例 1：
#
#
#
# 输入：n = 4, roads = [[0,1],[0,3],[1,2],[1,3]]
# 输出：4
# 解释：城市 0 和 1 的网络秩是 4，因为共有 4 条道路与城市 0 或 1 相连。位于 0 和 1 之间的道路只计算一次。
# 示例 2：
#
#
#
# 输入：n = 5, roads = [[0,1],[0,3],[1,2],[1,3],[2,3],[2,4]]
# 输出：5
# 解释：共有 5 条道路与城市 1 或 2 相连。
# 示例 3：
#
# 输入：n = 8, roads = [[0,1],[1,2],[2,3],[2,4],[5,6],[5,7]]
# 输出：5
# 解释：2 和 5 的网络秩为 5，注意并非所有的城市都需要连接起来。
#

class Solution:
    def maximalNetworkRank(self, n: int, roads: List[List[int]]) -> int:
        deg = [0] * n
        adj = [set() for _ in range(n)]
        for r in roads:
            deg[r[0]] += 1
            deg[r[1]] += 1
            adj[r[0]].add(r[1])
            adj[r[1]].add(r[0])

        aset = set()
        bset = set()
        a = 0
        b = 0
        for i in range(2):
            md = max(deg)
            if md > 0:
                while md in deg:
                    if i == 0:
                        a = md
                        aset.add(deg.index(md))
                    else:
                        b = md
                        bset.add(deg.index(md))
                    deg[deg.index(md)] = 0
        res = 0
        if len(aset) > 1:
            for x in aset:
                neighbor = adj[x]
                remain = aset.difference({x})
                if len(remain.difference(neighbor)) > 0:
                    res = 2 * a
                    break
            else:
                res = 2 * a - 1
        elif len(aset) == 1:
            neighbor = adj[aset.pop()]
            if len(bset.difference(neighbor)) > 0:
                res = a + b
            else:
                res = a + b - 1

        return res


if __name__ == "__main__":
    n = 5
    roads = [[2, 3], [0, 3], [0, 4], [4, 1]]

    test = Solution().maximalNetworkRank(n, roads)
    print(test)
