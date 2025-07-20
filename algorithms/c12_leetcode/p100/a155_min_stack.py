# -*- encoding: utf-8 -*-
"""
155. 最小栈
设计一个支持 push、pop、top 操作，并能在常数时间内检索到最小元素的栈。

实现 MinStack 类:

MinStack() 初始化堆栈对象。
void push(int val) 将元素val推入堆栈。
void pop() 删除堆栈顶部的元素。
int top() 获取堆栈顶部的元素。
int getMin() 获取堆栈中的最小元素。

算法思路：
通过空间换时间的方法。将每次入栈的节点包装成一个对象，存储两个信息，一个是节点值，一个是当前栈的最小值。
这样获取栈顶元素就同时能获取到这两个值了。
"""
from algorithms.c01_data_structure import Node


class MinStack:

    def __init__(self):
        self.first = None  # top of stack

    def push(self, val: int) -> None:
        current_min = self.getMin()
        min_val = min(val, current_min) if current_min is not None else val
        self.first = Node((val, min_val), self.first)

    def pop(self) -> None:
        if self.first:
            self.first = self.first.next

    def top(self) -> int:
        if not self.first:
            return None
        return self.first.data[0]

    def getMin(self) -> int:
        if not self.first:
            return None
        return self.first.data[1]


if __name__ == '__main__':
    pass
    # Your MinStack object will be instantiated and called as such:
    obj = MinStack()
    obj.push(0)
    obj.push(1)
    obj.push(0)
    print(obj.getMin())
    obj.pop()
    print(obj.getMin())
