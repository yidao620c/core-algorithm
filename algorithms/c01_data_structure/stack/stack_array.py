# -*- encoding: utf-8 -*-
"""
基于数组实现的栈结构
"""
from algorithms.c01_data_structure import Node


class ArrayStack:
    def __init__(self, size):
        self.items = [None] * size  # 初始数组大小
        self.size = size  # size of the stack
        self.num = 0  # 元素的个数

    def push(self, item):
        """
        入栈操作
        :param item: 入栈数据
        :return: 是否入栈成功
        """
        # 数组空间不够了，直接返回false，入栈失败。
        if self.num == self.size:
            return False
        # 将item放到下标为num的位置，并且num加一
        self.items[self.num] = Node(item)
        self.num += 1
        return True

    def pop(self):
        if self.num == 0:
            return None
        result = self.items[self.num - 1].data
        self.items[self.num - 1] = None
        self.num -= 1
        return result

    def peek(self):
        if self.num == 0:
            return None
        return self.items[0].data

    def __iter__(self):
        while self.num > 0:
            yield self.pop()


if __name__ == '__main__':
    s = ArrayStack(3)
    s.push(1)
    s.push(2)
    s.push(3)
    print("-----------------")
    print(s.pop())
    print(s.pop())
    print(s.pop())
    print("=================")
