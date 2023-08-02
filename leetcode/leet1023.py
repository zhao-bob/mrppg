import math
from functools import lru_cache
from typing import List, Optional


# 1023. 驼峰式匹配
# 如果我们可以将小写字母插入模式串 pattern 得到待查询项 query，那么待查询项与给定模式串匹配。（我们可以在任何位置插入每个字符，也可以插入 0 个字符。）
#
# 给定待查询列表 queries，和模式串 pattern，返回由布尔值组成的答案列表 answer。只有在待查项 queries[i] 与模式串 pattern 匹配时， answer[i] 才为 true，否则为 false。
#
#
#
# 示例 1：
#
# 输入：queries = ["FooBar","FooBarTest","FootBall","FrameBuffer","ForceFeedBack"], pattern = "FB"
# 输出：[true,false,true,true,false]
# 示例：
# "FooBar" 可以这样生成："F" + "oo" + "B" + "ar"。
# "FootBall" 可以这样生成："F" + "oot" + "B" + "all".
# "FrameBuffer" 可以这样生成："F" + "rame" + "B" + "uffer".
# 示例 2：
#
# 输入：queries = ["FooBar","FooBarTest","FootBall","FrameBuffer","ForceFeedBack"], pattern = "FoBa"
# 输出：[true,false,true,false,false]
# 解释：
# "FooBar" 可以这样生成："Fo" + "o" + "Ba" + "r".
# "FootBall" 可以这样生成："Fo" + "ot" + "Ba" + "ll".
# 示例 3：
#
# 输出：queries = ["FooBar","FooBarTest","FootBall","FrameBuffer","ForceFeedBack"], pattern = "FoBaT"
# 输入：[false,true,false,false,false]
# 解释：
# "FooBarTest" 可以这样生成："Fo" + "o" + "Ba" + "r" + "T" + "est".
#

class Solution:
    def camelMatch(self, queries: List[str], pattern: str) -> List[bool]:
        res = [False] * len(queries)
        i = 0
        for x in queries:
            res[i] = self.match(x, pattern)
            i += 1
        return res

    def match(self, s, p):
        i = 0
        j = 0

        while j < len(s):
            if i < len(p):
                if p[i].isupper():
                    if s[j].islower():
                        j += 1
                    else:
                        if s[j] != p[i]:
                            return False
                        else:
                            j += 1
                            i += 1
                else:
                    if s[j].isupper():
                        return False
                    else:
                        if s[j] != p[i]:
                            j += 1
                        else:
                            i += 1
                            j += 1
            else:
                break
        if len(p) > i:
            return False
        for x in s[j:]:
            if x.isupper():
                return False
        return True


if __name__ == "__main__":
    queries = ["FooBar","FooBarTest","FootBall","FrameBuffer","ForceFeedBack"]
    pattern = "FB"

    test = Solution().camelMatch(queries, pattern)
    print(test)
