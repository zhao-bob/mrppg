import math
from collections import deque
from itertools import pairwise
from typing import List


# 2437. 有效时间的数目
# 给你一个长度为 5 的字符串 time ，表示一个电子时钟当前的时间，格式为 "hh:mm" 。最早 可能的时间是 "00:00" ，最晚 可能的时间是 "23:59" 。
#
# 在字符串 time 中，被字符 ? 替换掉的数位是 未知的 ，被替换的数字可能是 0 到 9 中的任何一个。
#
# 请你返回一个整数 answer ，将每一个 ? 都用 0 到 9 中一个数字替换后，可以得到的有效时间的数目。
#
#
#
# 示例 1：
#
# 输入：time = "?5:00"
# 输出：2
# 解释：我们可以将 ? 替换成 0 或 1 ，得到 "05:00" 或者 "15:00" 。注意我们不能替换成 2 ，因为时间 "25:00" 是无效时间。所以我们有两个选择。
# 示例 2：
#
# 输入：time = "0?:0?"
# 输出：100
# 解释：两个 ? 都可以被 0 到 9 之间的任意数字替换，所以我们总共有 100 种选择。
# 示例 3：
#
# 输入：time = "??:??"
# 输出：1440
# 解释：小时总共有 24 种选择，分钟总共有 60 种选择。所以总共有 24 * 60 = 1440 种选择。
#

class Solution:
    def countTime(self, time: str) -> int:
        if "?" not in time:
            return 1
        [h, m] = time.split(":")
        ht = 0
        if h == "??":
            ht = 24
        else:
            if "?" not in h:
                ht = 1
            elif h.index("?") == 0:
                for i in range(3):
                    if int(str(i) + h[1]) < 24:
                        ht += 1
            else:
                for i in range(10):
                    if int(h[0] + str(i)) < 24:
                        ht += 1
        mt = 0
        if m == "??":
            mt = 60
        else:
            if "?" not in m:
                mt = 1
            elif m.index("?") == 0:
                for i in range(6):
                    if int(str(i) + m[1]) < 60:
                        mt += 1
            else:
                for i in range(10):
                    if int(m[0] + str(i)) < 60:
                        mt += 1

        return ht * mt


if __name__ == "__main__":
    time = "2?:00"

    test = Solution().countTime(time)
    print(test)
