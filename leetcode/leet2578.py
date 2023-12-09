import heapq
import math
from typing import List
from sortedcontainers import SortedList


# 2578. 最小和分割
# 提示
# 简单
# 30
# 相关企业
# 给你一个正整数 num ，请你将它分割成两个非负整数 num1 和 num2 ，满足：
#
# num1 和 num2 直接连起来，得到 num 各数位的一个排列。
# 换句话说，num1 和 num2 中所有数字出现的次数之和等于 num 中所有数字出现的次数。
# num1 和 num2 可以包含前导 0 。
# 请你返回 num1 和 num2 可以得到的和的 最小 值。
#
# 注意：
#
# num 保证没有前导 0 。
# num1 和 num2 中数位顺序可以与 num 中数位顺序不同。
#
#
# 示例 1：
#
# 输入：num = 4325
# 输出：59
# 解释：我们可以将 4325 分割成 num1 = 24 和 num2 = 35 ，和为 59 ，59 是最小和。
# 示例 2：
#
# 输入：num = 687
# 输出：75
# 解释：我们可以将 687 分割成 num1 = 68 和 num2 = 7 ，和为最优值 75 。
#


class Solution:
    def splitNum(self, num: int) -> int:
        digits = []
        while num > 0:
            digits.append(num % 10)
            num = num // 10
        digits.sort()

        # if len(digits) % 2 == 0:
        #     i = 0
        #     even = 0
        #     odd = 0
        # else:
        #     i = 1
        #     even = 0
        #     odd = digits[0]
        even = 0
        odd = 0
        for k in range(len(digits)):
            if k % 2 == 0:
                even = even * 10 + digits[k]
            else:
                odd = odd * 10 + digits[k]
        return even + odd


if __name__ == "__main__":
    num = 687
    test = Solution().splitNum(num)
    print(test)
