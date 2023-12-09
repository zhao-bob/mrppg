import heapq
import math
from collections import Counter, deque, defaultdict
from functools import cache, reduce
from itertools import product
from typing import List, Optional


# 307. 区域和检索 - 数组可修改
# 中等
# 636
# 相关企业
# 给你一个数组 nums ，请你完成两类查询。
#
# 其中一类查询要求 更新 数组 nums 下标对应的值
# 另一类查询要求返回数组 nums 中索引 left 和索引 right 之间（ 包含 ）的nums元素的 和 ，其中 left <= right
# 实现 NumArray 类：
#
# NumArray(int[] nums) 用整数数组 nums 初始化对象
# void update(int index, int val) 将 nums[index] 的值 更新 为 val
# int sumRange(int left, int right) 返回数组 nums 中索引 left 和索引 right 之间（ 包含 ）的nums元素的 和 （即，nums[left] + nums[left + 1], ..., nums[right]）
#
#
# 示例 1：
#
# 输入：
# ["NumArray", "sumRange", "update", "sumRange"]
# [[[1, 3, 5]], [0, 2], [1, 2], [0, 2]]
# 输出：
# [null, 9, null, 8]
#
# 解释：
# NumArray numArray = new NumArray([1, 3, 5]);
# numArray.sumRange(0, 2); // 返回 1 + 3 + 5 = 9
# numArray.update(1, 2);   // nums = [1,2,5]
# numArray.sumRange(0, 2); // 返回 1 + 2 + 5 = 8
#
#
class TreeNode:
    def __init__(self, l, r, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        self.l = l
        self.r = r
        self.update = False


def initSegTree(l, r, nums: List[int]):
    if l == r:
        return TreeNode(l, r, nums[l])
    mid = (l + r) // 2
    node = TreeNode(l, r)
    node.left = initSegTree(l, mid, nums)
    node.right = initSegTree(mid + 1, r, nums)
    node.val = node.left.val + node.right.val
    return node


def searchSegTree(l, r, node):
    if node.l == l and node.r == r:
        return node.val
    mid = (node.l + node.r) // 2
    res = 0
    if r <= mid:
        res += searchSegTree(l, r, node.left)
    elif l > mid:
        res += searchSegTree(l, r, node.right)
    else:
        res += searchSegTree(l, mid, node.left)
        res += searchSegTree(mid + 1, r, node.right)
    return res


def updateSegTree(index, val, node):
    if node.l == index and node.r == index:
        diff = val - node.val
        node.val = val
        return diff

    mid = (node.l + node.r) // 2
    if index <= mid:
        diff = updateSegTree(index, val, node.left)
    else:
        diff = updateSegTree(index, val, node.right)
    if diff != 0:
        node.val += diff
    return diff


class NumArray:

    def __init__(self, nums: List[int]):
        self.root = initSegTree(0, len(nums) - 1, nums)

    def update(self, index: int, val: int) -> None:
        updateSegTree(index, val, self.root)

    def sumRange(self, left: int, right: int) -> int:
        return searchSegTree(left, right, self.root)


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# obj.update(index,val)
# param_2 = obj.sumRange(left,right)


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# obj.update(index,val)
# param_2 = obj.sumRange(left,right)


if __name__ == "__main__":
    ops = ["NumArray","sumRange","sumRange","sumRange","update","update","update","sumRange","update","sumRange","update"]
    par = [[[0,9,5,7,3]],[4,4],[2,4],[3,3],[4,5],[1,7],[0,8],[1,2],[1,9],[4,4],[3,4]]
    na = NumArray(par[0][0])
    res = []
    for i in range(1, len(par)):
        if ops[i] == "sumRange":
            res.append(na.sumRange(par[i][0], par[i][1]))
        elif ops[i] == "update":
            res.append(na.update(par[i][0], par[i][1]))
    print(res)
