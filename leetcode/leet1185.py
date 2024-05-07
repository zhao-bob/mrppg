# 1185. 一周中的第几天
# 提示
# 简单
# 133
# 相关企业
# 给你一个日期，请你设计一个算法来判断它是对应一周中的哪一天。
#
# 输入为三个整数：day、month 和 year，分别表示日、月、年。
#
# 您返回的结果必须是这几个值中的一个 {"Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"}。
#
#
#
# 示例 1：
#
# 输入：day = 31, month = 8, year = 2019
# 输出："Saturday"
# 示例 2：
#
# 输入：day = 18, month = 7, year = 1999
# 输出："Sunday"
# 示例 3：
#
# 输入：day = 15, month = 8, year = 1993
# 输出："Sunday"
#

import heapq
import math
from datetime import date
from typing import List


class Solution:
    def dayOfTheWeek(self, day: int, month: int, year: int) -> str:
        d = date(year, month, day)
        return d.strftime("%A")

if __name__ == "__main__":
    day = 31
    month = 8
    year = 2019
    test = Solution().dayOfTheWeek(day, month, year)
    print(test)
