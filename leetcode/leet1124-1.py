from typing import List


# 1124. 表现良好的最长时间段

# 给你一份工作时间表 hours，上面记录着某一位员工每天的工作小时数。
#
# 我们认为当员工一天中的工作小时数大于 8 小时的时候，那么这一天就是「劳累的一天」。
#
# 所谓「表现良好的时间段」，意味在这段时间内，「劳累的天数」是严格 大于「不劳累的天数」。
#
# 请你返回「表现良好时间段」的最大长度。
#
#  
#
# 示例 1：
#
# 输入：hours = [9,9,6,0,6,6,9]
# 输出：3
# 解释：最长的表现良好时间段是 [9,9,6]。
# 示例 2：
#
# 输入：hours = [6,6,6]
# 输出：0
#


class Solution:
    def longestWPI(self, hours: List[int]) -> int:
        h = [1 if i > 8 else -1 for i in hours]
        sh = [0] * len(hours)
        s = 0
        for i in range(len(h)):
            s += h[i]
            sh[i] = s
        seen = {}

        res = 0
        for i in range(len(sh)):
            if sh[i] > 0:
                res = max(res, i + 1)
            else:
                if sh[i] - 1 in seen:
                    res = max(res, i - seen[sh[i] - 1])
                if sh[i] not in seen:
                    seen[sh[i]] = i

        return res


if __name__ == "__main__":
    #
    hours = [9,9,6,0,6,6,9,9]
    h = [int(x > 8) for x in hours]
    print(h)
    test = Solution().longestWPI(hours)
    print(test)
