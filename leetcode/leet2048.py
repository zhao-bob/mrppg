from typing import List


# 2048. 下一个更大的数值平衡数
# 提示
# 中等
# 32
# 相关企业
# 如果整数  x 满足：对于每个数位 d ，这个数位 恰好 在 x 中出现 d 次。那么整数 x 就是一个 数值平衡数 。
#
# 给你一个整数 n ，请你返回 严格大于 n 的 最小数值平衡数 。
#
#
#
# 示例 1：
#
# 输入：n = 1
# 输出：22
# 解释：
# 22 是一个数值平衡数，因为：
# - 数字 2 出现 2 次
# 这也是严格大于 1 的最小数值平衡数。
# 示例 2：
#
# 输入：n = 1000
# 输出：1333
# 解释：
# 1333 是一个数值平衡数，因为：
# - 数字 1 出现 1 次。
# - 数字 3 出现 3 次。
# 这也是严格大于 1000 的最小数值平衡数。
# 注意，1022 不能作为本输入的答案，因为数字 0 的出现次数超过了 0 。
# 示例 3：
#
# 输入：n = 3000
# 输出：3133
# 解释：
# 3133 是一个数值平衡数，因为：
# - 数字 1 出现 1 次。
# - 数字 3 出现 3 次。
# 这也是严格大于 3000 的最小数值平衡数。
#


class Solution:
    def nextBeautifulNumber(self, n: int) -> int:
        def beautiful(k):
            m = {}
            while k > 0:
                d = k % 10
                if d in m:
                    m[d] += 1
                else:
                    m[d] = 1
                k //= 10
            for x in m:
                if m[x] != 0 and m[x] != x:
                    return False
            return True
        n += 1
        while not beautiful(n):
            n += 1
        return n

        # def beautiful(i, m, s):
        #     if i == length + 1:
        #         for x in s:
        #             if s[x] != 0 and s[x] != x:
        #                 return -1
        #         return m
        #     for c in range(d[-i], length + 1):
        #         if c in s:
        #             if s[c] < c:
        #                 s[c] += 1
        #                 m = m * 10 + c
        #                 a = beautiful(i + 1, m, s)
        #                 if a > -1:
        #                     return a
        #             else:
        #                 continue
        #         else:
        #             if c == 0:
        #                 continue
        #             s[c] = 1
        #             m = m * 10 + c
        #             a = beautiful(i + 1, m, s)
        #             if a > -1:
        #                 return a
        #
        #         s[c] -= 1
        #         m = m // 10
        #     return -1
        #
        # a = beautiful(1, 0, {})
        # if a == -1:
        #     d = [0] * length
        #     d.append(1)
        #     length += 1
        #     return beautiful(1, 0, {})




if __name__ == "__main__":
    n = 188
    test = Solution().nextBeautifulNumber(n)
    print(test)
