from collections import Counter
from typing import List


# 2379. 得到 K 个黑块的最少涂色次数

# 给你一个长度为 n 下标从 0 开始的字符串 blocks ，blocks[i] 要么是 'W' 要么是 'B' ，表示第 i 块的颜色。字符 'W' 和 'B' 分别表示白色和黑色。
#
# 给你一个整数 k ，表示想要 连续 黑色块的数目。
#
# 每一次操作中，你可以选择一个白色块将它 涂成 黑色块。
#
# 请你返回至少出现 一次 连续 k 个黑色块的 最少 操作次数。
#
#  
#
# 示例 1：
#
# 输入：blocks = "WBBWWBBWBW", k = 7
# 输出：3
# 解释：
# 一种得到 7 个连续黑色块的方法是把第 0 ，3 和 4 个块涂成黑色。
# 得到 blocks = "BBBBBBBWBW" 。
# 可以证明无法用少于 3 次操作得到 7 个连续的黑块。
# 所以我们返回 3 。
# 示例 2：
#
# 输入：blocks = "WBWBBBW", k = 2
# 输出：0
# 解释：
# 不需要任何操作，因为已经有 2 个连续的黑块。
# 所以我们返回 0 。
#
#

class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        res = 0
        left = 0
        right = 0
        black = 0
        while right < len(blocks):
            x = blocks[right]
            y = blocks[left]
            if right - left < k:
                if x == "B":
                    black += 1
                right += 1
            else:
                if x == "B" and y == "W":
                    black += 1
                elif x == "W" and y == "B":
                    black -= 1
                right += 1
                left += 1
            res = max(res, black)

        return k - res



if __name__ == "__main__":
    blocks = "WBWBBBW"
    k = 2
    test = Solution().minimumRecolors(blocks, k)
    print(test)
