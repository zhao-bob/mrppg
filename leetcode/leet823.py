import collections
import heapq
import math
from bisect import bisect_right
from collections import Counter, deque
from functools import cache
from itertools import product
from typing import List, Optional


# 823. 带因子的二叉树
# 中等
# 115
# 相关企业
# 给出一个含有不重复整数元素的数组 arr ，每个整数 arr[i] 均大于 1。
#
# 用这些整数来构建二叉树，每个整数可以使用任意次数。其中：每个非叶结点的值应等于它的两个子结点的值的乘积。
#
# 满足条件的二叉树一共有多少个？答案可能很大，返回 对 109 + 7 取余 的结果。
#
#
#
# 示例 1:
#
# 输入: arr = [2, 4]
# 输出: 3
# 解释: 可以得到这些二叉树: [2], [4], [4, 2, 2]
# 示例 2:
#
# 输入: arr = [2, 4, 5, 10]
# 输出: 7
# 解释: 可以得到这些二叉树: [2], [4], [5], [10], [4, 2, 2], [10, 2, 5], [10, 5, 2].

class Solution:
    def numFactoredBinaryTrees(self, arr: List[int]) -> int:
        arr.sort()
        dp = [1] * len(arr)
        s = {arr[i]: i for i in range(len(arr))}
        for i in range(1, len(arr)):
            for j in range(i):
                if arr[i] % arr[j] == 0 and arr[i] // arr[j] in s:
                    dp[i] += (dp[j] * dp[s[arr[i] // arr[j]]])
        return sum(dp) % (10**9 + 7)



if __name__ == "__main__":
    arr = [2, 4, 5, 10]

    test = Solution().numFactoredBinaryTrees(arr)

    print(test)
