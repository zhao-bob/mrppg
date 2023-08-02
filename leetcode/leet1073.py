import math
from collections import deque, Counter
from itertools import pairwise
from typing import List


# 1073. 负二进制数相加
# 给出基数为 -2 的两个数 arr1 和 arr2，返回两数相加的结果。
#
# 数字以 数组形式 给出：数组由若干 0 和 1 组成，按最高有效位到最低有效位的顺序排列。例如，arr = [1,1,0,1] 表示数字 (-2)^3 + (-2)^2 + (-2)^0 = -3。数组形式 中的数字 arr 也同样不含前导零：即 arr == [0] 或 arr[0] == 1。
#
# 返回相同表示形式的 arr1 和 arr2 相加的结果。两数的表示形式为：不含前导零、由若干 0 和 1 组成的数组。
#
#
#
# 示例 1：
#
# 输入：arr1 = [1,1,1,1,1], arr2 = [1,0,1]
# 输出：[1,0,0,0,0]
# 解释：arr1 表示 11，arr2 表示 5，输出表示 16 。
# 示例 2：
#
# 输入：arr1 = [0], arr2 = [0]
# 输出：[0]
# 示例 3：
#
# 输入：arr1 = [0], arr2 = [1]
# 输出：[1]
#

class Solution:
    def addNegabinary(self, arr1: List[int], arr2: List[int]) -> List[int]:
        l = max(len(arr1), len(arr2))
        res = [0] * (l + 2)
        c = 0

        for i in range(-1, -l - 1, -1):
            if i >= -len(arr1) and i >= -len(arr2):
                a = arr1[i] + arr2[i] - c
            else:
                if i < -len(arr1):
                    a = arr2[i] - c
                else:
                    a = arr1[i] - c
            res[i] = a % 2
            c = a // 2
        if c != 0:
            res[0] = 1
            res[1] = 1
        i = 0
        while res[i] == 0 and i < len(res) - 1:
            i += 1
        return res[i:]


if __name__ == "__main__":
    arr1 = [1,1,1,1,1]
    arr2 = [1,0,1]
    test = Solution().addNegabinary(arr1, arr2)
    print(test)
