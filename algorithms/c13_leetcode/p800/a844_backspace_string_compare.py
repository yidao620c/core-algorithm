# -*- encoding: utf-8 -*-
"""
844. 比较含退格的字符串
给定s和t两个字符串，当它们分别被输入到空白的文本编辑器后，如果两者相等，返回 true 。# 代表退格字符。

注意：如果对空文本输入退格字符，文本继续为空。

输入：s = "ab#c", t = "ad#c"
输出：true
解释：s 和 t 都会变成 "ac"。

输入：s = "ab##", t = "c#d#"
输出：true
解释：s 和 t 都会变成 ""。

输入：s = "a#c", t = "b"
输出：false
解释：s 会变成 "c"，但 t 仍然是 "b"。

算法思路：
用两个栈遍历两个字符串，遇到#号就从栈弹出一个元素。最后再依次对比两个栈的每个元素。
"""


class LinkedNode:
    def __init__(self, val_, next_=None):
        self.val = val_
        self.next = next_

    def __str__(self):
        return str(self.val)


class LinkedStack:
    def __init__(self):
        self.first = None

    def push(self, val):
        self.first = LinkedNode(val, self.first)

    def pop(self):
        if not self.first:
            return None
        res = self.first.val
        self.first = self.first.next
        return res

    def peek(self):
        if not self.first:
            return None
        return self.first.val

    def empty(self):
        return self.first is None

    def __iter__(self):
        while self.first:
            yield self.first.val
            self.first = self.first.next


class Solution:
    def __init__(self):
        self.left_stack = LinkedStack()
        self.right_stack = LinkedStack()

    def backspaceCompare(self, s: str, t: str) -> bool:
        for left_val in s:
            if left_val == '#':
                if not self.left_stack.empty():
                    self.left_stack.pop()
            else:
                self.left_stack.push(left_val)
        for right_val in t:
            if right_val == '#':
                if not self.right_stack.empty():
                    self.right_stack.pop()
            else:
                self.right_stack.push(right_val)
        while not self.left_stack.empty() and not self.right_stack.empty():
            if self.left_stack.pop() != self.right_stack.pop():
                return False
        if not self.left_stack.empty() and self.right_stack.empty():
            return False
        if self.left_stack.empty() and not self.right_stack.empty():
            return False
        return True


if __name__ == '__main__':
    print(Solution().backspaceCompare("ab##", "c#d#"))
    print(Solution().backspaceCompare("ab#c", "ad#c"))
    print(Solution().backspaceCompare("a#c", "b"))
    print(Solution().backspaceCompare("y#fo##f", "y#f#o##f"))
