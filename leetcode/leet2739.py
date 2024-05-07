import heapq
import math
from collections import deque, Counter
from itertools import count
from typing import List, Optional


# 2739. 总行驶距离
# 简单
# 相关标签
# 相关企业
# 提示
# 卡车有两个油箱。给你两个整数，mainTank 表示主油箱中的燃料（以升为单位），additionalTank 表示副油箱中的燃料（以升为单位）。
#
# 该卡车每耗费 1 升燃料都可以行驶 10 km。每当主油箱使用了 5 升燃料时，如果副油箱至少有 1 升燃料，则会将 1 升燃料从副油箱转移到主油箱。
#
# 返回卡车可以行驶的最大距离。
#
# 注意：从副油箱向主油箱注入燃料不是连续行为。这一事件会在每消耗 5 升燃料时突然且立即发生。
#
#
#
# 示例 1：
#
# 输入：mainTank = 5, additionalTank = 10
# 输出：60
# 解释：
# 在用掉 5 升燃料后，主油箱中燃料还剩下 (5 - 5 + 1) = 1 升，行驶距离为 50km 。
# 在用掉剩下的 1 升燃料后，没有新的燃料注入到主油箱中，主油箱变为空。
# 总行驶距离为 60km 。
# 示例 2：
#
# 输入：mainTank = 1, additionalTank = 2
# 输出：10
# 解释：
# 在用掉 1 升燃料后，主油箱变为空。
# 总行驶距离为 10km 。
#
#
# 提示：
#
# 1 <= mainTank, additionalTank <= 100
#


class Solution:
    def distanceTraveled(self, mainTank: int, additionalTank: int) -> int:
        # res = 0
        # while mainTank > 0 and additionalTank > 0:
        #     if mainTank >= 5:
        #         res += 50
        #         mainTank -= 4
        #         additionalTank -= 1
        #     else:
        #         res += 10 * mainTank
        #         mainTank = 0
        # if mainTank > 0:
        #     res += 10 * mainTank
        # return res

        return (mainTank + min(additionalTank, (mainTank - 1) // 4)) * 10

if __name__ == "__main__":
    mainTank = 100
    additionalTank = 40

    test = Solution().distanceTraveled(mainTank, additionalTank)
    print(test)
