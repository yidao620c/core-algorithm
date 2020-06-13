# -*- encoding: utf-8 -*-
"""基于环形数组实现的一个简单队列
数组A[1..n]实现最多容纳n-1个元素的队列。
"""


class ArrayQueue:
    def __init__(self, size):
        self.head = 0  # 队头元素下标
        self.tail = 0  # 下一个插入位置
        self._arr = [None] * size  # 实际存放数据的数组

    def is_empty(self):
        return self.head == self.tail

    def is_full(self):
        return self.size() == len(self._arr) - 1

    def size(self):
        return (len(self._arr) + self.tail - self.head) % len(self._arr)

    def enqueue(self, item):
        # 队列满了则抛出异常
        if self.is_full():
            raise LookupError('Queue is full')
        self._arr[self.tail] = item
        self.tail = (self.tail + 1) % len(self._arr)

    def dequeue(self):
        # 队列空则抛出异常
        if self.is_empty():
            raise LookupError('Queue underflow')
        item = self._arr[self.head]
        self._arr[self.head] = None
        self.head = (self.head + 1) % len(self._arr)
        return item

    def __iter__(self):
        while not self.is_empty():
            yield self.dequeue()


if __name__ == '__main__':
    q = ArrayQueue(6)
    q.enqueue(1)
    q.enqueue(2)
    q.enqueue(3)
    q.enqueue(4)
    q.enqueue(5)
    print(q.dequeue())
    print(q.dequeue())
    print(q.dequeue())
    print(q.dequeue())
    print(q.dequeue())
    q.enqueue(1)
    q.enqueue(2)
    q.enqueue(3)
    q.enqueue(4)
    q.enqueue(5)
    print(q.dequeue())
    print(q.dequeue())
    print(q.dequeue())
    print(q.dequeue())
    print(q.dequeue())
