import math
from typing import List


# 188. 买卖股票的最佳时机 IV
# 困难
# 1K
# 相关企业
# 给你一个整数数组 prices 和一个整数 k ，其中 prices[i] 是某支给定的股票在第 i 天的价格。
#
# 设计一个算法来计算你所能获取的最大利润。你最多可以完成 k 笔交易。也就是说，你最多可以买 k 次，卖 k 次。
#
# 注意：你不能同时参与多笔交易（你必须在再次购买前出售掉之前的股票）。
#
#
#
# 示例 1：
#
# 输入：k = 2, prices = [2,4,1]
# 输出：2
# 解释：在第 1 天 (股票价格 = 2) 的时候买入，在第 2 天 (股票价格 = 4) 的时候卖出，这笔交易所能获得利润 = 4-2 = 2 。
# 示例 2：
#
# 输入：k = 2, prices = [3,2,6,5,0,3]
# 输出：7
# 解释：在第 2 天 (股票价格 = 2) 的时候买入，在第 3 天 (股票价格 = 6) 的时候卖出, 这笔交易所能获得利润 = 6-2 = 4 。
#      随后，在第 5 天 (股票价格 = 0) 的时候买入，在第 6 天 (股票价格 = 3) 的时候卖出, 这笔交易所能获得利润 = 3-0 = 3 。
#


class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        f = [-math.inf] * (2 * k)

        # for i in range(2 * k):
        #     if i % 2 == 0:
        #         f[i] = - prices[0]
        #     else:
        #         f[i] = 0

        for i in range(len(prices)):
            f[0] = max(-prices[i], f[0])
            for j in range(1, 2 * k):
                if j % 2 == 1:
                    f[j] = max(f[j - 1] + prices[i], f[j])
                else:
                    f[j] = max(f[j - 1] - prices[i], f[j])
        return f[-1]



if __name__ == "__main__":
    k = 2
    prices = [3,2,6,5,0,3]
    test = Solution().maxProfit(k, prices)
    print(test)
