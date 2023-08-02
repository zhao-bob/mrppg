import heapq
import math
from collections import Counter, deque
from functools import cache
from itertools import product
from typing import List, Optional


# 1681. 最小不兼容性
# 给你一个整数数组 nums​​​ 和一个整数 k 。你需要将这个数组划分到 k 个相同大小的子集中，使得同一个子集里面没有两个相同的元素。
#
# 一个子集的 不兼容性 是该子集里面最大值和最小值的差。
#
# 请你返回将数组分成 k 个子集后，各子集 不兼容性 的 和 的 最小值 ，如果无法分成分成 k 个子集，返回 -1 。
#
# 子集的定义是数组中一些数字的集合，对数字顺序没有要求。
#
#
#
# 示例 1：
#
# 输入：nums = [1,2,1,4], k = 2
# 输出：4
# 解释：最优的分配是 [1,2] 和 [1,4] 。
# 不兼容性和为 (2-1) + (4-1) = 4 。
# 注意到 [1,1] 和 [2,4] 可以得到更小的和，但是第一个集合有 2 个相同的元素，所以不可行。
# 示例 2：
#
# 输入：nums = [6,3,8,1,3,1,2,2], k = 4
# 输出：6
# 解释：最优的子集分配为 [1,2]，[2,3]，[6,8] 和 [1,3] 。
# 不兼容性和为 (2-1) + (3-2) + (8-6) + (3-1) = 6 。
# 示例 3：
#
# 输入：nums = [5,3,3,6,3,3], k = 3
# 输出：-1
# 解释：没办法将这些数字分配到 3 个子集且满足每个子集里没有相同数字。
#

class Solution:
    def minimumIncompatibility(self, nums: List[int], k: int) -> int:
        # 设nums数为n，则每次取n // k个数形成一组，预处理所有可能的组的组合，算出不兼容性，初始dp[0]=0，然后取一组，剩余的从没有取的集合的子集里选取，更新dp
        n = len(nums)
        dp = [math.inf] * (1 << n)
        dp[0] = 0
        group = n // k
        values = {}

        for mask in range(1 << n):
            if mask.bit_count() != group:
                continue
            mn = 20
            mx = 0
            cur = set()
            for i in range(n):
                if mask & (1 << i) > 0:
                    if nums[i] in cur:
                        break
                    cur.add(nums[i])
                    mn = min(mn, nums[i])
                    mx = max(mx, nums[i])
            if len(cur) == group:
                values[mask] = mx - mn

        for mask in range(1 << n):
            if dp[mask] == math.inf:
                continue
            seen = {}
            for i in range(n):
                if mask & (1 << i) == 0:
                    seen[nums[i]] = i
            if len(seen) < group:
                continue
            sub = 0
            for v in seen:
                sub |= 1 << seen[v]
            nxt = sub
            while nxt > 0:
                if nxt in values:
                    dp[mask | nxt] = min(dp[mask | nxt], dp[mask] + values[nxt])
                nxt = (nxt - 1) & sub

        return dp[-1] if dp[-1] < math.inf else -1



if __name__ == "__main__":
    nums = [1,2,1,4]
    k = 2

    test = Solution().minimumIncompatibility(nums, k)
    print(test)
