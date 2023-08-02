import heapq
import math
from collections import Counter
from typing import List, Optional


# 2611. 老鼠和奶酪
# 有两只老鼠和 n 块不同类型的奶酪，每块奶酪都只能被其中一只老鼠吃掉。
#
# 下标为 i 处的奶酪被吃掉的得分为：
#
# 如果第一只老鼠吃掉，则得分为 reward1[i] 。
# 如果第二只老鼠吃掉，则得分为 reward2[i] 。
# 给你一个正整数数组 reward1 ，一个正整数数组 reward2 ，和一个非负整数 k 。
#
# 请你返回第一只老鼠恰好吃掉 k 块奶酪的情况下，最大 得分为多少。
#
#
#
# 示例 1：
#
# 输入：reward1 = [1,1,3,4], reward2 = [4,4,1,1], k = 2
# 输出：15
# 解释：这个例子中，第一只老鼠吃掉第 2 和 3 块奶酪（下标从 0 开始），第二只老鼠吃掉第 0 和 1 块奶酪。
# 总得分为 4 + 4 + 3 + 4 = 15 。
# 15 是最高得分。
# 示例 2：
#
# 输入：reward1 = [1,1], reward2 = [1,1], k = 2
# 输出：2
# 解释：这个例子中，第一只老鼠吃掉第 0 和 1 块奶酪（下标从 0 开始），第二只老鼠不吃任何奶酪。
# 总得分为 1 + 1 = 2 。
# 2 是最高得分。
#

class Solution:
    def miceAndCheese(self, reward1: List[int], reward2: List[int], k: int) -> int:
        s = 0
        d = [0] * len(reward1)

        for i in range(len(reward1)):
            s += reward1[i]
            d[i] = reward2[i] - reward1[i]

        d.sort(reverse=True)

        for i in range(len(reward1) - k):
            s += d[i]
        return s




if __name__ == "__main__":
    reward1 = [1,1]
    reward2 = [1,1]
    k = 2
    test = Solution().miceAndCheese(reward1, reward2, k)
    print(test)
