from typing import List


# 1094. 拼车
# 提示
# 中等
# 301
# 相关企业
# 车上最初有 capacity 个空座位。车 只能 向一个方向行驶（也就是说，不允许掉头或改变方向）
#
# 给定整数 capacity 和一个数组 trips ,  trip[i] = [numPassengersi, fromi, toi] 表示第 i 次旅行有 numPassengersi 乘客，接他们和放他们的位置分别是 fromi 和 toi 。这些位置是从汽车的初始位置向东的公里数。
#
# 当且仅当你可以在所有给定的行程中接送所有乘客时，返回 true，否则请返回 false。
#
#
#
# 示例 1：
#
# 输入：trips = [[2,1,5],[3,3,7]], capacity = 4
# 输出：false
# 示例 2：
#
# 输入：trips = [[2,1,5],[3,3,7]], capacity = 5
# 输出：true
#


class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        l = {}

        for t in trips:
            if t[1] in l:
                l[t[1]] += t[0]
            else:
                l[t[1]] = t[0]
            if t[2] in l:
                l[t[2]] -= t[0]
            else:
                l[t[2]] = -t[0]
        p = sorted(l.keys())

        c = 0
        for i in p:
            c += l[i]
            if c > capacity:
                return False
        return True


if __name__ == "__main__":
    trips = [[2, 1, 5], [3, 3, 7]]
    capacity = 4
    test = Solution().carPooling(trips, capacity)
    print(test)
