import math
from typing import List


# 2423. 删除字符使频率相同
# 给你一个下标从 0 开始的字符串 word ，字符串只包含小写英文字母。你需要选择 一个 下标并 删除 下标处的字符，使得 word 中剩余每个字母出现 频率 相同。
#
# 如果删除一个字母后，word 中剩余所有字母的出现频率都相同，那么返回 true ，否则返回 false 。
#
# 注意：
#
# 字母 x 的 频率 是这个字母在字符串中出现的次数。
# 你 必须 恰好删除一个字母，不能一个字母都不删除。
#
#
# 示例 1：
#
# 输入：word = "abcc"
# 输出：true
# 解释：选择下标 3 并删除该字母，word 变成 "abc" 且每个字母出现频率都为 1 。
# 示例 2：
#
# 输入：word = "aazz"
# 输出：false
# 解释：我们必须删除一个字母，所以要么 "a" 的频率变为 1 且 "z" 的频率为 2 ，要么两个字母频率反过来。所以不可能让剩余所有字母出现频率相同。
#

class Solution:
    def equalFrequency(self, word: str) -> bool:
        m = {}
        for x in word:
            if x in m:
                m[x] += 1
            else:
                m[x] = 1
        l = {}
        for x in m.keys():
            if m[x] in l:
                l[m[x]] += 1
            else:
                l[m[x]] = 1
        if len(l) > 2:
            return False
        if len(l) == 2:
            a = list(l.keys())[0]
            b = list(l.keys())[1]
            if (l[a] == 1 and (a == 1 or a - b == 1)) or (l[b] == 1 and (b == 1 or b - a == 1)):
                return True
        elif len(l) == 1:
            a = list(l.keys())[0]
            if a == 1 or l[a] == 1:
                return True
        return False



if __name__ == "__main__":
    word = "aaaabbbbccc"

    test = Solution().equalFrequency(word)
    print(test)
