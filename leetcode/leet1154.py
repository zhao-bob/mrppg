# 1154. 一年中的第几天
# 提示
# 简单
# 126
# 相关企业
# 给你一个字符串 date ，按 YYYY-MM-DD 格式表示一个 现行公元纪年法 日期。返回该日期是当年的第几天。
#
#
#
# 示例 1：
#
# 输入：date = "2019-01-09"
# 输出：9
# 解释：给定日期是2019年的第九天。
# 示例 2：
#
# 输入：date = "2019-02-10"
# 输出：41
#

import heapq
import math
from datetime import date
from typing import List


class Solution:
    def dayOfYear(self, date: str) -> int:
        d = list(map(int, date.split('-')))
        days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        res = 0
        for i in range(d[1] - 1):
            res += days[i]
        res += d[2]
        if (d[0] % 4 == 0 and d[0] % 100 != 0 or d[0] % 400 == 0) and d[1] >= 3:
            res += 1
        return res



if __name__ == "__main__":
    date = "2019-02-10"
    test = Solution().dayOfYear(date)
    print(test)
