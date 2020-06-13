# -*- encoding: utf-8 -*-
"""自己实现的一个简单栈，内部使用链表方式，同时将这个栈设计成一个可迭代对象。
可迭代的对象一定不能是自身的迭代器。也就是说，可迭代的对象必须实现`__iter__`方法，但不能实现 `__next__` 方法。
另一方面，迭代器应该一直可以迭代。迭代器的 `__iter__` 方法应该返回自身。
一般可使用生成器函数实现更符合python风格的可迭代对象。
"""
from algorithms.ch01structure import Node


class Stack:
    def __init__(self):
        self.first = None  # top of stack
        self.n = 0  # size of the stack

    def is_empty(self):
        return self.first is None

    def size(self):
        return self.n

    def push(self, item):
        self.first = Node(item, self.first)
        self.n += 1

    def pop(self):
        if self.is_empty():
            raise LookupError('Stack underflow')
        result = self.first.val
        self.first = self.first.next
        self.n -= 1
        return result

    def peek(self):
        if self.is_empty():
            raise LookupError('Stack underflow')
        return self.first.val

    def __iter__(self):
        while self.n > 0:
            yield self.pop()

