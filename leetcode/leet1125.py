import math
from functools import lru_cache
from typing import List


# 1125. 最小的必要团队
# 作为项目经理，你规划了一份需求的技能清单 req_skills，并打算从备选人员名单 people 中选出些人组成一个「必要团队」（ 编号为 i 的备选人员 people[i] 含有一份该备选人员掌握的技能列表）。
#
# 所谓「必要团队」，就是在这个团队中，对于所需求的技能列表 req_skills 中列出的每项技能，团队中至少有一名成员已经掌握。可以用每个人的编号来表示团队中的成员：
#
# 例如，团队 team = [0, 1, 3] 表示掌握技能分别为 people[0]，people[1]，和 people[3] 的备选人员。
# 请你返回 任一 规模最小的必要团队，团队成员用人员编号表示。你可以按 任意顺序 返回答案，题目数据保证答案存在。
#
#
#
# 示例 1：
#
# 输入：req_skills = ["java","nodejs","reactjs"], people = [["java"],["nodejs"],["nodejs","reactjs"]]
# 输出：[0,2]
# 示例 2：
#
# 输入：req_skills = ["algorithms","math","java","reactjs","csharp","aws"], people = [["algorithms","math","java"],["algorithms","math","reactjs"],["java","csharp","aws"],["reactjs","csharp"],["csharp","math"],["aws","java"]]
# 输出：[1,2]
#

class Solution:
    def smallestSufficientTeam(self, req_skills: List[str], people: List[List[str]]) -> List[int]:
        sid = {s: i for i, s in enumerate(req_skills)}  # 字符串映射到下标
        n = len(people)
        u = 1 << len(req_skills)
        f = [(1 << n) - 1] * u
        f[0] = 0
        for i, skills in enumerate(people):
            mask = 0
            for s in skills:  # 把 skills 压缩成一个二进制数 mask
                mask |= 1 << sid[s]
            for j in range(u - 1, 0, -1):
                res = f[j]  # 不选 mask
                res2 = f[j & ~mask] | (1 << i)  # 选 mask
                f[j] = res if res.bit_count() < res2.bit_count() else res2
        res = f[-1]
        return [i for i in range(n) if (res >> i) & 1]  # 所有在 res 中的下标


if __name__ == "__main__":
    req_skills = ["java", "nodejs", "reactjs"]
    people = [["java"], ["nodejs"], ["nodejs", "reactjs"]]

    test = Solution().smallestSufficientTeam(req_skills, people)
    print(test)
