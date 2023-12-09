from typing import List


# 496. 下一个更大元素 I
# 简单
# 1.1K
# 相关企业
# nums1 中数字 x 的 下一个更大元素 是指 x 在 nums2 中对应位置 右侧 的 第一个 比 x 大的元素。
#
# 给你两个 没有重复元素 的数组 nums1 和 nums2 ，下标从 0 开始计数，其中nums1 是 nums2 的子集。
#
# 对于每个 0 <= i < nums1.length ，找出满足 nums1[i] == nums2[j] 的下标 j ，并且在 nums2 确定 nums2[j] 的 下一个更大元素 。如果不存在下一个更大元素，那么本次查询的答案是 -1 。
#
# 返回一个长度为 nums1.length 的数组 ans 作为答案，满足 ans[i] 是如上所述的 下一个更大元素 。
#
#
#
# 示例 1：
#
# 输入：nums1 = [4,1,2], nums2 = [1,3,4,2].
# 输出：[-1,3,-1]
# 解释：nums1 中每个值的下一个更大元素如下所述：
# - 4 ，用加粗斜体标识，nums2 = [1,3,4,2]。不存在下一个更大元素，所以答案是 -1 。
# - 1 ，用加粗斜体标识，nums2 = [1,3,4,2]。下一个更大元素是 3 。
# - 2 ，用加粗斜体标识，nums2 = [1,3,4,2]。不存在下一个更大元素，所以答案是 -1 。
# 示例 2：
#
# 输入：nums1 = [2,4], nums2 = [1,2,3,4].
# 输出：[3,-1]
# 解释：nums1 中每个值的下一个更大元素如下所述：
# - 2 ，用加粗斜体标识，nums2 = [1,2,3,4]。下一个更大元素是 3 。
# - 4 ，用加粗斜体标识，nums2 = [1,2,3,4]。不存在下一个更大元素，所以答案是 -1 。
#


class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        m = {}
        for i in range(len(nums1)):
            m[nums1[i]] = i

        stk = [-1]
        res = [-1] * len(nums1)
        for i in range(len(nums2) - 1, -1, -1):
            a = nums2[i]
            while stk:
                b = stk[-1]
                if b == -1 or a > nums2[b]:
                    stk.pop()
                else:
                    if a in m:
                        res[m[a]] = nums2[b]
                    break
            stk.append(i)
        return res


if __name__ == "__main__":
    nums1 = [2,4]
    nums2 = [1,2,3,4]
    test = Solution().nextGreaterElement(nums1, nums2)
    print(test)
