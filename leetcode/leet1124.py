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
        h = [x > 8 for x in hours]
        dp = [0] * (len(hours) + 1)
        diff = [0] * (len(hours) + 1)
        for i in range(len(h)):
            if h[i]:
                dp[i + 1] = dp[i] + 1
                if i + 1 - 2 * dp[i + 1] >= 0:
                    if dp[i + 2 - 2 * dp[i + 1]] > 0:
                        dp[i + 1] = dp[i + 1] + dp[i + 2 - 2 * dp[i + 1]]
                        diff[i + 1] = 1 + diff[i + 2 - 2 * dp[i + 1]]
                    else:
                        a = h[i + 1 - 2 * dp[i + 1]]
                        if not a:
                            a = -1
                        diff[i + 1] = diff[i] + a + 1
                else:
                    diff[i + 1] = diff[i] + 1
            else:
                dp[i + 1] = dp[i]
                if dp[i + 1] == 0:
                    diff[i + 1] = 0
                else:
                    diff[i + 1] = diff[i] - 1
                    if diff[i + 1] < 0:
                        if i - 2 * dp[i + 1] >= 0:
                            if h[i - 2 * dp[i + 1]]:
                                k = i - 2 * dp[i + 1]
                                a = -1
                                d = dp[i + 1]
                                while k < i and a < 0 < d:
                                    if h[k]:
                                        a -= 1
                                        d -= 1
                                    else:
                                        a += 1
                                    k += 1
                                dp[i + 1] = d
                                diff[i + 1] = 0
                            else:
                                diff[i + 1] = 0

        return min(max(0, 2 * max(dp) - 1), len(h))

    def longestWPI1(self, hours: List[int]) -> int:
        n = len(hours)
        s = [0] * (n + 1)  # 前缀和
        st = [0]  # s[0]
        for j, h in enumerate(hours, 1):
            s[j] = s[j - 1] + (1 if h > 8 else -1)
            if s[j] < s[st[-1]]:
                st.append(j)  # 感兴趣的 j
        ans = 0
        for i in range(n, 0, -1):
            while st and s[i] > s[st[-1]]:
                ans = max(ans, i - st.pop())  # [st[-1],i) 可能是最长子数组
        return ans


if __name__ == "__main__":
    #
    hours = [9,9,9,6,6,6,6,9,9,9,9]
    h = [int(x > 8) for x in hours]
    print(h)
    test = Solution().longestWPI1(hours)
    print(test)
