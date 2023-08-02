import math
from typing import List


# 1010. 总持续时间可被 60 整除的歌曲
# 在歌曲列表中，第 i 首歌曲的持续时间为 time[i] 秒。
#
# 返回其总持续时间（以秒为单位）可被 60 整除的歌曲对的数量。形式上，我们希望下标数字 i 和 j 满足  i < j 且有 (time[i] + time[j]) % 60 == 0。
#
#
#
# 示例 1：
#
# 输入：time = [30,20,150,100,40]
# 输出：3
# 解释：这三对的总持续时间可被 60 整除：
# (time[0] = 30, time[2] = 150): 总持续时间 180
# (time[1] = 20, time[3] = 100): 总持续时间 120
# (time[1] = 20, time[4] = 40): 总持续时间 60
# 示例 2：
#
# 输入：time = [60,60,60]
# 输出：3
# 解释：所有三对的总持续时间都是 120，可以被 60 整除。
#

class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        # l = [0] * 60
        # res = 0
        #
        # for x in time:
        #     l[x % 60] += 1
        #
        # for i in range(0, 31):
        #     if i == 0 or i == 30:
        #         if l[i] > 1:
        #             res += l[i] * (l[i] - 1) // 2
        #     elif l[i] != 0:
        #         res += l[i] * l[60 - i]
        m = {}
        res = 0
        for x in time:
            i = x % 60
            if i in m:
                m[i] += 1
            else:
                m[i] = 1
        for k in m.keys():
            if k == 0 or k == 30:
                if m[k] > 1:
                    res += m[k] * (m[k] - 1) // 2
            elif 60 - k in m and m[k] > 0 and m[60 - k] > 0:
                res += m[k] * m[60 - k]
                m[k] = 0
                m[60 - k] = 0
        return res


if __name__ == "__main__":
    time = [60,60,60]

    test = Solution().numPairsDivisibleBy60(time)
    print(test)
