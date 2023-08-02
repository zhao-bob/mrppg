import heapq
import math
from collections import Counter, deque
from functools import cache
from itertools import product
from typing import List, Optional

# 1499. 满足不等式的最大值
# 给你一个数组 points 和一个整数 k 。数组中每个元素都表示二维平面上的点的坐标，并按照横坐标 x 的值从小到大排序。也就是说 points[i] = [xi, yi] ，并且在 1 <= i < j <= points.length 的前提下， xi < xj 总成立。
#
# 请你找出 yi + yj + |xi - xj| 的 最大值，其中 |xi - xj| <= k 且 1 <= i < j <= points.length。
#
# 题目测试数据保证至少存在一对能够满足 |xi - xj| <= k 的点。
#
#
#
# 示例 1：
#
# 输入：points = [[1,3],[2,0],[5,10],[6,-10]], k = 1
# 输出：4
# 解释：前两个点满足 |xi - xj| <= 1 ，代入方程计算，则得到值 3 + 0 + |1 - 2| = 4 。第三个和第四个点也满足条件，得到值 10 + -10 + |5 - 6| = 1 。
# 没有其他满足条件的点，所以返回 4 和 1 中最大的那个。
# 示例 2：
#
# 输入：points = [[0,0],[3,0],[9,2]], k = 3
# 输出：3
# 解释：只有前两个点满足 |xi - xj| <= 3 ，代入方程后得到值 0 + 0 + |0 - 3| = 3 。
#

class Solution:
    def findMaxValueOfEquation(self, points: List[List[int]], k: int) -> int:
        # xj+yj-(xi-yi)，所以用堆保存xi-yi，取出满足|xi-xj|<=k最小的，不满足的丢弃，因为|xi|已经排序，后面i不可能满足|xi-xj|<=k，遍历所有点即可
        # h = []
        # res = -math.inf
        # for i in range(len(points)):
        #     while len(h) > 0 and points[i][0] - h[0][1] > k:
        #         heapq.heappop(h)
        #     a = (points[i][0] - points[i][1], points[i][0])
        #     if len(h) > 0:
        #         res = max(points[i][0] + points[i][1] - h[0][0], res)
        #     heapq.heappush(h, a)
        # return res

        q = deque()
        res = -math.inf
        for i in range(len(points)):
            while len(q) > 0 and points[i][0] - q[0][1] > k:
                q.popleft()
            a = (points[i][1] - points[i][0], points[i][0])
            if len(q) > 0:
                res = max(points[i][0] + points[i][1] + q[0][0], res)
            while len(q) > 0 and a[0] >= q[-1][0]:
                q.pop()
            q.append(a)
        return res

if __name__ == "__main__":
    points = [[0,0],[3,0],[9,2]]
    k = 3

    test = Solution().findMaxValueOfEquation(points, k)
    print(test)
