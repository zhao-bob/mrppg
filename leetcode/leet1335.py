import math
from collections import deque, Counter
from itertools import pairwise
from typing import List


# 1335. 工作计划的最低难度
# 你需要制定一份 d 天的工作计划表。工作之间存在依赖，要想执行第 i 项工作，你必须完成全部 j 项工作（ 0 <= j < i）。
#
# 你每天 至少 需要完成一项任务。工作计划的总难度是这 d 天每一天的难度之和，而一天的工作难度是当天应该完成工作的最大难度。
#
# 给你一个整数数组 jobDifficulty 和一个整数 d，分别代表工作难度和需要计划的天数。第 i 项工作的难度是 jobDifficulty[i]。
#
# 返回整个工作计划的 最小难度 。如果无法制定工作计划，则返回 -1 。
#
#
#
# 示例 1：
#
#
#
# 输入：jobDifficulty = [6,5,4,3,2,1], d = 2
# 输出：7
# 解释：第一天，您可以完成前 5 项工作，总难度 = 6.
# 第二天，您可以完成最后一项工作，总难度 = 1.
# 计划表的难度 = 6 + 1 = 7
# 示例 2：
#
# 输入：jobDifficulty = [9,9,9], d = 4
# 输出：-1
# 解释：就算你每天完成一项工作，仍然有一天是空闲的，你无法制定一份能够满足既定工作时间的计划表。
# 示例 3：
#
# 输入：jobDifficulty = [1,1,1], d = 3
# 输出：3
# 解释：工作计划为每天一项工作，总难度为 3 。
# 示例 4：
#
# 输入：jobDifficulty = [7,1,7,1,7,1], d = 3
# 输出：15
# 示例 5：
#
# 输入：jobDifficulty = [11,111,22,222,33,333,44,444], d = 6
# 输出：843
#

class Solution:
    def minDifficulty(self, jobDifficulty: List[int], d: int) -> int:
        dp = [[[math.inf for _ in range(d)] for _ in range(len(jobDifficulty))] for _ in range(len(jobDifficulty))]

        for i in range(len(jobDifficulty)):
            dp[i][i][0] = jobDifficulty[i]

        for i in range(len(jobDifficulty) - 1):
            for j in range(i + 1, len(jobDifficulty)):
                dp[i][j][0] = max(dp[i][j - 1][0], dp[j][j][0])

        for l in range(1, d):
            for i in range(len(jobDifficulty) - l):
                for j in range(i + l, len(jobDifficulty)):
                    for k in range(i + l - 1, j):
                        dp[i][j][l] = min(dp[i][j][l], dp[i][k][l - 1] + dp[k + 1][j][0])
        return -1 if dp[0][-1][d - 1] == math.inf else dp[0][-1][d - 1]

    def minDifficulty1(self, jobDifficulty: List[int], d: int) -> int:
        dp = [[math.inf for _ in range(d)] for _ in range(len(jobDifficulty))]
        m = [[0 for _ in range(len(jobDifficulty))] for _ in range(len(jobDifficulty))]
        for i in range(len(jobDifficulty)):
            m[i][i] = jobDifficulty[i]
            for j in range(i + 1, len(jobDifficulty)):
                m[i][j] = max(m[i][j - 1], jobDifficulty[j])

        dp[0][0] = jobDifficulty[0]
        for i in range(1, len(jobDifficulty)):
            dp[i][0] = max(dp[i - 1][0], jobDifficulty[i])

        for l in range(1, d):
            for i in range(len(jobDifficulty)):
                for j in range(l - 1, i):
                    dp[i][l] = min(dp[i][l], dp[j][l - 1] + m[j + 1][i])
        return -1 if dp[-1][d - 1] == math.inf else dp[-1][d - 1]


if __name__ == "__main__":
    jobDifficulty = [1,1,1]
    d = 3
    test = Solution().minDifficulty1(jobDifficulty, d)
    print(test)
