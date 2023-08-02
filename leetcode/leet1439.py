import heapq
import math
from typing import List


# 1439. 有序矩阵中的第 k 个最小数组和
# 给你一个 m * n 的矩阵 mat，以及一个整数 k ，矩阵中的每一行都以非递减的顺序排列。
#
# 你可以从每一行中选出 1 个元素形成一个数组。返回所有可能数组中的第 k 个 最小 数组和。
#
#
#
# 示例 1：
#
# 输入：mat = [[1,3,11],[2,4,6]], k = 5
# 输出：7
# 解释：从每一行中选出一个元素，前 k 个和最小的数组分别是：
# [1,2], [1,4], [3,2], [3,4], [1,6]。其中第 5 个的和是 7 。
# 示例 2：
#
# 输入：mat = [[1,3,11],[2,4,6]], k = 9
# 输出：17
# 示例 3：
#
# 输入：mat = [[1,10,10],[1,4,5],[2,3,6]], k = 7
# 输出：9
# 解释：从每一行中选出一个元素，前 k 个和最小的数组分别是：
# [1,1,2], [1,1,3], [1,4,2], [1,4,3], [1,1,6], [1,5,2], [1,5,3]。其中第 7 个的和是 9 。
# 示例 4：
#
# 输入：mat = [[1,1,10],[2,2,9]], k = 7
# 输出：12
#

class Solution:
    def kthSmallest(self, mat: List[List[int]], k: int) -> int:
        def merge(f: List[int], g: List[int], k: int) -> List[int]:
            if len(g) > len(f):
                return merge(g, f, k)

            q = [(f[0] + g[i], 0, i) for i in range(len(g))]
            heapq.heapify(q)

            ans = list()
            while k and q:
                entry = heapq.heappop(q)
                ans.append(entry[0])
                if entry[1] + 1 < len(f):
                    heapq.heappush(q, (f[entry[1] + 1] + g[entry[2]], entry[1] + 1, entry[2]))
                k -= 1

            return ans

        prev = mat[0]
        for i in range(1, len(mat)):
            prev = merge(prev, mat[i], k)
        return prev[k - 1]


if __name__ == "__main__":
    mat = [[1,3,11],[2,4,6]]
    k = 9
    test = Solution().kthSmallest(mat, k)
    print(test)
