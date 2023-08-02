import math
from functools import lru_cache
from typing import List


# 1053. 交换一次的先前排列
# 给你一个正整数数组 arr（可能存在重复的元素），请你返回可在 一次交换（交换两数字 arr[i] 和 arr[j] 的位置）后得到的、按字典序排列小于 arr 的最大排列。
#
# 如果无法这么操作，就请返回原数组。
#
#
#
# 示例 1：
#
# 输入：arr = [3,2,1]
# 输出：[3,1,2]
# 解释：交换 2 和 1
# 示例 2：
#
# 输入：arr = [1,1,5]
# 输出：[1,1,5]
# 解释：已经是最小排列
# 示例 3：
#
# 输入：arr = [1,9,4,6,7]
# 输出：[1,7,4,6,9]
# 解释：交换 9 和 7
#

class Solution:
    def prevPermOpt1(self, arr: List[int]) -> List[int]:
        begin = 0
        end = 0
        for i in range(1, len(arr)):
            if arr[i] > arr[i - 1]:
                if arr[begin] > arr[i]:
                    end = i
            elif arr[i] < arr[i - 1]:
                begin = i - 1
                end = i

        if begin != end:
            arr[begin], arr[end] = arr[end], arr[begin]

        return arr

    def prevPermOpt2(self, arr: List[int]) -> List[int]:
        n = len(arr)
        for i in range(n - 2, -1, -1):
            if arr[i] > arr[i + 1]:
                j = n - 1
                while arr[j] >= arr[i] or arr[j] == arr[j - 1]:
                    j -= 1
                arr[i], arr[j] = arr[j], arr[i]
                break
        return arr


if __name__ == "__main__":
    arr = [6,1,5,9,1,1,9,7,7,9,7,6,2,7,3,4,5,1,7,6,3,5,3,1,4,7,1,1,8,8,9,1,9,5,1,6,5,4,7,3,2,7,4,9,7,6,2,5,7,4,3,7,5,5,4,4,2,1,3,1,6,4,8,7,5,9,3,1,4,4,7,5,3,7,2,4,4,8,5,4,8,1,1,3,4,3,5,4,8,1,5,4,9,8,4,5,3,1,1,3]

    test = Solution().prevPermOpt2(arr)
    print(test)
