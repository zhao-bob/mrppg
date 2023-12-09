from typing import List


# 1234. 替换子串得到平衡字符串

# 有一个只含有 'Q', 'W', 'E', 'R' 四种字符，且长度为 n 的字符串。
#
# 假如在该字符串中，这四个字符都恰好出现 n/4 次，那么它就是一个「平衡字符串」。
#
#  
#
# 给你一个这样的字符串 s，请通过「替换一个子串」的方式，使原字符串 s 变成一个「平衡字符串」。
#
# 你可以用和「待替换子串」长度相同的 任何 其他字符串来完成替换。
#
# 请返回待替换子串的最小可能长度。
#
# 如果原字符串自身就是一个平衡字符串，则返回 0。
#
#  
#
# 示例 1：
#
# 输入：s = "QWER"
# 输出：0
# 解释：s 已经是平衡的了。
# 示例 2：
#
# 输入：s = "QQWE"
# 输出：1
# 解释：我们需要把一个 'Q' 替换成 'R'，这样得到的 "RQWE" (或 "QRWE") 是平衡的。
# 示例 3：
#
# 输入：s = "QQQW"
# 输出：2
# 解释：我们可以把前面的 "QQ" 替换成 "ER"。
# 示例 4：
#
# 输入：s = "QQQQ"
# 输出：3
# 解释：我们可以替换后 3 个 'Q'，使 s = "QWER"。
#


class Solution:
    def balancedString(self, s: str) -> int:
        length = len(s)
        if length % 4 != 0:
            return -1
        countMap = {}
        for i in range(length):
            if s[i] in countMap:
                countMap[s[i]] += 1
            else:
                countMap[s[i]] = 1
        minSub = 0
        for k in countMap:
            if countMap[k] > length / 4:
                minSub += countMap[k] - length / 4

        if minSub == 0:
            return 0
        else:
            left = 0
            right = 0
            res = length
            while right < length:
                countMap[s[right]] -= 1
                c = self.check(countMap, length / 4)
                if c:
                    res = min(res, right - left + 1)
                    while left <= right:
                        countMap[s[left]] += 1
                        if self.check(countMap, length / 4):
                            res = min(res, right - left)
                            left += 1
                        else:
                            left += 1
                            break
                right += 1
            return res

    def check(self, countMap, n):
        res = True
        for k in countMap:
            if countMap[k] > n:
                res = False
        return res


if __name__ == "__main__":
    s = "WWEQERQWQWWRWWERQWEQ"
    test = Solution().balancedString(s)
    print(test)
