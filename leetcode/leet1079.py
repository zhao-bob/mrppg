import math
from collections import deque, Counter
from itertools import pairwise
from typing import List


# 1079. 活字印刷
# 你有一套活字字模 tiles，其中每个字模上都刻有一个字母 tiles[i]。返回你可以印出的非空字母序列的数目。
#
# 注意：本题中，每个活字字模只能使用一次。
#
#
#
# 示例 1：
#
# 输入："AAB"
# 输出：8
# 解释：可能的序列为 "A", "B", "AA", "AB", "BA", "AAB", "ABA", "BAA"。
# 示例 2：
#
# 输入："AAABBC"
# 输出：188
# 示例 3：
#
# 输入："V"
# 输出：1
#

class Solution:
    def numTilePossibilities(self, tiles: str) -> int:
        s = {tiles[0]}
        for i in range(1, len(tiles)):
            t = s.copy()
            for x in s:
                for j in range(len(x) + 1):
                    n = x[0:j] + tiles[i] + x[j:]
                    t.add(n)
            t.add(tiles[i])
            s = t
        return len(s)


if __name__ == "__main__":
    tiles = "V"
    test = Solution().numTilePossibilities(tiles)
    print(test)
