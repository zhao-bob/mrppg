import math
from collections import deque
from itertools import pairwise
from typing import List


# 1015. 可被 K 整除的最小整数
# 给定正整数 k ，你需要找出可以被 k 整除的、仅包含数字 1 的最 小 正整数 n 的长度。
#
# 返回 n 的长度。如果不存在这样的 n ，就返回-1。
#
# 注意： n 不符合 64 位带符号整数。
#
#
#
# 示例 1：
#
# 输入：k = 1
# 输出：1
# 解释：最小的答案是 n = 1，其长度为 1。
# 示例 2：
#
# 输入：k = 2
# 输出：-1
# 解释：不存在可被 2 整除的正整数 n 。
# 示例 3：
#
# 输入：k = 3
# 输出：3
# 解释：最小的答案是 n = 111，其长度为 3。
#

class Solution:
    def smallestRepunitDivByK(self, k: int) -> int:
        i = len(str(k))
        s = int("1" * i)
        if s % k == 0:
            return i
        l = 0
        while l < k + 1:
            if s % k == 0:
                return i
            m = s % k
            s = m * 10 + 1
            i += 1
            l += 1
        return -1




if __name__ == "__main__":
    k = 19

    test = Solution().smallestRepunitDivByK(k)
    print(test)
