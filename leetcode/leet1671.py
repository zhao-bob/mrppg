import heapq
import math
from typing import List, Optional


# 1671. 得到山形数组的最少删除次数
# 提示
# 困难
# 63
# 相关企业
# 我们定义 arr 是 山形数组 当且仅当它满足：
#
# arr.length >= 3
# 存在某个下标 i （从 0 开始） 满足 0 < i < arr.length - 1 且：
# arr[0] < arr[1] < ... < arr[i - 1] < arr[i]
# arr[i] > arr[i + 1] > ... > arr[arr.length - 1]
# 给你整数数组 nums​ ，请你返回将 nums 变成 山形状数组 的​ 最少 删除次数。
#
#
#
# 示例 1：
#
# 输入：nums = [1,3,1]
# 输出：0
# 解释：数组本身就是山形数组，所以我们不需要删除任何元素。
# 示例 2：
#
# 输入：nums = [2,1,1,5,6,2,3,1]
# 输出：3
# 解释：一种方法是将下标为 0，1 和 5 的元素删除，剩余元素为 [1,5,6,3,1] ，是山形数组。
#
from sortedcontainers import SortedDict, SortedList


class Solution:
    def minimumMountainRemovals(self, nums: List[int]) -> int:
        n = len(nums)
        lr = [0] * n
        sr = SortedList()

        le = [0] * n

        for i in range(n):
            for j in range(len(sr)):
                if nums[sr[j][1]] < nums[i]:
                    lr[i] = sr[j][0] + i
                    le[i] = 1
                    break
                else:
                    lr[i] = i
            sr.add((lr[i] - i - 1, i))

        rr = [0] * n
        sr = SortedList()
        re = [0] * n
        for i in range(n - 1, -1, -1):
            for j in range(len(sr)):
                if nums[sr[j][1]] < nums[i]:
                    rr[i] = sr[j][0] - i
                    re[i] = 1
                    break
            else:
                rr[i] = n - i - 1
            sr.add((rr[i] + i - 1, i))

        res = math.inf
        for i in range(1, n - 1):
            if re[i] != 0 and le[i] != 0:
                res = min(res, lr[i] + rr[i])
        return res
    # for i in range(n):
    #     if stkd:
    #         if nums[i] > nums[i - 1]:
    #             lr[i] = lr[i - 1]
    #             le[i] = 1
    #             while stkd and nums[stkd[-1]] < nums[i]:
    #                 lr[i] = min(lr[i], lr[stkd[-1]] + i - 1 - stkd[-1])
    #                 stkd.pop()
    #         else:
    #             while stku and nums[stku[-1]] >= nums[i]:
    #                 stku.pop()
    #             if stku:
    #                 lr[i] = lr[stku[-1]] + i - 1 - stku[-1]
    #                 le[i] = 1
    #             else:
    #                 lr[i] = i
    #     stku.append(i)
    #     stkd.append(i)
    #
    # rr = [0] * n
    # stkd = []
    # stku = []
    # re = [0] * n
    #
    # for i in range(n - 1, -1, -1):
    #     if stkd:
    #         if nums[i] > nums[i + 1]:
    #             rr[i] = rr[i + 1]
    #             re[i] = 1
    #             while stkd and nums[stkd[-1]] < nums[i]:
    #                 rr[i] = min(rr[i], rr[stkd[-1]] + stkd[-1] - 1 - i)
    #                 stkd.pop()
    #         else:
    #             while stku and nums[stku[-1]] >= nums[i]:
    #                 stku.pop()
    #             if stku:
    #                 rr[i] = rr[stku[-1]] + stku[-1] - 1 - i
    #                 re[i] = 1
    #             else:
    #                 rr[i] = n - 1 - i
    #     stku.append(i)
    #     stkd.append(i)


if __name__ == "__main__":
    nums = [1734846,657301534,202183831,84229134,242792360,402042562,407999894,513769671,525744287,826118159,227900438,551758234,552318472,501708629,729751186,869478695,907554366,198244004,803977850,401105617,58874439,575074508,311563251,363497745,333929956,971094168,129405760,139867083,227379934]
    nnums = [0] * len(nums)
    for i, e in enumerate(sorted([(n, i) for i, n in enumerate(nums)])):
        nnums[e[1]] = i
    test = Solution().minimumMountainRemovals(nnums)
    print(test)
