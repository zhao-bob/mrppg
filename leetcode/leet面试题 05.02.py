from typing import List


# 面试题 05.02. 二进制数转字符串

# 二进制数转字符串。给定一个介于0和1之间的实数（如0.72），类型为double，打印它的二进制表达式。如果该数字无法精确地用32位以内的二进制表示，则打印“ERROR”。
#
# 示例1:
#
#  输入：0.625
#  输出："0.101"
# 示例2:
#
#  输入：0.1
#  输出："ERROR"
#  提示：0.1无法被二进制准确表示
#


class Solution:
    def printBin(self, num: float) -> str:
        res = "0."
        if num >= 1 or num < 0:
            return "ERROR"

        c = num
        for i in range(32):
            if c * 2 == 0:
                res += "0"
                return res
            if c * 2 < 1:
                res += "0"
                c = c * 2
            elif c * 2 > 1:
                res += "1"
                c = c * 2 - 1
            else:
                res += "1"
                return res
        else:
            return "ERROR"


if __name__ == "__main__":
    #
    num = 0.0
    test = Solution().printBin(num)
    print(test)
