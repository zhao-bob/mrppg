from typing import List


# 1140. 石子游戏 II

# 爱丽丝和鲍勃继续他们的石子游戏。许多堆石子 排成一行，每堆都有正整数颗石子 piles[i]。游戏以谁手中的石子最多来决出胜负。
#
# 爱丽丝和鲍勃轮流进行，爱丽丝先开始。最初，M = 1。
#
# 在每个玩家的回合中，该玩家可以拿走剩下的 前 X 堆的所有石子，其中 1 <= X <= 2M。然后，令 M = max(M, X)。
#
# 游戏一直持续到所有石子都被拿走。
#
# 假设爱丽丝和鲍勃都发挥出最佳水平，返回爱丽丝可以得到的最大数量的石头。
#
# 示例 1：
#
# 输入：piles = [2,7,9,4,4]
# 输出：10
# 解释：如果一开始Alice取了一堆，Bob取了两堆，然后Alice再取两堆。爱丽丝可以得到2 + 4 + 4 = 10堆。如果Alice一开始拿走了两堆，那么Bob可以拿走剩下的三堆。在这种情况下，Alice得到2 + 7 = 9堆。返回10，因为它更大。
# 示例 2:
#
# 输入：piles = [1,2,3,4,5,100]
# 输出：104
#

class Solution:
    #
    # dp[i][j]表示剩余[i : len - 1]堆时，M = j的情况下，先取的人能获得的最多石子数
    #
    # i + 2M >= len, dp[i][M] = sum[i : len - 1], 剩下的堆数能够直接全部取走，那么最优的情况就是剩下的石子总和
    # i + 2M < len, dp[i][M] = max(dp[i][M], sum[i : len - 1] - dp[i + x][max(M, x)]), 其中 1 <= x <=
    # 2M，剩下的堆数不能全部取走，那么最优情况就是让下一个人取的更少。对于我所有的x取值，下一个人从x开始取起，M变为max(M, x)，所以下一个人能取dp[i + x][max(M, x)]，我最多能取sum[i :
    # len - 1] - dp[i + x][max(M, x)]。
    #
    def stoneGameII(self, piles: List[int]) -> int:
        length = len(piles)
        dp = [[0 for i in range(length)] for j in range(length)]
        s = 0

        for i in range(length, 0, -1):
            s += piles[i - 1]
            for M in range(length, 0, -1):
                if i - 1 + 2 * M >= length:
                    dp[i - 1][M - 1] = s
                else:
                    for x in range(1, 2 * M + 1):
                        if dp[i - 1][M - 1] < s - dp[i - 1 + x][max(M, x) - 1]:
                            dp[i - 1][M - 1] = s - dp[i - 1 + x][max(M, x) - 1]
        print(dp)
        return dp[0][0]


if __name__ == "__main__":
    piles = [1,2,3,4,5,100]
    test = Solution().stoneGameII(piles)
    print(test)
