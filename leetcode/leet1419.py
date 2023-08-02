import math
from typing import List

# 1419. 数青蛙
# 给你一个字符串 croakOfFrogs，它表示不同青蛙发出的蛙鸣声（字符串 "croak" ）的组合。由于同一时间可以有多只青蛙呱呱作响，所以 croakOfFrogs 中会混合多个 “croak” 。
#
# 请你返回模拟字符串中所有蛙鸣所需不同青蛙的最少数目。
#
# 要想发出蛙鸣 "croak"，青蛙必须 依序 输出 ‘c’, ’r’, ’o’, ’a’, ’k’ 这 5 个字母。如果没有输出全部五个字母，那么它就不会发出声音。如果字符串 croakOfFrogs 不是由若干有效的 "croak" 字符混合而成，请返回 -1 。
#
#
#
# 示例 1：
#
# 输入：croakOfFrogs = "croakcroak"
# 输出：1
# 解释：一只青蛙 “呱呱” 两次
# 示例 2：
#
# 输入：croakOfFrogs = "crcoakroak"
# 输出：2
# 解释：最少需要两只青蛙，“呱呱” 声用黑体标注
# 第一只青蛙 "crcoakroak"
# 第二只青蛙 "crcoakroak"
# 示例 3：
#
# 输入：croakOfFrogs = "croakcrook"
# 输出：-1
# 解释：给出的字符串不是 "croak" 的有效组合。
#

class Solution:
    def minNumberOfFrogs(self, croakOfFrogs: str) -> int:
        l = [0] * 4
        res = 0
        frogs = 0

        for x in croakOfFrogs:
            if x == "c":
                frogs += 1
                l[0] += 1
            elif x == "r":
                if l[0] == 0:
                    return -1
                else:
                    l[0] -= 1
                l[1] += 1
            elif x == "o":
                if l[1] == 0:
                    return -1
                else:
                    l[1] -= 1
                l[2] += 1
            elif x == "a":
                if l[2] == 0:
                    return -1
                else:
                    l[2] -= 1
                l[3] += 1
            elif x == "k":
                if l[3] == 0:
                    return -1
                else:
                    l[3] -= 1
                res = max(res, frogs)
                frogs -= 1
                # res = max(res, sum(l) + 1)
            else:
                return -1
        if max(l) == 0:
            return res
        else:
            return -1

if __name__ == "__main__":
    croakOfFrogs = "crocracokrakoak"

    test = Solution().minNumberOfFrogs(croakOfFrogs)
    print(test)
