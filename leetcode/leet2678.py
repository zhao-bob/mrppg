import heapq
import math
from collections import Counter
from typing import List
from sortedcontainers import SortedList


# 2678. 老人的数目
# 提示
# 简单
# 17
# 相关企业
# 给你一个下标从 0 开始的字符串 details 。details 中每个元素都是一位乘客的信息，信息用长度为 15 的字符串表示，表示方式如下：
#
# 前十个字符是乘客的手机号码。
# 接下来的一个字符是乘客的性别。
# 接下来两个字符是乘客的年龄。
# 最后两个字符是乘客的座位号。
# 请你返回乘客中年龄 严格大于 60 岁 的人数。
#
#
#
# 示例 1：
#
# 输入：details = ["7868190130M7522","5303914400F9211","9273338290F4010"]
# 输出：2
# 解释：下标为 0 ，1 和 2 的乘客年龄分别为 75 ，92 和 40 。所以有 2 人年龄大于 60 岁。
# 示例 2：
#
# 输入：details = ["1313579440F2036","2921522980M5644"]
# 输出：0
# 解释：没有乘客的年龄大于 60 岁。
#


class Solution:
    def countSeniors(self, details: List[str]) -> int:
        res = 0
        for d in details:
            age = int(d[11:13])
            if age > 60:
                res += 1
        return res


if __name__ == "__main__":
    details = ["7868190130M7522", "5303914400F9211", "9273338290F4010"]
    test = Solution().countSeniors(details)
    print(test)
