from typing import List


# 1237. 找出给定方程的正整数解

# 给你一个函数f(x, y)和一个目标结果z，函数公式未知，请你计算方程f(x,y) == z所有可能的正整数 数对x 和 y。满足条件的结果数对可以按任意顺序返回。
#
# 尽管函数的具体式子未知，但它是单调递增函数，也就是说：
#
# f(x, y) < f(x + 1, y)
# f(x, y) < f(x, y + 1)
# 函数接口定义如下：
#
# interface CustomFunction {
# public:
#   // Returns some positive integer f(x, y) for two positive integers x and y based on a formula.
#   int f(int x, int y);
# };

# 你的解决方案将按如下规则进行评判：
#
# 判题程序有一个由 CustomFunction 的 9 种实现组成的列表，以及一种为特定的 z 生成所有有效数对的答案的方法。
# 判题程序接受两个输入：function_id（决定使用哪种实现测试你的代码）以及目标结果 z 。
# 判题程序将会调用你实现的 findSolution 并将你的结果与答案进行比较。
# 如果你的结果与答案相符，那么解决方案将被视作正确答案，即 Accepted 。

# 示例 1：
#
# 输入：function_id = 1, z = 5
# 输出：[[1,4],[2,3],[3,2],[4,1]]
# 解释：function_id = 1 暗含的函数式子为 f(x, y) = x + y
# 以下 x 和 y 满足 f(x, y) 等于 5：
# x=1, y=4 -> f(1, 4) = 1 + 4 = 5
# x=2, y=3 -> f(2, 3) = 2 + 3 = 5
# x=3, y=2 -> f(3, 2) = 3 + 2 = 5
# x=4, y=1 -> f(4, 1) = 4 + 1 = 5
# 示例 2：
#
# 输入：function_id = 2, z = 5
# 输出：[[1,5],[5,1]]
# 解释：function_id = 2 暗含的函数式子为 f(x, y) = x * y
# 以下 x 和 y 满足 f(x, y) 等于 5：
# x=1, y=5 -> f(1, 5) = 1 * 5 = 5
# x=5, y=1 -> f(5, 1) = 5 * 1 = 5


class Solution:
    def findSolution(self, customfunction: 'CustomFunction', z: int) -> List[List[int]]:
        x = 1
        y = 1
        res = []
        while customfunction.f(x, y) <= z:
            if customfunction.f(x, y) == z:
                solution = [x, y]
                res.append(solution)
                x += 1
                y = 1
            else:
                y += 1
                if customfunction.f(x, y) == z:
                    solution = [x, y]
                    res.append(solution)
                    x += 1
                    y = 1
                elif customfunction.f(x, y) > z:
                    x += 1
                    y = 1
        return res


class CustomFunction:
    def __init__(self, x):
        self.num = x

    def f(self, x, y):
        if self.num == 1:
            return x + y
        elif self.num == 2:
            return x * y
        elif self.num == 3:
            return x * x + y
        elif self.num == 4:
            return x + y * y
        elif self.num == 5:
            return x * x + y * y
        elif self.num == 6:
            return (x + y) * (x + y)
        elif self.num == 7:
            return x * x * x + y * y * y
        elif self.num == 8:
            return x * x * y
        elif self.num == 9:
            return x * y * y
        else:
            return 0


if __name__ == "__main__":
    z = 5
    test = Solution().findSolution(CustomFunction(1), z)
    print(test)
