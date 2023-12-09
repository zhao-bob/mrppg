import math
from typing import List


# 901. 股票价格跨度
# 中等
# 359
# 相关企业
# 设计一个算法收集某些股票的每日报价，并返回该股票当日价格的 跨度 。
#
# 当日股票价格的 跨度 被定义为股票价格小于或等于今天价格的最大连续日数（从今天开始往回数，包括今天）。
#
# 例如，如果未来 7 天股票的价格是 [100,80,60,70,60,75,85]，那么股票跨度将是 [1,1,1,2,1,4,6] 。
#
# 实现 StockSpanner 类：
#
# StockSpanner() 初始化类对象。
# int next(int price) 给出今天的股价 price ，返回该股票当日价格的 跨度 。
#
#
# 示例：
#
# 输入：
# ["StockSpanner", "next", "next", "next", "next", "next", "next", "next"]
# [[], [100], [80], [60], [70], [60], [75], [85]]
# 输出：
# [null, 1, 1, 1, 2, 1, 4, 6]
#
# 解释：
# StockSpanner stockSpanner = new StockSpanner();
# stockSpanner.next(100); // 返回 1
# stockSpanner.next(80);  // 返回 1
# stockSpanner.next(60);  // 返回 1
# stockSpanner.next(70);  // 返回 2
# stockSpanner.next(60);  // 返回 1
# stockSpanner.next(75);  // 返回 4 ，因为截至今天的最后 4 个股价 (包括今天的股价 75) 都小于或等于今天的股价。
# stockSpanner.next(85);  // 返回 6
#


class StockSpanner:

    def __init__(self):
        self.spanner = []

    def next(self, price: int) -> int:
        if self.spanner:
            if self.spanner[-1][0] > price:
                self.spanner.append([price, 1])
                return 1
            else:
                res = 1
                while self.spanner and self.spanner[-1][0] <= price:
                    res += self.spanner.pop()[1]
                self.spanner.append([price, res])
                return res
        else:
            self.spanner.append([price, 1])
            return 1


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)


if __name__ == "__main__":
    ops = ["StockSpanner","next","next","next","next","next","next","next","next","next"]
    par = [[],[60],[80],[60],[70],[60],[75],[85],[80],[85]]
    ss = StockSpanner()
    res = []
    for i in range(1, len(par)):
        if ops[i] == "next":
            res.append(ss.next(par[i][0]))
    print(res)
