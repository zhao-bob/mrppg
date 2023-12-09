import heapq
import math
from collections import Counter
from functools import cache
from typing import List
from sortedcontainers import SortedList


# 1465. 切割后面积最大的蛋糕
# 提示
# 中等
# 52
# 相关企业
# 矩形蛋糕的高度为 h 且宽度为 w，给你两个整数数组 horizontalCuts 和 verticalCuts，其中：
#
#  horizontalCuts[i] 是从矩形蛋糕顶部到第  i 个水平切口的距离
# verticalCuts[j] 是从矩形蛋糕的左侧到第 j 个竖直切口的距离
# 请你按数组 horizontalCuts 和 verticalCuts 中提供的水平和竖直位置切割后，请你找出 面积最大 的那份蛋糕，并返回其 面积 。由于答案可能是一个很大的数字，因此需要将结果 对 109 + 7 取余 后返回。
#
#
#
# 示例 1：
#
#
#
# 输入：h = 5, w = 4, horizontalCuts = [1,2,4], verticalCuts = [1,3]
# 输出：4
# 解释：上图所示的矩阵蛋糕中，红色线表示水平和竖直方向上的切口。切割蛋糕后，绿色的那份蛋糕面积最大。
# 示例 2：
#
#
#
# 输入：h = 5, w = 4, horizontalCuts = [3,1], verticalCuts = [1]
# 输出：6
# 解释：上图所示的矩阵蛋糕中，红色线表示水平和竖直方向上的切口。切割蛋糕后，绿色和黄色的两份蛋糕面积最大。
# 示例 3：
#
# 输入：h = 5, w = 4, horizontalCuts = [3], verticalCuts = [3]
# 输出：9
#


class Solution:
    def maxArea(self, h: int, w: int, horizontalCuts: List[int], verticalCuts: List[int]) -> int:
        hi = [0] * (len(horizontalCuts) + 1)
        wi = [0] * (len(verticalCuts) + 1)
        k = 0
        horizontalCuts.sort()
        verticalCuts.sort()
        for i in range(len(horizontalCuts)):
            hi[i] = horizontalCuts[i] - k
            k = horizontalCuts[i]
        hi[-1] = h - k

        k = 0
        for i in range(len(verticalCuts)):
            wi[i] = verticalCuts[i] - k
            k = verticalCuts[i]
        wi[-1] = w - k

        return (max(hi) * max(wi)) % (10 ** 9 + 7)


if __name__ == "__main__":
    h = 5
    w = 4
    horizontalCuts = [3]
    verticalCuts = [3]
    test = Solution().maxArea(h, w, horizontalCuts, verticalCuts)
    print(test)
