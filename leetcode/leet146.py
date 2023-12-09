import collections
import heapq
import math
from bisect import bisect_right
from collections import Counter, deque
from functools import cache
from itertools import product
from typing import List, Optional


# 146. LRU 缓存
# 中等
# 2.9K
# 相关企业
# 请你设计并实现一个满足  LRU (最近最少使用) 缓存 约束的数据结构。
# 实现 LRUCache 类：
# LRUCache(int capacity) 以 正整数 作为容量 capacity 初始化 LRU 缓存
# int get(int key) 如果关键字 key 存在于缓存中，则返回关键字的值，否则返回 -1 。
# void put(int key, int value) 如果关键字 key 已经存在，则变更其数据值 value ；如果不存在，则向缓存中插入该组 key-value 。如果插入操作导致关键字数量超过 capacity ，则应该 逐出 最久未使用的关键字。
# 函数 get 和 put 必须以 O(1) 的平均时间复杂度运行。
#
#
#
# 示例：
#
# 输入
# ["LRUCache", "put", "put", "get", "put", "get", "put", "get", "get", "get"]
# [[2], [1, 1], [2, 2], [1], [3, 3], [2], [4, 4], [1], [3], [4]]
# 输出
# [null, null, null, 1, null, -1, null, -1, 3, 4]
#
# 解释
# LRUCache lRUCache = new LRUCache(2);
# lRUCache.put(1, 1); // 缓存是 {1=1}
# lRUCache.put(2, 2); // 缓存是 {1=1, 2=2}
# lRUCache.get(1);    // 返回 1
# lRUCache.put(3, 3); // 该操作会使得关键字 2 作废，缓存是 {1=1, 3=3}
# lRUCache.get(2);    // 返回 -1 (未找到)
# lRUCache.put(4, 4); // 该操作会使得关键字 1 作废，缓存是 {4=4, 3=3}
# lRUCache.get(1);    // 返回 -1 (未找到)
# lRUCache.get(3);    // 返回 3
# lRUCache.get(4);    // 返回 4

class LRUCache:
    class Queue:
        def __init__(self, val, n=None):
            self.next = n
            self.val = val

    def change(self, q):
        t = q.next
        n = t.next
        self.cache[n.val][1] = q
        q.next = n
        self.last.next = t
        t.next = None

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.first = self.Queue(-1)
        self.last = self.first
        self.cache = {}

    def get(self, key: int) -> int:
        if key in self.cache:
            res = self.cache[key]
            if res[1].next != self.last:
                self.change(res[1])
                res[1] = self.last
                self.last = self.last.next
            return res[0]
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            res = self.cache[key]
            if res[1].next != self.last:
                self.change(res[1])
                res[1] = self.last
                self.last = self.last.next
            res[0] = value
        else:
            if len(self.cache) >= self.capacity:
                dkey = self.first.next.val
                self.cache.pop(dkey)
                self.first = self.first.next
                if self.first is None:
                    self.first = self.Queue(-1)
                    self.last = self.first
            q = self.Queue(key)
            self.last.next = q
            self.cache[key] = [value, self.last]
            self.last = q


if __name__ == "__main__":
    ops = ["LRUCache", "put", "put", "get", "put", "get", "put", "get", "get", "get"]
    par = [[2], [1, 1], [2, 2], [1], [3, 3], [2], [4, 4], [1], [3], [4]]
    lruc = LRUCache(par[0][0])
    res = []
    for i in range(1, len(par)):
        if ops[i] == "put":
            res.append(lruc.put(par[i][0], par[i][1]))
        if ops[i] == "get":
            res.append(lruc.get(par[i][0]))
    print(res)
