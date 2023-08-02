import heapq
import math
from collections import Counter
from typing import List, Optional


# 1240. 铺瓷砖
# 你是一位施工队的工长，根据设计师的要求准备为一套设计风格独特的房子进行室内装修。
#
# 房子的客厅大小为 n x m，为保持极简的风格，需要使用尽可能少的 正方形 瓷砖来铺盖地面。
#
# 假设正方形瓷砖的规格不限，边长都是整数。
#
# 请你帮设计师计算一下，最少需要用到多少块方形瓷砖？
#
#
#
# 示例 1：
#
#
#
# 输入：n = 2, m = 3
# 输出：3
# 解释：3 块地砖就可以铺满卧室。
#      2 块 1x1 地砖
#      1 块 2x2 地砖
# 示例 2：
#
#
#
# 输入：n = 5, m = 8
# 输出：5
# 示例 3：
#
#
#
# 输入：n = 11, m = 13
# 输出：6
#

class Solution:
    def tilingRectangle(self, n: int, m: int) -> int:
        def dfs(x: int, y: int, cnt: int) -> None:
            nonlocal ans
            if cnt >= ans:
                return
            if x >= n:
                ans = cnt
                return

            # 检测下一行
            if y >= m:
                dfs(x + 1, 0, cnt)
                return
            # 如当前已经被覆盖，则直接尝试下一个位置
            if rect[x][y]:
                dfs(x, y + 1, cnt)
                return

            k = min(n - x, m - y)
            while k >= 1 and isAvailable(x, y, k):
                fillUp(x, y, k, True)
                # 跳过 k 个位置开始检测
                dfs(x, y + k, cnt + 1)
                fillUp(x, y, k, False)
                k -= 1

        def isAvailable(x: int, y: int, k: int) -> bool:
            for i in range(k):
                for j in range(k):
                    if rect[x + i][y + j] == True:
                        return False
            return True

        def fillUp(x: int, y: int, k: int, val: bool) -> None:
            for i in range(k):
                for j in range(k):
                    rect[x + i][y + j] = val

        ans = max(n, m)
        rect = [[False] * m for _ in range(n)]
        dfs(0, 0, 0)
        return ans


if __name__ == "__main__":
    n = 11
    m = 13
    test = Solution().tilingRectangle(n, m)
    print(test)
