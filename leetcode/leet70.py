from typing import List


# 70. 爬楼梯
# 提示
# 简单
# 3.4K
# 相关企业
# 假设你正在爬楼梯。需要 n 阶你才能到达楼顶。
#
# 每次你可以爬 1 或 2 个台阶。你有多少种不同的方法可以爬到楼顶呢？
#
#
#
# 示例 1：
#
# 输入：n = 2
# 输出：2
# 解释：有两种方法可以爬到楼顶。
# 1. 1 阶 + 1 阶
# 2. 2 阶
# 示例 2：
#
# 输入：n = 3
# 输出：3
# 解释：有三种方法可以爬到楼顶。
# 1. 1 阶 + 1 阶 + 1 阶
# 2. 1 阶 + 2 阶
# 3. 2 阶 + 1 阶
#


class Solution:
    def climbStairs(self, n: int) -> int:
        f1 = 1
        f2 = 0
        res = 0
        for i in range(n):
            res = f1 + f2
            f2 = f1
            f1 = res
        return res




if __name__ == "__main__":
    n = 3
    test = Solution().climbStairs(n)
    print(test)
