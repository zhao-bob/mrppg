import heapq
import math
from collections import deque, Counter
from typing import List


# 2007. 从双倍数组中还原原数组
# 中等
# 相关标签
# 相关企业
# 提示
# 一个整数数组 original 可以转变成一个 双倍 数组 changed ，转变方式为将 original 中每个元素 值乘以 2 加入数组中，然后将所有元素 随机打乱 。
#
# 给你一个数组 changed ，如果 change 是 双倍 数组，那么请你返回 original数组，否则请返回空数组。original 的元素可以以 任意 顺序返回。
#
#
#
# 示例 1：
#
# 输入：changed = [1,3,4,2,6,8]
# 输出：[1,3,4]
# 解释：一个可能的 original 数组为 [1,3,4] :
# - 将 1 乘以 2 ，得到 1 * 2 = 2 。
# - 将 3 乘以 2 ，得到 3 * 2 = 6 。
# - 将 4 乘以 2 ，得到 4 * 2 = 8 。
# 其他可能的原数组方案为 [4,3,1] 或者 [3,1,4] 。
# 示例 2：
#
# 输入：changed = [6,3,0,1]
# 输出：[]
# 解释：changed 不是一个双倍数组。
# 示例 3：
#
# 输入：changed = [1]
# 输出：[]
# 解释：changed 不是一个双倍数组。
#
#
# 提示：
#
# 1 <= changed.length <= 105
# 0 <= changed[i] <= 105
#


class Solution:
    def findOriginalArray(self, changed: List[int]) -> List[int]:
        # n = len(changed)
        # if n % 2 == 1:
        #     return []
        # changed.sort(reverse=True)
        # c = {}
        # for i, v in enumerate(changed):
        #     if v not in c:
        #         c[v] = deque()
        #     c[v].append(i)
        # index = set()
        # i = 0
        # res = []
        # while i < n:
        #     if i not in index:
        #         c[changed[i]].popleft()
        #         if changed[i] % 2 == 0:
        #             k = changed[i] // 2
        #             if k in c and c[k]:
        #                 res.append(k)
        #                 index.add(c[k].popleft())
        #             else:
        #                 return []
        #         else:
        #             return []
        #     index.add(i)
        #     i += 1
        # return res
        n = len(changed)
        if n % 2 == 1:
            return []
        changed.sort()
        c = Counter(changed)
        res = []
        for i in changed:
            if c[i] > 0:
                c[i] -= 1
                k = i * 2
                if k in c and c[k] > 0:
                    c[k] -= 1
                    res.append(i)
                else:
                    return []
        return res


if __name__ == "__main__":
    changed = [0,0,0,0,0,0]
    test = Solution().findOriginalArray(changed)
    print(test)
