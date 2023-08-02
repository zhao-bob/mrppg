from typing import List


# 1144. 递减元素使数组呈锯齿状

# 给你一个整数数组 nums，每次 操作 会从中选择一个元素并 将该元素的值减少 1。
#
# 如果符合下列情况之一，则数组 A 就是 锯齿数组：
#
# 每个偶数索引对应的元素都大于相邻的元素，即 A[0] > A[1] < A[2] > A[3] < A[4] > ...
# 或者，每个奇数索引对应的元素都大于相邻的元素，即 A[0] < A[1] > A[2] < A[3] > A[4] < ...
# 返回将数组 nums 转换为锯齿数组所需的最小操作次数。
#
#  
#
# 示例 1：
#
# 输入：nums = [1,2,3]
# 输出：2
# 解释：我们可以把 2 递减到 0，或把 3 递减到 1。
# 示例 2：
#
# 输入：nums = [9,6,1,6,2]
# 输出：4
#


class Solution:
    def movesToMakeZigzag(self, nums: List[int]) -> int:
        length = len(nums)
        up = 0
        down = 0
        if length <= 2:
            return 0
        diff = [0] * (length - 1)
        tnums = nums.copy()
        for i in range(length - 1):
            diff[i] = tnums[i + 1] - tnums[i]
            if diff[i] > 0:
                if i % 2 == 0:
                    down += (diff[i] + 1)
                    tnums[i + 1] = tnums[i + 1] - (diff[i] + 1)
            elif diff[i] < 0:
                if i % 2 == 1:
                    down += (1 - diff[i])
            else:
                if i % 2 == 0:
                    tnums[i + 1] -= 1
                down += 1

        tnums = nums.copy()
        for i in range(length - 1):
            diff[i] = tnums[i + 1] - tnums[i]
            if diff[i] > 0:
                if i % 2 == 1:
                    up += (diff[i] + 1)
                    tnums[i + 1] = tnums[i + 1] - (diff[i] + 1)
            elif diff[i] < 0:
                if i % 2 == 0:
                    up += (1 - diff[i])
            else:
                if i % 2 == 1:
                    tnums[i + 1] -= 1
                up += 1
        return min(up, down)


if __name__ == "__main__":
    #
    nums = [7,4,8,9,7,7,5]
    test = Solution().movesToMakeZigzag(nums)
    print(test)
