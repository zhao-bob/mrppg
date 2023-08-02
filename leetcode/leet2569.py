import heapq
import math
from collections import Counter, deque
from functools import cache
from itertools import product
from typing import List, Optional


# 2569. 更新数组后处理求和查询
# 给你两个下标从 0 开始的数组 nums1 和 nums2 ，和一个二维数组 queries 表示一些操作。总共有 3 种类型的操作：
#
# 操作类型 1 为 queries[i] = [1, l, r] 。你需要将 nums1 从下标 l 到下标 r 的所有 0 反转成 1 或将 1 反转成 0 。l 和 r 下标都从 0 开始。
# 操作类型 2 为 queries[i] = [2, p, 0] 。对于 0 <= i < n 中的所有下标，令 nums2[i] = nums2[i] + nums1[i] * p 。
# 操作类型 3 为 queries[i] = [3, 0, 0] 。求 nums2 中所有元素的和。
# 请你返回一个数组，包含所有第三种操作类型的答案。
#
#
#
# 示例 1：
#
# 输入：nums1 = [1,0,1], nums2 = [0,0,0], queries = [[1,1,1],[2,1,0],[3,0,0]]
# 输出：[3]
# 解释：第一个操作后 nums1 变为 [1,1,1] 。第二个操作后，nums2 变成 [1,1,1] ，所以第三个操作的答案为 3 。所以返回 [3] 。
# 示例 2：
#
# 输入：nums1 = [1], nums2 = [5], queries = [[2,0,0],[3,0,0]]
# 输出：[5]
# 解释：第一个操作后，nums2 保持不变为 [5] ，所以第二个操作的答案是 5 。所以返回 [5] 。
#

class Solution:
    def handleQuery(self, nums1: List[int], nums2: List[int], queries: List[List[int]]) -> List[int]:
        n = len(nums1)
        m = len(queries)
        seg_tree = SegTree(nums1)

        total = sum(nums2)
        ans = []
        for i in range(m):
            if queries[i][0] == 1:
                l = queries[i][1]
                r = queries[i][2]
                seg_tree.reverse_range(l, r)
            elif queries[i][0] == 2:
                total += seg_tree.sum_range(0, n - 1) * queries[i][1]
            elif queries[i][0] == 3:
                ans.append(total)
        return ans


class SegTree:
    def __init__(self, nums):
        n = len(nums)
        self.arr = [SegNode() for _ in range(n * 4 + 1)]
        self.build(1, 0, n - 1, nums)

    def sum_range(self, left, right):
        return self.query(1, left, right)

    def reverse_range(self, left, right):
        self.modify(1, left, right)

    def build(self, id, l, r, nums):
        arr = self.arr
        arr[id] = SegNode()
        arr[id].l = l
        arr[id].r = r
        arr[id].lazytag = False
        if l == r:
            arr[id].sum = nums[l]
            return
        mid = (l + r) >> 1
        self.build(2 * id, l, mid, nums)
        self.build(2 * id + 1, mid + 1, r, nums)
        arr[id].sum = arr[2 * id].sum + arr[2 * id + 1].sum

    # pushdown函数：下传懒标记，即将当前区间的修改情况下传到其左右孩子结点
    def pushdown(self, x):
        arr = self.arr
        if arr[x].lazytag:
            arr[2 * x].lazytag = not arr[2 * x].lazytag
            arr[2 * x].sum = arr[2 * x].r - arr[2 * x].l + 1 - arr[2 * x].sum
            arr[2 * x + 1].lazytag = not arr[2 * x + 1].lazytag
            arr[2 * x + 1].sum = arr[2 * x + 1].r - arr[2 * x + 1].l + 1 - arr[2 * x + 1].sum
            arr[x].lazytag = False

    # 区间修改
    def modify(self, id, l, r):
        arr = self.arr
        if arr[id].l >= l and arr[id].r <= r:
            arr[id].sum = (arr[id].r - arr[id].l + 1) - arr[id].sum
            arr[id].lazytag = not arr[id].lazytag
            return
        self.pushdown(id)
        mid = (arr[id].l + arr[id].r) >> 1
        if arr[2 * id].r >= l:
            self.modify(2 * id, l, r)
        if arr[2 * id + 1].l <= r:
            self.modify(2 * id + 1, l, r)
        arr[id].sum = arr[2 * id].sum + arr[2 * id + 1].sum

    # 区间查询
    def query(self, id, l, r):
        arr = self.arr
        if arr[id].l >= l and arr[id].r <= r:
            return arr[id].sum
        if arr[id].r < l or arr[id].l > r:
            return 0
        self.pushdown(id)
        mid = (arr[id].l + arr[id].r) >> 1
        res = 0
        if arr[2 * id].r >= l:
            res += self.query(2 * id, l, r)
        if arr[2 * id + 1].l <= r:
            res += self.query(2 * id + 1, l, r)
        return res


class SegNode:
    def __init__(self):
        self.l = 0
        self.r = 0
        self.sum = 0
        self.lazytag = False


if __name__ == "__main__":
    nums1 = [1, 0, 1]
    nums2 = [0, 0, 0]
    queries = [[1, 1, 1], [2, 1, 0], [3, 0, 0]]

    test = Solution().handleQuery(nums1, nums2, queries)
    print(test)
