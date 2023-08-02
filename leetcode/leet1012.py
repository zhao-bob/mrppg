import math
from typing import List


# 1012. 至少有 1 位重复的数字
# 给定正整数 n，返回在 [1, n] 范围内具有 至少 1 位 重复数字的正整数的个数。
#
#
#
# 示例 1：
#
# 输入：n = 20
# 输出：1
# 解释：具有至少 1 位重复数字的正数（<= 20）只有 11 。
# 示例 2：
#
# 输入：n = 100
# 输出：10
# 解释：具有至少 1 位重复数字的正数（<= 100）有 11，22，33，44，55，66，77，88，99 和 100 。
# 示例 3：
#
# 输入：n = 1000
# 输出：262
#

class Solution:
    def numDupDigitsAtMostN(self, n: int) -> int:
        limit, s = list(map(int, str(n + 1))), set()
        k, res = len(limit), sum(9 * math.perm(9, i) for i in range(len(limit) - 1))
        for i, x in enumerate(limit):
            for y in range(i == 0, x):
                if y not in s:
                    res += math.perm(9 - i, k - i - 1)
            if x in s:
                break
            s.add(x)
        return n - res

    def numDupDigitsAtMostN1(self, n: int) -> int:
        r = n
        l = []
        c = [0]
        while r > 0:
            d = r % 10
            count = 0
            for i in range(d):
                k = len(l) - 1
                if k == 0 and i != 0:
                    count += 1
                else:
                    if i == 0:
                        if k == 1:
                            count = 9
                            c.append(count)
                        else:
                            count += c[len(c) - 1]
                    else:
                        count += c[len(c) - 1]
                        for j in range(1, len(l)):
                            count += (int(math.pow(10, k)) - 1)
            else:
                if len(l) > 1:
                    count += 1
                for i in range(len(l)):
                    if d == l[i]:
                        k = 0
                        for j in range(len(l)):
                            if j != i:
                                count += ((l[i] - 1) % 10) * pow(10, k)
                                k += 1
                count += c[len(c) - 1]
            l.append(r % 10)
            r = r // 10
        return c[len(c) - 1]


if __name__ == "__main__":
    n = 98
    test = Solution().numDupDigitsAtMostN(n)
    print(test)
