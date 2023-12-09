import math
from typing import List


# 309. 买卖股票的最佳时机含冷冻期
# 中等
# 1.6K
# 相关企业
# 给定一个整数数组prices，其中第  prices[i] 表示第 i 天的股票价格 。​
#
# 设计一个算法计算出最大利润。在满足以下约束条件下，你可以尽可能地完成更多的交易（多次买卖一支股票）:
#
# 卖出股票后，你无法在第二天买入股票 (即冷冻期为 1 天)。
# 注意：你不能同时参与多笔交易（你必须在再次购买前出售掉之前的股票）。
#
#
#
# 示例 1:
#
# 输入: prices = [1,2,3,0,2]
# 输出: 3
# 解释: 对应的交易状态为: [买入, 卖出, 冷冻期, 买入, 卖出]
# 示例 2:
#
# 输入: prices = [1]
# 输出: 0
#


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        f = [[0 for _ in range(len(prices))] for _ in range(2)]
        f[0][0] = -prices[0]
        f[1][0] = 0

        for i in range(1, len(prices)):
            if i >= 2:
                f[0][i] = max(f[1][i - 2] - prices[i], f[0][i - 1])
            else:
                f[0][i] = max(-prices[i], f[0][i - 1])
            f[1][i] = max(f[0][i - 1] + prices[i], f[1][i - 1])

        return f[1][-1]


if __name__ == "__main__":
    prices = [1]
    test = Solution().maxProfit(prices)
    print(test)
