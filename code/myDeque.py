class MyDeque:
    # 构造方法，默认队列大小为10
    def __init__(self, iterable=None, maxlen=10):
        if iterable == None:
            self._content = []
            self._current = 0
        else:
            self._content = list(iterable)
            self._current = len(iterable)
        self._size = max(len(self._content), maxlen)
        # self._size = maxlen
        # if self._size < self._current:
        #    self._size = self._current
        # self._size = max(self._size, self._current)

    # 析构方法
    def __del__(self):
        del self._content

    # 修改队列大小
    def setSize(self, size):
        if size < self._current:
            # 如果缩小队列，需要同时删除后面的元素
            # del self._content[size:]
            for i in range(size, self._current)[::-1]:
                del self._content[i]
            self._current = size
        self._size = size

    # 在右侧入队
    def appendRight(self, v):
        if self._current < self._size:
            self._content.append(v)
            self._current = self._current + 1
        else:
            print('The queue is full')

    # 在左侧入队
    def appendLeft(self, v):
        if self._current < self._size:
            self._content.insert(0, v)
            self._current = self._current + 1
        else:
            print('The queue is full')

    # 在左侧出队
    def popLeft(self):
        if self._content:
            self._current = self._current - 1
            return self._content.pop(0)
        else:
            print('The queue is empty')

    # 在右侧出队
    def popRight(self):
        if self._content:
            self._current = self._current - 1
            return self._content.pop()
        else:
            print('The queue is empty')

    # 循环移位
    def rotate(self, k):
        if abs(k) > self._current:
            print(f'k must <= {self._current}')
            return
        # k>0时循环右移，k<0时循环左移
        self._content = self._content[-k:] + self._content[:-k]

    # 元素翻转
    def reverse(self):
        self._content = self._content[::-1]
        # self._content.reverse()

    # 显示当前队列中元素个数
    def __len__(self):
        return self._current

    # 使用print()打印对象时，显示当前队列中的元素
    def __str__(self):
        return f'MyDeque({self._content}, maxlen={self._size})'

    # 直接对象名当做表达式时，显示当前队列中的元素，共用__str__()的代码
    __repr__ = __str__

    # 队列置空
    def clear(self):
        self._content = []
        self._current = 0

    # 测试队列是否为空
    def isEmpty(self):
        return not self._content

    # 测试队列是否已满
    def isFull(self):
        return self._current == self._size

if __name__ == '__main__':
    print('Please use me as a module.')
