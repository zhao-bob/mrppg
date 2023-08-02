import heapq
import math
from typing import List, Optional


# 1130. 叶值的最小代价生成树
# 给你一个正整数数组 arr，考虑所有满足以下条件的二叉树：
#
# 每个节点都有 0 个或是 2 个子节点。
# 数组 arr 中的值与树的中序遍历中每个叶节点的值一一对应。
# 每个非叶节点的值等于其左子树和右子树中叶节点的最大值的乘积。
# 在所有这样的二叉树中，返回每个非叶节点的值的最小可能总和。这个和的值是一个 32 位整数。
#
# 如果一个节点有 0 个子节点，那么该节点为叶节点。
#
#
#
# 示例 1：
#
#
# 输入：arr = [6,2,4]
# 输出：32
# 解释：有两种可能的树，第一种的非叶节点的总和为 36 ，第二种非叶节点的总和为 32 。
# 示例 2：
#
#
# 输入：arr = [4,11]
# 输出：44
#

class Solution:
    def mctFromLeafValues(self, arr: List[int]) -> int:
        dp = [[[0, 0] for _ in range(len(arr))] for _ in range(len(arr))]
        for i in range(len(arr)):
            dp[0][i][1] = arr[i]

        for k in range(1, len(arr)):
            for i in range(len(arr) - k):
                dp[k][i][0] = math.inf
                dp[k][i][1] = max(dp[k-1][i][1], arr[i+k])
                for j in range(k):
                    dp[k][i][0] = min(dp[k][i][0], dp[j][i][0] + dp[k-1-j][i+j+1][0] + dp[j][i][1]*dp[k-1-j][i+j+1][1])

        return dp[-1][0][0]



if __name__ == "__main__":
    arr = [6,2,4,1]
    test = Solution().mctFromLeafValues(arr)
    print(test)
