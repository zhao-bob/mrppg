# 303. 区域和检索 - 数组不可变
# 简单
# 相关标签
# 相关企业
# 给定一个整数数组  nums，处理以下类型的多个查询:
#
# 计算索引 left 和 right （包含 left 和 right）之间的 nums 元素的 和 ，其中 left <= right
# 实现 NumArray 类：
#
# NumArray(int[] nums) 使用数组 nums 初始化对象
# int sumRange(int i, int j) 返回数组 nums 中索引 left 和 right 之间的元素的 总和 ，包含 left 和 right 两点（也就是 nums[left] + nums[left + 1] + ... + nums[right] )
#
#
# 示例 1：
#
# 输入：
# ["NumArray", "sumRange", "sumRange", "sumRange"]
# [[[-2, 0, 3, -5, 2, -1]], [0, 2], [2, 5], [0, 5]]
# 输出：
# [null, 1, -1, -3]
#
# 解释：
# NumArray numArray = new NumArray([-2, 0, 3, -5, 2, -1]);
# numArray.sumRange(0, 2); // return 1 ((-2) + 0 + 3)
# numArray.sumRange(2, 5); // return -1 (3 + (-5) + 2 + (-1))
# numArray.sumRange(0, 5); // return -3 ((-2) + 0 + 3 + (-5) + 2 + (-1))
#
#
# 提示：
#
# 1 <= nums.length <= 104
# -105 <= nums[i] <= 105
# 0 <= i <= j < nums.length
# 最多调用 104 次 sumRange 方法
#

import heapq
import math
from collections import Counter, deque, defaultdict
from datetime import date
from functools import cache
from typing import List, Optional

from sortedcontainers import SortedList


class NumArray:

    def __init__(self, nums: List[int]):
        self.sum = [0] * (len(nums) + 1)

        for i in range(1, len(nums) + 1):
            self.sum[i] = self.sum[i - 1] + nums[i - 1]

    def sumRange(self, left: int, right: int) -> int:
        return self.sum[right + 1] - self.sum[left]


if __name__ == "__main__":
    ops = ["NumArray", "sumRange", "sumRange", "sumRange"]
    par = [[[-2, 0, 3, -5, 2, -1]], [0, 2], [2, 5], [0, 5]]
    na = NumArray(par[0][0])
    res = []
    for i in range(1, len(par)):
        if ops[i] == "sumRange":
            res.append(na.sumRange(par[i][0], par[i][1]))
    print(res)
