# 2834. 找出美丽数组的最小和
# 中等
# 相关标签
# 相关企业
# 提示
# 给你两个正整数：n 和 target 。
#
# 如果数组 nums 满足下述条件，则称其为 美丽数组 。
#
# nums.length == n.
# nums 由两两互不相同的正整数组成。
# 在范围 [0, n-1] 内，不存在 两个 不同 下标 i 和 j ，使得 nums[i] + nums[j] == target 。
# 返回符合条件的美丽数组所可能具备的 最小 和，并对结果进行取模 109 + 7。
#
#
#
# 示例 1：
#
# 输入：n = 2, target = 3
# 输出：4
# 解释：nums = [1,3] 是美丽数组。
# - nums 的长度为 n = 2 。
# - nums 由两两互不相同的正整数组成。
# - 不存在两个不同下标 i 和 j ，使得 nums[i] + nums[j] == 3 。
# 可以证明 4 是符合条件的美丽数组所可能具备的最小和。
# 示例 2：
#
# 输入：n = 3, target = 3
# 输出：8
# 解释：
# nums = [1,3,4] 是美丽数组。
# - nums 的长度为 n = 3 。
# - nums 由两两互不相同的正整数组成。
# - 不存在两个不同下标 i 和 j ，使得 nums[i] + nums[j] == 3 。
# 可以证明 8 是符合条件的美丽数组所可能具备的最小和。
# 示例 3：
#
# 输入：n = 1, target = 1
# 输出：1
# 解释：nums = [1] 是美丽数组。
#
#
# 提示：
#
# 1 <= n <= 109
# 1 <= target <= 109
#

import heapq
import math
from collections import Counter, deque, defaultdict
from datetime import date
from functools import cache
from typing import List, Optional

from sortedcontainers import SortedList


class Solution:
    def minimumPossibleSum(self, n: int, target: int) -> int:
        if target % 2 == 1:
            k = (target - 1) // 2
        else:
            k = target // 2
        if k >= n:
            return (n * (n + 1) // 2) % (10 ** 9 + 7)
        else:
            return ((1 + k) * k // 2 + (target + target + n - k - 1) * (n - k) // 2) % (10 ** 9 + 7)


if __name__ == "__main__":
    n = 3
    target = 3
    test = Solution().minimumPossibleSum(n, target)
    print(test)
