# -*- encoding: utf-8 -*-
"""
232. 用栈实现队列
请你仅使用两个栈实现先入先出队列。队列应当支持一般队列支持的所有操作（push、pop、peek、empty）

实现 MyQueue 类：
void push(int x) 将元素 x 推到队列的末尾
int pop() 从队列的开头移除并返回元素
int peek() 返回队列开头的元素
boolean empty() 如果队列为空，返回 true ；否则，返回 false

说明：
你只能使用标准的栈操作，也就是只有push to top, peek/pop from top, size,和is empty作是合法的。
你所使用的语言也许不支持栈。你可以使用 list 或者 deque（双端队列）来模拟一个栈，只要是标准的栈操作即可。

算法思路：
两个栈，左边栈用于最终存放数据，右边栈只是临时来交换数据用。每次push新数据的时候，
先将左边栈所有的数据一个个压到右边栈，然后将新数据压到左边栈底，再将右边栈一个个压到左边栈。
"""


class ListNode:
    def __init__(self, val_, next_=None):
        self.val = val_
        self.next = next_

    def __str__(self):
        return str(self.val)


class MyStack:
    def __init__(self):
        self.first = None

    def push(self, val):
        self.first = ListNode(val, self.first)

    def pop(self):
        if not self.first:
            return None
        res = self.first.val
        self.first = self.first.next
        return res

    def empty(self):
        return self.first is None


class MyQueue:

    def __init__(self):
        self.left_stack = MyStack()
        self.right_stack = MyStack()

    def push(self, x: int) -> None:
        # 先将左栈全部压入右栈
        while not self.left_stack.empty():
            self.right_stack.push(self.left_stack.pop())
        # 然后将新数据压入左栈底
        self.left_stack.push(x)
        # 最后将右栈全部压入左栈
        while not self.right_stack.empty():
            self.left_stack.push(self.right_stack.pop())

    def pop(self) -> int:
        if self.left_stack.empty():
            return None
        return self.left_stack.pop()

    def peek(self) -> int:
        if self.left_stack.empty():
            return None
        return self.left_stack.first.val

    def empty(self) -> bool:
        return self.left_stack.empty()


if __name__ == '__main__':
    # Your MyQueue object will be instantiated and called as such:
    obj = MyQueue()
    obj.push(1)
    obj.push(2)
    obj.push(3)
    param_2 = obj.pop()
    param_3 = obj.peek()
    param_4 = obj.empty()
    print(param_2, param_3, param_4)
