import heapq
import math
from collections import Counter
from functools import cache
from typing import List
from sortedcontainers import SortedList


# 2520. 统计能整除数字的位数
# 提示
# 简单
# 16
# 相关企业
# 给你一个整数 num ，返回 num 中能整除 num 的数位的数目。
#
# 如果满足 nums % val == 0 ，则认为整数 val 可以整除 nums 。
#
#
#
# 示例 1：
#
# 输入：num = 7
# 输出：1
# 解释：7 被自己整除，因此答案是 1 。
# 示例 2：
#
# 输入：num = 121
# 输出：2
# 解释：121 可以被 1 整除，但无法被 2 整除。由于 1 出现两次，所以返回 2 。
# 示例 3：
#
# 输入：num = 1248
# 输出：4
# 解释：1248 可以被它每一位上的数字整除，因此答案是 4 。
#


class Solution:
    def countDigits(self, num: int) -> int:
        res = 0
        for s in str(num):
            if int(s) != 0 and num % int(s) == 0:
                res += 1
        return res

    # res = 0
    # remain = num
    # while remain > 0:
    #     if num % (remain % 10) == 0:
    #         res += 1
    #     remain //= 10
    # return res


if __name__ == "__main__":
    num = 121
    test = Solution().countDigits(num)
    print(test)
