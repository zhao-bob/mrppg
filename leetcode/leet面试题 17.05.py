from typing import List


# 面试题 17.05.  字母与数字

# 给定一个放有字母和数字的数组，找到最长的子数组，且包含的字母和数字的个数相同。
#
# 返回该子数组，若存在多个最长子数组，返回左端点下标值最小的子数组。若不存在这样的数组，返回一个空数组。
#
# 示例 1:
#
# 输入: ["A","1","B","C","D","2","3","4","E","5","F","G","6","7","H","I","J","K","L","M"]
#
# 输出: ["A","1","B","C","D","2","3","4","E","5","F","G","6","7"]
# 示例 2:
#
# 输入: ["A","A"]
#
# 输出: []
#

class Solution:
    def findLongestSubarray(self, array: List[str]) -> List[str]:
        diff = {}
        s = [0] * (len(array) + 1)
        for i in range(len(array)):
            if array[i].isnumeric():
                s[i + 1] = s[i] + 1
            else:
                s[i + 1] = s[i] - 1

        left = 0
        right = 0
        pair = 0
        for i in range(len(s)):
            if s[i] in diff:
                if i - diff[s[i]] > pair:
                    left = diff[s[i]]
                    right = i
                    pair = i - diff[s[i]]
            else:
                diff[s[i]] = i
        return array[left:right] if pair > 0 else []


if __name__ == "__main__":
    array = ["A","A"]
    test = Solution().findLongestSubarray(array)
    print(test)
