import collections
import heapq
import math
from bisect import bisect_right
from collections import Counter, deque
from functools import cache
from itertools import product
from typing import List, Optional


# 1993. 树上的操作
# 提示
# 中等
# 31
# 相关企业
# 给你一棵 n 个节点的树，编号从 0 到 n - 1 ，以父节点数组 parent 的形式给出，其中 parent[i] 是第 i 个节点的父节点。树的根节点为 0 号节点，所以 parent[0] = -1 ，因为它没有父节点。你想要设计一个数据结构实现树里面对节点的加锁，解锁和升级操作。
#
# 数据结构需要支持如下函数：
#
# Lock：指定用户给指定节点 上锁 ，上锁后其他用户将无法给同一节点上锁。只有当节点处于未上锁的状态下，才能进行上锁操作。
# Unlock：指定用户给指定节点 解锁 ，只有当指定节点当前正被指定用户锁住时，才能执行该解锁操作。
# Upgrade：指定用户给指定节点 上锁 ，并且将该节点的所有子孙节点 解锁 。只有如下 3 个条件 全部 满足时才能执行升级操作：
# 指定节点当前状态为未上锁。
# 指定节点至少有一个上锁状态的子孙节点（可以是 任意 用户上锁的）。
# 指定节点没有任何上锁的祖先节点。
# 请你实现 LockingTree 类：
#
# LockingTree(int[] parent) 用父节点数组初始化数据结构。
# lock(int num, int user) 如果 id 为 user 的用户可以给节点 num 上锁，那么返回 true ，否则返回 false 。如果可以执行此操作，节点 num 会被 id 为 user 的用户 上锁 。
# unlock(int num, int user) 如果 id 为 user 的用户可以给节点 num 解锁，那么返回 true ，否则返回 false 。如果可以执行此操作，节点 num 变为 未上锁 状态。
# upgrade(int num, int user) 如果 id 为 user 的用户可以给节点 num 升级，那么返回 true ，否则返回 false 。如果可以执行此操作，节点 num 会被 升级 。
#
#
# 示例 1：
#
#
#
# 输入：
# ["LockingTree", "lock", "unlock", "unlock", "lock", "upgrade", "lock"]
# [[[-1, 0, 0, 1, 1, 2, 2]], [2, 2], [2, 3], [2, 2], [4, 5], [0, 1], [0, 1]]
# 输出：
# [null, true, false, true, true, true, false]
#
# 解释：
# LockingTree lockingTree = new LockingTree([-1, 0, 0, 1, 1, 2, 2]);
# lockingTree.lock(2, 2);    // 返回 true ，因为节点 2 未上锁。
#                            // 节点 2 被用户 2 上锁。
# lockingTree.unlock(2, 3);  // 返回 false ，因为用户 3 无法解锁被用户 2 上锁的节点。
# lockingTree.unlock(2, 2);  // 返回 true ，因为节点 2 之前被用户 2 上锁。
#                            // 节点 2 现在变为未上锁状态。
# lockingTree.lock(4, 5);    // 返回 true ，因为节点 4 未上锁。
#                            // 节点 4 被用户 5 上锁。
# lockingTree.upgrade(0, 1); // 返回 true ，因为节点 0 未上锁且至少有一个被上锁的子孙节点（节点 4）。
#                            // 节点 0 被用户 1 上锁，节点 4 变为未上锁。
# lockingTree.lock(0, 1);    // 返回 false ，因为节点 0 已经被上锁了。

class LockingTree:

    def __init__(self, parent: List[int]):
        self.next = [[] for _ in range(len(parent) + 1)]
        self.status = [-1 for _ in range(len(parent))]
        self.parent = parent

        for i in range(len(parent)):
            self.next[parent[i]].append(i)

    def lock(self, num: int, user: int) -> bool:
        if self.status[num] != -1:
            return False
        else:
            self.status[num] = user
            return True

    def unlock(self, num: int, user: int) -> bool:
        if self.status[num] == user:
            self.status[num] = -1
            return True
        else:
            return False

    def upgrade(self, num: int, user: int) -> bool:
        if self.status[num] != -1:
            return False
        p = self.parent[num]
        while p != -1:
            if self.status[p] != -1:
                return False
            p = self.parent[p]
        q = self.next[num]

        locked = []
        while q:
            n = q[0]
            q = q[1:]
            if self.status[n] != -1:
                locked.append(n)
            q.extend(self.next[n])

        if len(locked) == 0:
            return False


# Your LockingTree object will be instantiated and called as such:
# obj = LockingTree(parent)
# param_1 = obj.lock(num,user)
# param_2 = obj.unlock(num,user)
# param_3 = obj.upgrade(num,user)


if __name__ == "__main__":
    ops = ["LockingTree","lock","upgrade","lock","upgrade","upgrade","lock","lock","upgrade","upgrade","lock","unlock","upgrade","upgrade","lock","unlock","upgrade","upgrade","upgrade","lock","upgrade","unlock","unlock","lock","upgrade","unlock","upgrade","unlock","upgrade","upgrade","upgrade","upgrade","upgrade","upgrade","upgrade","upgrade","lock","upgrade","upgrade","unlock","upgrade","upgrade","unlock","unlock","unlock","upgrade","upgrade","upgrade","upgrade","lock","upgrade","unlock","upgrade","upgrade","lock","upgrade","upgrade","upgrade","upgrade","upgrade","upgrade","upgrade","unlock","lock","lock","upgrade","lock","upgrade","upgrade","upgrade","upgrade","lock","unlock","upgrade","lock","unlock","upgrade","upgrade","unlock","unlock","lock","upgrade","upgrade","lock","upgrade","upgrade","lock","lock","upgrade","upgrade","upgrade","upgrade","upgrade","unlock","upgrade","unlock","upgrade","upgrade","unlock","lock","upgrade"]
    par = [[[-1,36,21,22,5,41,23,0,14,15,26,24,41,33,13,22,4,16,0,22,7,6,18,8,0,13,24,26,15,37,18,18,13,40,4,28,18,0,8,24,18,30,19,34,24,22,19,20,27,26]],[35,3],[38,34],[35,73],[13,59],[12,71],[37,41],[16,33],[45,74],[38,46],[16,66],[8,78],[49,4],[41,99],[37,14],[37,41],[29,17],[4,85],[4,11],[16,31],[47,47],[46,44],[37,18],[43,58],[47,62],[16,33],[33,59],[35,3],[42,67],[9,10],[18,41],[18,67],[7,40],[20,32],[5,76],[25,71],[43,19],[26,68],[34,49],[43,58],[0,72],[38,66],[47,85],[1,69],[44,75],[32,5],[23,15],[23,87],[43,81],[36,15],[46,29],[36,15],[42,68],[1,83],[35,81],[44,27],[16,54],[47,54],[14,61],[0,11],[10,78],[10,79],[35,81],[38,42],[1,92],[31,55],[38,98],[19,13],[17,42],[10,77],[15,63],[1,5],[38,42],[44,1],[37,37],[1,92],[41,44],[16,53],[21,27],[21,90],[37,83],[26,33],[37,30],[37,52],[12,16],[37,74],[37,94],[15,54],[43,19],[1,54],[27,36],[44,62],[18,52],[37,37],[6,58],[36,89],[38,28],[41,41],[15,54],[44,82],[0,99]]
    lt = LockingTree(par[0][0])
    res = []
    for i in range(1, 39):
        if ops[i] == "lock":
            res.append(lt.lock(par[i][0], par[i][1]))
        if ops[i] == "unlock":
            res.append(lt.unlock(par[i][0], par[i][1]))
        if ops[i] == "upgrade":
            res.append(lt.upgrade(par[i][0], par[i][1]))
    print(res)
