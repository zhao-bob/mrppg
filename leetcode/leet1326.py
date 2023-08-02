from typing import List


# 1326. 灌溉花园的最少水龙头数目

# 在 x 轴上有一个一维的花园。花园长度为 n，从点 0 开始，到点 n 结束。
#
# 花园里总共有 n + 1 个水龙头，分别位于 [0, 1, ..., n] 。
#
# 给你一个整数 n 和一个长度为 n + 1 的整数数组 ranges ，其中 ranges[i] （下标从 0 开始）表示：如果打开点 i 处的水龙头，可以灌溉的区域为 [i -  ranges[i], i + ranges[i]] 。
#
# 请你返回可以灌溉整个花园的 最少水龙头数目 。如果花园始终存在无法灌溉到的地方，请你返回 -1 。
#
# 示例 1：
# 输入：n = 5, ranges = [3,4,1,1,0,0]
# 输出：1
# 解释：
# 点 0 处的水龙头可以灌溉区间 [-3,3]
# 点 1 处的水龙头可以灌溉区间 [-3,5]
# 点 2 处的水龙头可以灌溉区间 [1,3]
# 点 3 处的水龙头可以灌溉区间 [2,4]
# 点 4 处的水龙头可以灌溉区间 [4,4]
# 点 5 处的水龙头可以灌溉区间 [5,5]
# 只需要打开点 1 处的水龙头即可灌溉整个花园 [0,5] 。
#
# 示例 2：
#
# 输入：n = 3, ranges = [0,0,0,0]
# 输出：-1
# 解释：即使打开所有水龙头，你也无法灌溉整个花园。


class Solution:
    def minTaps(self, n: int, ranges: List[int]) -> int:
        cover = [[[-1, 0], [-1, 0]]]
        for i in range(n + 1):
            if i - ranges[i] <= 0 and i + ranges[i] >= n:
                return 1
            else:
                minum = [[0, -1], [0, -1]]
                left = i - ranges[i]
                if i - ranges[i] < 0:
                    left = 0
                elif i -ranges[i] > 0 and ranges[i] != 0:
                    left = i -ranges[i] + 1
                right = i + ranges[i]
                if i == 0:
                    minum = [[right, 1], [right, 1]]
                while left <= i:
                    c = []
                    if cover[left][0][1] > -1:
                        if cover[left][0][0] >= i:
                            c = cover[left][0]
                        else:
                            if i != right:
                                c = [right, cover[left][0][1] + 1]
                            else:
                                if cover[left][1][0] >= i:
                                    c = cover[left][1]
                                else:
                                    c = minum[0]
                        if minum[0][1] == -1:
                            minum[0] = c
                        elif c[1] < minum[0][1]:
                            minum[0] = c
                        elif c[1] == minum[0][1] and c[0] > minum[0][0]:
                            minum[0] = c
                    if cover[left][1][1] > -1:
                        if cover[left][1][0] >= right:
                            c = cover[left][1]
                        # elif cover[left][1][0] >= i:
                        #     c = [right, cover[left][1][1]]
                        #     if c[1] <= minum[0][1]:
                        #         minum[0] = c
                        else:
                            if i != right:
                                c = [right, cover[left][1][1] + 1]
                            else:
                                c = minum[1]
                        if minum[1][1] == -1:
                            minum[1] = c
                        elif c[0] > minum[1][0]:
                            minum[1] = c
                        if minum[1][0] <= minum[0][0]:
                            minum[1] = minum[0]
                    left += 1
                cover.append(minum)
        return cover[n + 1][0][1]


if __name__ == "__main__":
    n = 3
    ranges = [0,0,0,0]
    test = Solution().minTaps(n, ranges)
    print(test)
