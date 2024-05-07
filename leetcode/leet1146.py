import heapq
import math
from collections import deque, Counter
from itertools import count
from typing import List, Optional


# 1146. 快照数组
# 中等
# 相关标签
# 相关企业
# 提示
# 实现支持下列接口的「快照数组」- SnapshotArray：
#
# SnapshotArray(int length) - 初始化一个与指定长度相等的 类数组 的数据结构。初始时，每个元素都等于 0。
# void set(index, val) - 会将指定索引 index 处的元素设置为 val。
# int snap() - 获取该数组的快照，并返回快照的编号 snap_id（快照号是调用 snap() 的总次数减去 1）。
# int get(index, snap_id) - 根据指定的 snap_id 选择快照，并返回该快照指定索引 index 的值。
#
#
# 示例：
#
# 输入：["SnapshotArray","set","snap","set","get"]
#      [[3],[0,5],[],[0,6],[0,0]]
# 输出：[null,null,0,null,5]
# 解释：
# SnapshotArray snapshotArr = new SnapshotArray(3); // 初始化一个长度为 3 的快照数组
# snapshotArr.set(0,5);  // 令 array[0] = 5
# snapshotArr.snap();  // 获取快照，返回 snap_id = 0
# snapshotArr.set(0,6);
# snapshotArr.get(0,0);  // 获取 snap_id = 0 的快照中 array[0] 的值，返回 5
#
#
# 提示：
#
# 1 <= length <= 50000
# 题目最多进行50000 次set，snap，和 get的调用 。
# 0 <= index < length
# 0 <= snap_id < 我们调用 snap() 的总次数
# 0 <= val <= 10^9
#

class SnapshotArray:

    def __init__(self, length: int):
        self.snapId = 0
        self.array = [[] for _ in range(length)]

    def set(self, index: int, val: int) -> None:
        if self.array[index] and self.array[index][-1][0] == self.snapId:
            self.array[index][-1][1] = val
        else:
            if not self.array[index] and self.snapId != 0:
                self.array[index].append([0, 0])
            self.array[index].append([self.snapId, val])

    def snap(self) -> int:
        si = self.snapId
        self.snapId += 1
        return si

    def get(self, index: int, snap_id: int) -> int:
        snap = self.array[index]

        if snap:
            right = len(snap)
            left = 0
            while left < right - 1:
                mid = (left + right) // 2
                if snap[mid][0] > snap_id:
                    right = mid - 1
                elif snap[mid][0] < snap_id:
                    left = mid
                else:
                    left = mid
                    break
            if snap[left + 1][0] <= snap_id:
                return snap[left + 1][1]
            else:
                return snap[left][1]
        else:
            return 0

# Your SnapshotArray object will be instantiated and called as such:
# obj = SnapshotArray(length)
# obj.set(index,val)
# param_2 = obj.snap()
# param_3 = obj.get(index,snap_id)

if __name__ == "__main__":
    ops = ["SnapshotArray","set","snap","set","snap","snap","set","snap","get","snap","snap","set","snap","get","set","snap","set","set"]
    par = [[2],[0,8],[],[0,9],[],[],[0,11],[],[1,1],[],[],[0,1],[],[0,1],[0,0],[],[0,3],[1,13]]
    sa = SnapshotArray(par[0][0])
    res = []
    for i in range(1, len(par)):
        if ops[i] == "set":
            res.append(sa.set(par[i][0], par[i][1]))
        if ops[i] == "snap":
            res.append(sa.snap())
        if ops[i] == "get":
            res.append(sa.get(par[i][0], par[i][1]))
    print(res)
