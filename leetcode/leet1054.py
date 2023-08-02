import math
from collections import deque, Counter
from itertools import pairwise
from typing import List


# 1054. 距离相等的条形码
# 在一个仓库里，有一排条形码，其中第 i 个条形码为 barcodes[i]。
#
# 请你重新排列这些条形码，使其中任意两个相邻的条形码不能相等。 你可以返回任何满足该要求的答案，此题保证存在答案。
#
#
#
# 示例 1：
#
# 输入：barcodes = [1,1,1,2,2,2]
# 输出：[2,1,2,1,2,1]
# 示例 2：
#
# 输入：barcodes = [1,1,1,1,2,2,3,3]
# 输出：[1,3,1,3,2,1,2,1]
#

class Solution:
    def rearrangeBarcodes(self, barcodes: List[int]) -> List[int]:
        mb = {}
        for x in barcodes:
            if x in mb:
                mb[x] += 1
            else:
                mb[x] = 1
        smb = sorted(mb.items(), key=lambda x: x[1], reverse=True)
        res = [0] * len(barcodes)
        s = 0
        gap = len(barcodes) // smb[0][1]
        if gap == 1:
            gap = 2
        for i in range(len(smb)):
            while res[s] > 0:
                s += 1
            for j in range(smb[i][1]):
                if s + j * gap < gap * smb[0][1]:
                    res[s + j * gap] = smb[i][0]
                else:
                    k = j * 2 + 1
                    res = res[0: k] + [smb[i][0]] + res[k:len(res) - 1]

        return res

    def rearrangeBarcodes1(self, barcodes: List[int]) -> List[int]:
        cnt = Counter(barcodes)
        barcodes.sort(key=lambda x: (-cnt[x], x))
        n = len(barcodes)
        ans = [0] * len(barcodes)
        ans[::2] = barcodes[: (n + 1) // 2]
        ans[1::2] = barcodes[(n + 1) // 2:]
        return ans

    def rearrangeBarcodes2(self, barcodes: List[int]) -> List[int]:
        mb = {}
        mc = 0
        mx = 0
        for x in barcodes:
            if x in mb:
                mb[x] += 1
                if mb[x] > mc:
                    mx = x
                    mc = mb[x]
            else:
                mb[x] = 1
                if mb[x] > mc:
                    mx = x
                    mc = mb[x]
        res = [0] * len(barcodes)
        s = 0

        for j in range(mb[mx]):
            res[s] = mx
            s += 2
        mb.pop(mx)

        for x in mb:
            k = mb[x]
            if s + 2 * k < len(barcodes):
                for j in range(mb[x]):
                    res[s] = x
                    s += 2
                mb[x] = 0
            else:
                while s < len(barcodes):
                    res[s] = x
                    s += 2
                    mb[x] -= 1
                break
        s = 1
        for x in mb:
            for j in range(mb[x]):
                res[s] = x
                s += 2
        return res


if __name__ == "__main__":
    barcodes = [51,83,51,40,51,40,51,40,83,40,83,83,51,40,40,51,51,51,40,40,40,83,51,51,40,51,51,40,40,51,51,40,51,51,51,40,83,40,40,83,51,51,51,40,40,40,51,51,83,83,40,51,51,40,40,40,51,40,83,40,83,40,83,40,51,51,40,51,51,51,51,40,51,83,51,83,51,51,40,51,40,51,40,51,40,40,51,51,51,40,51,83,51,51,51,40,51,51,40,40]
    test = Solution().rearrangeBarcodes2(barcodes)
    print(test)
