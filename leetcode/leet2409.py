import math
from bisect import bisect_right, bisect_left
from collections import defaultdict
from functools import lru_cache
from random import randint
from typing import List, Optional


# 2409. 统计共同度过的日子数
# Alice 和 Bob 计划分别去罗马开会。
#
# 给你四个字符串 arriveAlice ，leaveAlice ，arriveBob 和 leaveBob 。Alice 会在日期 arriveAlice 到 leaveAlice 之间在城市里（日期为闭区间），而 Bob 在日期 arriveBob 到 leaveBob 之间在城市里（日期为闭区间）。每个字符串都包含 5 个字符，格式为 "MM-DD" ，对应着一个日期的月和日。
#
# 请你返回 Alice和 Bob 同时在罗马的天数。
#
# 你可以假设所有日期都在 同一个 自然年，而且 不是 闰年。每个月份的天数分别为：[31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31] 。
#
#
#
# 示例 1：
#
# 输入：arriveAlice = "08-15", leaveAlice = "08-18", arriveBob = "08-16", leaveBob = "08-19"
# 输出：3
# 解释：Alice 从 8 月 15 号到 8 月 18 号在罗马。Bob 从 8 月 16 号到 8 月 19 号在罗马，他们同时在罗马的日期为 8 月 16、17 和 18 号。所以答案为 3 。
# 示例 2：
#
# 输入：arriveAlice = "10-01", leaveAlice = "10-31", arriveBob = "11-01", leaveBob = "12-31"
# 输出：0
# 解释：Alice 和 Bob 没有同时在罗马的日子，所以我们返回 0 。
#

class Solution:
    def countDaysTogether(self, arriveAlice: str, leaveAlice: str, arriveBob: str, leaveBob: str) -> int:
        aliceA = self.getDate(arriveAlice)
        bobA = self.getDate(arriveBob)
        aliceL = self.getDate(leaveAlice)
        bobL = self.getDate(leaveBob)

        if self.compareDate(aliceA, bobL) > 0 or self.compareDate(bobA, aliceL) > 0:
            return 0
        if self.compareDate(aliceA, bobA) >= 0:
            a = aliceA
        else:
            a = bobA
        if self.compareDate(bobL, aliceL) >= 0:
            b = aliceL
        else:
            b = bobL
        return self.diffDate(b, a)

    def getDate(self, date):
        d = date.split('-')
        return [int(x) for x in d]

    def compareDate(self, a, b):
        if a[0] > b[0]:
            return 1
        elif b[0] > a[0]:
            return -1
        else:
            if a[1] > b[1]:
                return 1
            elif b[1] > a[1]:
                return -1
            else:
                return 0

    def diffDate(self, a, b):
        days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        if a[0] > b[0]:
            c = sum(days[b[0] - 1: a[0] - 1]) - b[1] + a[1] + 1
            return c
        elif b[0] > a[0]:
            return -1
        else:
            if a[1] >= b[1]:
                return a[1] - b[1] + 1
            elif b[1] > a[1]:
                return -1


if __name__ == "__main__":
    arriveAlice = "10-01"
    leaveAlice = "11-30"
    arriveBob = "10-01"
    leaveBob = "12-31"

    test = Solution().countDaysTogether(arriveAlice, leaveAlice, arriveBob, leaveBob)
    print(test)
