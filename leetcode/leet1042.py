import math
from functools import lru_cache
from typing import List, Optional


# 1042. 不邻接植花
# 有 n 个花园，按从 1 到 n 标记。另有数组 paths ，其中 paths[i] = [xi, yi] 描述了花园 xi 到花园 yi 的双向路径。在每个花园中，你打算种下四种花之一。
#
# 另外，所有花园 最多 有 3 条路径可以进入或离开.
#
# 你需要为每个花园选择一种花，使得通过路径相连的任何两个花园中的花的种类互不相同。
#
# 以数组形式返回 任一 可行的方案作为答案 answer，其中 answer[i] 为在第 (i+1) 个花园中种植的花的种类。花的种类用  1、2、3、4 表示。保证存在答案。
#
#
#
# 示例 1：
#
# 输入：n = 3, paths = [[1,2],[2,3],[3,1]]
# 输出：[1,2,3]
# 解释：
# 花园 1 和 2 花的种类不同。
# 花园 2 和 3 花的种类不同。
# 花园 3 和 1 花的种类不同。
# 因此，[1,2,3] 是一个满足题意的答案。其他满足题意的答案有 [1,2,4]、[1,4,2] 和 [3,2,1]
# 示例 2：
#
# 输入：n = 4, paths = [[1,2],[3,4]]
# 输出：[1,2,1,2]
# 示例 3：
#
# 输入：n = 4, paths = [[1,2],[2,3],[3,4],[4,1],[1,3],[2,4]]
# 输出：[1,2,3,4]
#

class Solution:
    def gardenNoAdj(self, n: int, paths: List[List[int]]) -> List[int]:
        adj = {}
        for p in paths:
            if p[0] - 1 in adj:
                adj[p[0] - 1].add(p[1] - 1)
            else:
                adj[p[0] - 1] = {p[1] - 1}
            if p[1] - 1 in adj:
                adj[p[1] - 1].add(p[0] - 1)
            else:
                adj[p[1] - 1] = {p[0] - 1}

        d = [0] * n
        for i in range(n):
            s = [0] * 4
            if i in adj:
                a = adj[i]
                for x in a:
                    if d[x] != 0:
                        s[d[x] - 1] = 1
            for j in range(4):
                if s[j] == 0:
                    d[i] = j + 1
                    break
        return d


if __name__ == "__main__":
    n = 5
    paths = [[3,4],[4,5],[3,2],[5,1],[1,3],[4,2]]

    test = Solution().gardenNoAdj(n, paths)
    print(test)
