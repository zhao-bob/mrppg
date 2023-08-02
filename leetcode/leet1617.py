from typing import List


# 1617. 统计子树中城市之间最大距离

# 给你 n 个城市，编号为从 1 到 n 。同时给你一个大小为 n-1 的数组 edges ，其中 edges[i] = [ui, vi] 表示城市 ui 和 vi 之间有一条双向边。题目保证任意城市之间只有唯一的一条路径。换句话说，所有城市形成了一棵 树 。
#
# 一棵 子树 是城市的一个子集，且子集中任意城市之间可以通过子集中的其他城市和边到达。两个子树被认为不一样的条件是至少有一个城市在其中一棵子树中存在，但在另一棵子树中不存在。
#
# 对于 d 从 1 到 n-1 ，请你找到城市间 最大距离 恰好为 d 的所有子树数目。
#
# 请你返回一个大小为 n-1 的数组，其中第 d 个元素（下标从 1 开始）是城市间 最大距离 恰好等于 d 的子树数目。
#
# 请注意，两个城市间距离定义为它们之间需要经过的边的数目。
#
#  
#
# 示例 1：
#
#
#
# 输入：n = 4, edges = [[1,2],[2,3],[2,4]]
# 输出：[3,4,0]
# 解释：
# 子树 {1,2}, {2,3} 和 {2,4} 最大距离都是 1 。
# 子树 {1,2,3}, {1,2,4}, {2,3,4} 和 {1,2,3,4} 最大距离都为 2 。
# 不存在城市间最大距离为 3 的子树。
# 示例 2：
#
# 输入：n = 2, edges = [[1,2]]
# 输出：[1]
# 示例 3：
#
# 输入：n = 3, edges = [[1,2],[2,3]]
# 输出：[2,1]
#

class Solution:
    def countSubgraphsForEachDiameter(self, n: int, edges: List[List[int]]) -> List[int]:
        res = [0] * (n - 1)
        adj = [[] for _ in range(n)]
        for i in range(len(edges)):
            adj[edges[i][0] - 1].append(edges[i][1] - 1)
            adj[edges[i][1] - 1].append(edges[i][0] - 1)

        def dfs(root, mask, diameter):
            first = 0
            second = 0

            mask &= ~(1 << root)
            for x in adj[root]:
                if mask & (1 << x):
                    mask &= ~(1 << x)
                    res = dfs(x, mask, diameter)
                    distance = 1 + res[0]
                    diameter = res[1]
                    mask = res[2]
                    if distance > first:
                        second = first
                        first = distance
                    elif distance > second:
                        second = distance
            diameter = max(second + first, diameter)
            return [first, diameter, mask]

        for mask in range(1, 1 << n):
            if mask & (mask - 1) == 0:
                continue
            root = mask.bit_length() - 1
            [f, d, m] = dfs(root, mask, 0)
            if m == 0 and d > 0:
                res[d - 1] += 1
        return res


if __name__ == "__main__":
    n = 7
    edges = [[1,4],[1,3],[2,5],[2,6],[3,6],[6,7]]
    test = Solution().countSubgraphsForEachDiameter(n, edges)
    print(test)
