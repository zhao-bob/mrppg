import math
from typing import List


# 1032. 字符流
# 设计一个算法：接收一个字符流，并检查这些字符的后缀是否是字符串数组 words 中的一个字符串。
#
# 例如，words = ["abc", "xyz"] 且字符流中逐个依次加入 4 个字符 'a'、'x'、'y' 和 'z' ，你所设计的算法应当可以检测到 "axyz" 的后缀 "xyz" 与 words 中的字符串 "xyz" 匹配。
#
# 按下述要求实现 StreamChecker 类：
#
# StreamChecker(String[] words) ：构造函数，用字符串数组 words 初始化数据结构。
# boolean query(char letter)：从字符流中接收一个新字符，如果字符流中的任一非空后缀能匹配 words 中的某一字符串，返回 true ；否则，返回 false。
#

class StreamChecker:
    def __init__(self, words: List[str]):
        self.word_map = {}
        self.q_map = []
        for s in words:
            p = self.word_map
            for x in s:
                if x not in p:
                    p[x] = {}
                p = p[x]
            else:
                p[0] = True

    def query(self, letter: str) -> bool:
        res = False
        for i in range(len(self.q_map)):
            if letter in self.q_map[i]:
                if 0 in self.q_map[i][letter]:
                    res = True
                self.q_map[i] = self.q_map[i][letter]
            else:
                self.q_map[i] = 0
        self.q_map = list(filter(lambda x: x != 0, self.q_map))
        if letter in self.word_map:
            n = self.word_map[letter]
            self.q_map.append(n)
            if 0 in n:
                res = True
        return res


if __name__ == "__main__":
    words = ["cd", "f", "kl"]
    s =[["a"], ["b"], ["c"], ["d"], ["e"], ["f"], ["g"], ["h"], ["i"], ["j"], ["k"], ["l"]]

    test = StreamChecker(words)
    for x in s:
        print(test.query(x[0]))
