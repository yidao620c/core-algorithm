# -*- encoding: utf-8 -*-
"""基于链表实现的一个简单队列
队尾插入元素，队头取元素。就跟在菜市场排队买菜原理是一样的
"""
from algorithms.ch01structure import Node


class LinkedQueue:
    def __init__(self):
        self.first = None  # beginning of queue
        self.last = None  # end of queue
        self.n = 0  # number of elements on queue

    def is_empty(self):
        return self.first is None

    def size(self):
        return self.n

    def enqueue(self, item):
        old_last = self.last
        self.last = Node(item)  # 将新插入的节点变成队尾元素
        if self.is_empty():
            self.first = self.last
        else:
            old_last.next = self.last  # 同时将原来的队尾元素的next指向新的队尾元素

    def dequeue(self):
        if self.is_empty():
            raise LookupError('Queue underflow')
        item = self.first.val
        self.first = self.first.next
        self.n -= 1
        if self.is_empty():
            # 如果队列现在为空了，说明之前队列中只有一个元素了。
            # 这时候需要把last赋空，防止一直引用着对象，导致无法内存回收
            self.last = None
        return item

    def __iter__(self):
        while self.n > 0:
            yield self.dequeue()
