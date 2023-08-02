import math
from typing import List


# 1090. 受标签影响的最大值
# 我们有一个 n 项的集合。给出两个整数数组 values 和 labels ，第 i 个元素的值和标签分别是 values[i] 和 labels[i]。还会给出两个整数 numWanted 和 useLimit 。
#
# 从 n 个元素中选择一个子集 s :
#
# 子集 s 的大小 小于或等于 numWanted 。
# s 中 最多 有相同标签的 useLimit 项。
# 一个子集的 分数 是该子集的值之和。
#
# 返回子集 s 的最大 分数 。
#
#
#
# 示例 1：
#
# 输入：values = [5,4,3,2,1], labels = [1,1,2,2,3], numWanted = 3, useLimit = 1
# 输出：9
# 解释：选出的子集是第一项，第三项和第五项。
# 示例 2：
#
# 输入：values = [5,4,3,2,1], labels = [1,3,3,3,2], numWanted = 3, useLimit = 2
# 输出：12
# 解释：选出的子集是第一项，第二项和第三项。
# 示例 3：
#
# 输入：values = [9,8,8,7,6], labels = [0,0,0,1,1], numWanted = 3, useLimit = 1
# 输出：16
# 解释：选出的子集是第一项和第四项。
#

class Solution:
    def largestValsFromLabels(self, values: List[int], labels: List[int], numWanted: int, useLimit: int) -> int:
        comb = [[values[i], labels[i]] for i in range(len(values))]
        res = 0
        comb.sort(key=lambda x: x[0], reverse=True)

        lc = {}
        i = numWanted
        k = 0
        while i > 0:
            while k < len(values):
                a = 0
                if comb[k][1] in lc:
                    a = lc[comb[k][1]]
                if a + 1 <= useLimit:
                    res += comb[k][0]
                    lc[comb[k][1]] = a + 1
                    k += 1
                    break
                k += 1
            i -= 1
        return res


if __name__ == "__main__":
    values = [5]
    labels = [1]
    numWanted = 3
    useLimit = 0

    test = Solution().largestValsFromLabels(values, labels, numWanted, useLimit)
    print(test)
