import math
from typing import List


# 2418. 按身高排序
# 给你一个字符串数组 names ，和一个由 互不相同 的正整数组成的数组 heights 。两个数组的长度均为 n 。
#
# 对于每个下标 i，names[i] 和 heights[i] 表示第 i 个人的名字和身高。
#
# 请按身高 降序 顺序返回对应的名字数组 names 。
#
#
#
# 示例 1：
#
# 输入：names = ["Mary","John","Emma"], heights = [180,165,170]
# 输出：["Mary","Emma","John"]
# 解释：Mary 最高，接着是 Emma 和 John 。
# 示例 2：
#
# 输入：names = ["Alice","Bob","Bob"], heights = [155,185,150]
# 输出：["Bob","Alice","Bob"]
# 解释：第一个 Bob 最高，然后是 Alice 和第二个 Bob 。
#

class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        m = [[names[i], heights[i]] for i in range(len(names))]

        return [k[0] for k in sorted(m, key=lambda x:x[1], reverse=True)]


if __name__ == "__main__":
    names = ["Alice","Bob","Bob"]
    heights = [155,185,150]

    test = Solution().sortPeople(names, heights)
    print(test)
