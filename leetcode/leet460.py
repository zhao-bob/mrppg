import collections
import heapq
import math
from bisect import bisect_right
from collections import Counter, deque
from functools import cache
from itertools import product
from typing import List, Optional


# 460. LFU 缓存
# 困难
# 694
# 相关企业
# 请你为 最不经常使用（LFU）缓存算法设计并实现数据结构。
#
# 实现 LFUCache 类：
#
# LFUCache(int capacity) - 用数据结构的容量 capacity 初始化对象
# int get(int key) - 如果键 key 存在于缓存中，则获取键的值，否则返回 -1 。
# void put(int key, int value) - 如果键 key 已存在，则变更其值；如果键不存在，请插入键值对。当缓存达到其容量 capacity 时，则应该在插入新项之前，移除最不经常使用的项。在此问题中，当存在平局（即两个或更多个键具有相同使用频率）时，应该去除 最近最久未使用 的键。
# 为了确定最不常使用的键，可以为缓存中的每个键维护一个 使用计数器 。使用计数最小的键是最久未使用的键。
#
# 当一个键首次插入到缓存中时，它的使用计数器被设置为 1 (由于 put 操作)。对缓存中的键执行 get 或 put 操作，使用计数器的值将会递增。
#
# 函数 get 和 put 必须以 O(1) 的平均时间复杂度运行。
#
#
#
# 示例：
#
# 输入：
# ["LFUCache", "put", "put", "get", "put", "get", "get", "put", "get", "get", "get"]
# [[2], [1, 1], [2, 2], [1], [3, 3], [2], [3], [4, 4], [1], [3], [4]]
# 输出：
# [null, null, null, 1, null, -1, 3, null, -1, 3, 4]
#
# 解释：
# // cnt(x) = 键 x 的使用计数
# // cache=[] 将显示最后一次使用的顺序（最左边的元素是最近的）
# LFUCache lfu = new LFUCache(2);
# lfu.put(1, 1);   // cache=[1,_], cnt(1)=1
# lfu.put(2, 2);   // cache=[2,1], cnt(2)=1, cnt(1)=1
# lfu.get(1);      // 返回 1
#                  // cache=[1,2], cnt(2)=1, cnt(1)=2
# lfu.put(3, 3);   // 去除键 2 ，因为 cnt(2)=1 ，使用计数最小
#                  // cache=[3,1], cnt(3)=1, cnt(1)=2
# lfu.get(2);      // 返回 -1（未找到）
# lfu.get(3);      // 返回 3
#                  // cache=[3,1], cnt(3)=2, cnt(1)=2
# lfu.put(4, 4);   // 去除键 1 ，1 和 3 的 cnt 相同，但 1 最久未使用
#                  // cache=[4,3], cnt(4)=1, cnt(3)=2
# lfu.get(1);      // 返回 -1（未找到）
# lfu.get(3);      // 返回 3
#                  // cache=[3,4], cnt(4)=1, cnt(3)=3
# lfu.get(4);      // 返回 4
#                  // cache=[3,4], cnt(4)=2, cnt(3)=3

class LFUCache:
    class Queue:
        def __init__(self, val, n=None, p=None):
            self.next = n
            self.previous = self
            self.val = val

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}
        self.queues = [self.Queue(-1) for _ in range(20000)]
        self.ci = -1

    def change(self, n, q):
        h1 = self.queues[n]
        h2 = self.queues[n + 1]
        if q.next:
            p = q.previous
            q.next.previous = p
            p.next = q.next
        else:
            h1.previous = q.previous
            q.previous.next = None
        if h2.previous:
            h2.previous.next = q
            q.previous = h2.previous
            h2.previous = q
        else:
            q.previous = h2
            h2.previous = q
            h2.next = q
        q.next = None
        if h1.next is None and n == self.ci:
            self.ci += 1

    def get(self, key: int) -> int:
        if key in self.cache:
            res = self.cache[key]
            self.change(res[1], res[2])
            res[1] += 1
            return res[0]
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            res = self.cache[key]
            self.change(res[1], res[2])
            res[1] += 1
            res[0] = value
        else:
            if len(self.cache) >= self.capacity:
                dh = self.queues[self.ci]
                self.cache.pop(dh.next.val)
                if dh.next.next:
                    dh.next.next.previous = dh
                    dh.next = dh.next.next
                else:
                    dh.next = None
                    dh.previous = dh
            q = self.Queue(key)
            if self.queues[0].previous != self.queues[0]:
                self.queues[0].previous.next = q
                q.previous = self.queues[0].previous
                self.queues[0].previous = q
            else:
                self.queues[0].next = q
                q.previous = self.queues[0]
                self.queues[0].previous = q
                self.ci = 0
            self.cache[key] = [value, 0, q]


# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)


if __name__ == "__main__":
    ops = ["LFUCache","put","put","get","get","get","put","put","get","get","get","get"]
    par = [[3],[2,2],[1,1],[2],[1],[2],[3,3],[4,4],[3],[2],[1],[4]]
    lfuc = LFUCache(par[0][0])
    res = []
    for i in range(1, len(par)):
        if ops[i] == "put":
            res.append(lfuc.put(par[i][0], par[i][1]))
        if ops[i] == "get":
            res.append(lfuc.get(par[i][0]))
    print(res)
