import heapq
import math
from collections import deque
from typing import List


# 706. 设计哈希映射
# 简单
# 相关标签
# 相关企业
# 不使用任何内建的哈希表库设计一个哈希映射（HashMap）。
#
# 实现 MyHashMap 类：
#
# MyHashMap() 用空映射初始化对象
# void put(int key, int value) 向 HashMap 插入一个键值对 (key, value) 。如果 key 已经存在于映射中，则更新其对应的值 value 。
# int get(int key) 返回特定的 key 所映射的 value ；如果映射中不包含 key 的映射，返回 -1 。
# void remove(key) 如果映射中存在 key 的映射，则移除 key 和它所对应的 value 。
#
#
# 示例：
#
# 输入：
# ["MyHashMap", "put", "put", "get", "get", "put", "get", "remove", "get"]
# [[], [1, 1], [2, 2], [1], [3], [2, 1], [2], [2], [2]]
# 输出：
# [null, null, null, 1, -1, null, 1, null, -1]
#
# 解释：
# MyHashMap myHashMap = new MyHashMap();
# myHashMap.put(1, 1); // myHashMap 现在为 [[1,1]]
# myHashMap.put(2, 2); // myHashMap 现在为 [[1,1], [2,2]]
# myHashMap.get(1);    // 返回 1 ，myHashMap 现在为 [[1,1], [2,2]]
# myHashMap.get(3);    // 返回 -1（未找到），myHashMap 现在为 [[1,1], [2,2]]
# myHashMap.put(2, 1); // myHashMap 现在为 [[1,1], [2,1]]（更新已有的值）
# myHashMap.get(2);    // 返回 1 ，myHashMap 现在为 [[1,1], [2,1]]
# myHashMap.remove(2); // 删除键为 2 的数据，myHashMap 现在为 [[1,1]]
# myHashMap.get(2);    // 返回 -1（未找到），myHashMap 现在为 [[1,1]]
#
#
# 提示：
#
# 0 <= key, value <= 106
# 最多调用 104 次 put、get 和 remove 方法
#


class MyHashMap:

    def __init__(self):
        self.hash = 769
        self.hashMap = [[] for _ in range(self.hash)]

    def put(self, key: int, value: int) -> None:
        h = key % self.hash
        for i in range(len(self.hashMap[h])):
            if self.hashMap[h][i][0] == key:
                self.hashMap[h][i][1] = value
                break
        else:
            self.hashMap[h].append([key, value])

    def get(self, key: int) -> int:
        h = key % self.hash
        for i in range(len(self.hashMap[h])):
            if self.hashMap[h][i][0] == key:
                return self.hashMap[h][i][1]
        else:
            return -1

    def remove(self, key: int) -> None:
        h = key % self.hash
        for i in range(len(self.hashMap[h])):
            if self.hashMap[h][i][0] == key:
                del self.hashMap[h][i]
                break


if __name__ == "__main__":
    ops = ["MyHashMap", "put", "put", "get", "get", "put", "get", "remove", "get"]
    par = [[], [1, 1], [2, 2], [1], [3], [2, 1], [2], [2], [2]]

    mhm = MyHashMap()
    res = []
    for i in range(1, len(par)):
        if ops[i] == "put":
            res.append(mhm.put(par[i][0], par[i][1]))
        if ops[i] == "remove":
            res.append(mhm.remove(par[i][0]))
        if ops[i] == "get":
            res.append(mhm.get(par[i][0]))
    print(res)
