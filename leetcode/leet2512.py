import heapq
import math
from collections import Counter
from typing import List
from sortedcontainers import SortedList


# 2512. 奖励最顶尖的 K 名学生
# 提示
# 中等
# 12
# 相关企业
# 给你两个字符串数组 positive_feedback 和 negative_feedback ，分别包含表示正面的和负面的词汇。不会 有单词同时是正面的和负面的。
#
# 一开始，每位学生分数为 0 。每个正面的单词会给学生的分数 加 3 分，每个负面的词会给学生的分数 减  1 分。
#
# 给你 n 个学生的评语，用一个下标从 0 开始的字符串数组 report 和一个下标从 0 开始的整数数组 student_id 表示，其中 student_id[i] 表示这名学生的 ID ，这名学生的评语是 report[i] 。每名学生的 ID 互不相同。
#
# 给你一个整数 k ，请你返回按照得分 从高到低 最顶尖的 k 名学生。如果有多名学生分数相同，ID 越小排名越前。
#
#
#
# 示例 1：
#
# 输入：positive_feedback = ["smart","brilliant","studious"], negative_feedback = ["not"], report = ["this student is studious","the student is smart"], student_id = [1,2], k = 2
# 输出：[1,2]
# 解释：
# 两名学生都有 1 个正面词汇，都得到 3 分，学生 1 的 ID 更小所以排名更前。
# 示例 2：
#
# 输入：positive_feedback = ["smart","brilliant","studious"], negative_feedback = ["not"], report = ["this student is not studious","the student is smart"], student_id = [1,2], k = 2
# 输出：[2,1]
# 解释：
# - ID 为 1 的学生有 1 个正面词汇和 1 个负面词汇，所以得分为 3-1=2 分。
# - ID 为 2 的学生有 1 个正面词汇，得分为 3 分。
# 学生 2 分数更高，所以返回 [2,1] 。
#


class Solution:
    def topStudents(self, positive_feedback: List[str], negative_feedback: List[str], report: List[str], student_id: List[int], k: int) -> List[int]:
        pf = set(positive_feedback)
        nf = set(negative_feedback)
        o = []
        for i in range(len(report)):
            w = Counter(report[i].split(' '))
            s = sum(w[x] * 3 for x in pf.intersection(w)) - sum(w[x] for x in nf.intersection(w))
            o.append((s, student_id[i]))

        o.sort(key=lambda x: (x[0], -x[1]), reverse=True)
        return [o[i][1] for i in range(k)]



if __name__ == "__main__":
    positive_feedback = ["utqjmq","f","phss","gbuq","qutww","irwkmv","kdr","cb"]
    negative_feedback = ["tccrt","xyvvvjhf","igkhpx","l","hqdhsc","nrgfoaje","pwp","xgnrgm"]
    report = ["idkcqa cb evdotmzx phss l xyvvvjhf l ccfa kdr l",
              "jtswrxt lwj gryuxwdk fodazsucff pwp f tccrt qutww irwkmv lzohrrfahd",
              "l f cb gornnntm tccrt xgnrgm gexhslh hqdhsc gbuq igkhpx",
              "f igkhpx irwkmv fmvomibc estombev irwkmv xyvvvjhf irwkmv gbuq irwkmv"]
    student_id = [880134715,923494207,595896825,62500464]
    k = 3
    test = Solution().topStudents(positive_feedback, negative_feedback, report, student_id, k)
    print(test)
