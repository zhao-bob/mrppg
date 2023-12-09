from typing import List
from functools import cache


# 2477. 到达首都的最少油耗
# 提示
# 中等
# 66
# 相关企业
# 给你一棵 n 个节点的树（一个无向、连通、无环图），每个节点表示一个城市，编号从 0 到 n - 1 ，且恰好有 n - 1 条路。0 是首都。给你一个二维整数数组 roads ，其中 roads[i] = [ai, bi] ，表示城市 ai 和 bi 之间有一条 双向路 。
#
# 每个城市里有一个代表，他们都要去首都参加一个会议。
#
# 每座城市里有一辆车。给你一个整数 seats 表示每辆车里面座位的数目。
#
# 城市里的代表可以选择乘坐所在城市的车，或者乘坐其他城市的车。相邻城市之间一辆车的油耗是一升汽油。
#
# 请你返回到达首都最少需要多少升汽油。
#
#
#
# 示例 1：
#
#
#
# 输入：roads = [[0,1],[0,2],[0,3]], seats = 5
# 输出：3
# 解释：
# - 代表 1 直接到达首都，消耗 1 升汽油。
# - 代表 2 直接到达首都，消耗 1 升汽油。
# - 代表 3 直接到达首都，消耗 1 升汽油。
# 最少消耗 3 升汽油。
# 示例 2：
#
#
#
# 输入：roads = [[3,1],[3,2],[1,0],[0,4],[0,5],[4,6]], seats = 2
# 输出：7
# 解释：
# - 代表 2 到达城市 3 ，消耗 1 升汽油。
# - 代表 2 和代表 3 一起到达城市 1 ，消耗 1 升汽油。
# - 代表 2 和代表 3 一起到达首都，消耗 1 升汽油。
# - 代表 1 直接到达首都，消耗 1 升汽油。
# - 代表 5 直接到达首都，消耗 1 升汽油。
# - 代表 6 到达城市 4 ，消耗 1 升汽油。
# - 代表 4 和代表 6 一起到达首都，消耗 1 升汽油。
# 最少消耗 7 升汽油。
# 示例 3：
#
#
#
# 输入：roads = [], seats = 1
# 输出：0
# 解释：没有代表需要从别的城市到达首都。
#


class Solution:
    def minimumFuelCost(self, roads: List[List[int]], seats: int) -> int:
        adj = {}
        for r in roads:
            if r[0] in adj:
                adj[r[0]].add(r[1])
            else:
                adj[r[0]] = {r[1]}
            if r[1] in adj:
                adj[r[1]].add(r[0])
            else:
                adj[r[1]] = {r[0]}

        searched = {0}
        def dfs(n):
            searched.add(n)
            if n in adj:
                if len(adj[n]) == 1:
                    return 0, 1, 1
                car = 0
                num = 1
                pl = 0
                for i in adj[n]:
                    if i not in searched:
                        searched.add(i)
                        p, c, a = dfs(i)
                        car += c
                        num += a
                        pl += (p + c)
                car = num // seats if num % seats == 0 else num // seats + 1
                return pl, car, num

        if not adj or not adj[0]:
            return 0
        res = 0
        for i in adj[0]:
            p, c, num = dfs(i)
            res += (p + c)
        return res


if __name__ == "__main__":
    roads = [[3,1],[3,2],[1,0],[0,4],[0,5],[4,6]]
    seats = 2

    test = Solution().minimumFuelCost(roads, seats)
    print(test)
