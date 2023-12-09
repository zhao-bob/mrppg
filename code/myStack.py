class Stack:
    def __init__(self, maxlen=10):
        '''创建栈对象并进行初始化，默认栈大小为10'''
        # 使用列表存放栈的元素
        self._content = []
        # 初始栈大小
        self._size = maxlen
        # 栈中元素个数初始化为0
        self._current = 0

    def __del__(self):
        del self._content
        
    def empty(self):
        '''清空栈'''
        self._content = []
        self._current = 0
        
    def isEmpty(self):
        '''测试栈是否为空'''
        return not self._content

    def setSize(self, size):
        '''调整栈的大小，可以增大或缩小栈空间'''
        # 如果缩小空间时指定的新大小，小于已有元素个数
        # 则删除指定大小之后的已有元素
        if size < self._current:
            for i in range(size, self._current)[::-1]:
                del self._content[i]
            self._current = size
        self._size = size

    def __len__(self):
        return len(self._content)
    
    def isFull(self):
        '''测试栈是否已满'''
        return self._current == self._size
        
    def push(self, v):
        '''将新元素入栈'''
        if self._current < self._size:
            self._content.append(v)
            # 栈中元素个数加1
            self._current = self._current + 1
        else:
            print('Stack Full!')
            
    def pop(self):
        '''将栈顶元素出栈'''
        if self._content:
            # 栈中元素个数减1
            self._current = self._current - 1
            return self._content.pop()
        else:
            print('Stack is empty!')

    def __str__(self):
        return f'Stack({self._content}, maxlen={self._size})'

    __repr__ = __str__


if __name__ == '__main__':
    print('Please use me as a module.')
