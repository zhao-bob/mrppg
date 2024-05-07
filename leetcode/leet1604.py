# 1604. 警告一小时内使用相同员工卡大于等于三次的人
# 中等
# 相关标签
# 相关企业
# 提示
# 力扣公司的员工都使用员工卡来开办公室的门。每当一个员工使用一次他的员工卡，安保系统会记录下员工的名字和使用时间。如果一个员工在一小时时间内使用员工卡的次数大于等于三次，这个系统会自动发布一个 警告 。
#
# 给你字符串数组 keyName 和 keyTime ，其中 [keyName[i], keyTime[i]] 对应一个人的名字和他在 某一天 内使用员工卡的时间。
#
# 使用时间的格式是 24小时制 ，形如 "HH:MM" ，比方说 "23:51" 和 "09:49" 。
#
# 请你返回去重后的收到系统警告的员工名字，将它们按 字典序升序 排序后返回。
#
# 请注意 "10:00" - "11:00" 视为一个小时时间范围内，而 "22:51" - "23:52" 不被视为一小时时间范围内。
#
#
#
# 示例 1：
#
# 输入：keyName = ["daniel","daniel","daniel","luis","luis","luis","luis"], keyTime = ["10:00","10:40","11:00","09:00","11:00","13:00","15:00"]
# 输出：["daniel"]
# 解释："daniel" 在一小时内使用了 3 次员工卡（"10:00"，"10:40"，"11:00"）。
# 示例 2：
#
# 输入：keyName = ["alice","alice","alice","bob","bob","bob","bob"], keyTime = ["12:01","12:00","18:00","21:00","21:20","21:30","23:00"]
# 输出：["bob"]
# 解释："bob" 在一小时内使用了 3 次员工卡（"21:00"，"21:20"，"21:30"）。
#
#
# 提示：
#
# 1 <= keyName.length, keyTime.length <= 105
# keyName.length == keyTime.length
# keyTime 格式为 "HH:MM" 。
# 保证 [keyName[i], keyTime[i]] 形成的二元对 互不相同 。
# 1 <= keyName[i].length <= 10
# keyName[i] 只包含小写英文字母。
#

import heapq
import math
from collections import Counter
from datetime import date
from typing import List, Optional


class Solution:
    def alertNames(self, keyName: List[str], keyTime: List[str]) -> List[str]:
        def compareTime(t1, t2):
            l1 = list(map(int, t1.split(':')))
            l2 = list(map(int, t2.split(':')))
            if abs(l2[0] - l1[0]) > 1 or (l2[0] - l1[0] == 1 and l2[1] > l1[1]):
                return False
            else:
                return True

        n = len(keyName)
        l = []
        for i in range(n):
            l.append((keyName[i], keyTime[i]))
        l.sort(key=lambda x: (x[0], x[1]))

        name = ''
        time1 = ''
        time2 = ''
        res = []
        for i in range(n):
            if res and l[i][0] == res[-1]:
                continue
            if l[i][0] == name:
                if time1 != '':
                    if compareTime(time1, l[i][1]):
                        if time2 != '':
                            res.append(l[i][0])
                        else:
                            time2 = l[i][1]
                    else:
                        if time2 != '':
                            if compareTime(time2, l[i][1]):
                                time1 = time2
                                time2 = l[i][1]
                            else:
                                time1 = l[i][1]
                                time2 = ''
                        else:
                            time1 = l[i][1]
                else:
                    time1 = l[i][1]
            else:
                name = l[i][0]
                time1 = l[i][1]
                time2 = ''
        return res


if __name__ == "__main__":
    keyName = ["daniel", "daniel", "daniel", "luis", "luis", "luis", "luis"]
    keyTime = ["10:00", "10:40", "11:00", "09:00", "11:00", "13:00", "15:00"]

    test = Solution().alertNames(keyName, keyTime)

    print(test)
