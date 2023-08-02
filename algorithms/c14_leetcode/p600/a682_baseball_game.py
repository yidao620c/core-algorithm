# -*- encoding: utf-8 -*-
"""
682. 棒球比赛
你现在是一场采用特殊赛制棒球比赛的记录员。这场比赛由若干回合组成，过去几回合的得分可能会影响以后几回合的得分。

比赛开始时，记录是空白的。你会得到一个记录操作的字符串列表 ops，其中 ops[i] 是你需要记录的第 i 项操作，ops 遵循下述规则：

整数 x - 表示本回合新获得分数 x
"+" - 表示本回合新获得的得分是前两次得分的总和。题目数据保证记录此操作时前面总是存在两个有效的分数。
"D" - 表示本回合新获得的得分是前一次得分的两倍。题目数据保证记录此操作时前面总是存在一个有效的分数。
"C" - 表示前一次得分无效，将其从记录中移除。题目数据保证记录此操作时前面总是存在一个有效的分数。
请你返回记录中所有得分的总和。

输入：ops = ["5","2","C","D","+"]
输出：30
解释：
"5" - 记录加 5 ，记录现在是 [5]
"2" - 记录加 2 ，记录现在是 [5, 2]
"C" - 使前一次得分的记录无效并将其移除，记录现在是 [5].
"D" - 记录加 2 * 5 = 10 ，记录现在是 [5, 10].
"+" - 记录加 5 + 10 = 15 ，记录现在是 [5, 10, 15].
所有得分的总和 5 + 10 + 15 = 30

输入：ops = ["5","-2","4","C","D","9","+","+"]
输出：27
解释：
"5" - 记录加 5 ，记录现在是 [5]
"-2" - 记录加 -2 ，记录现在是 [5, -2]
"4" - 记录加 4 ，记录现在是 [5, -2, 4]
"C" - 使前一次得分的记录无效并将其移除，记录现在是 [5, -2]
"D" - 记录加 2 * -2 = -4 ，记录现在是 [5, -2, -4]
"9" - 记录加 9 ，记录现在是 [5, -2, -4, 9]
"+" - 记录加 -4 + 9 = 5 ，记录现在是 [5, -2, -4, 9, 5]
"+" - 记录加 9 + 5 = 14 ，记录现在是 [5, -2, -4, 9, 5, 14]
所有得分的总和 5 + -2 + -4 + 9 + 5 + 14 = 27

算法思路：
跟加减乘除思路类似，这里的C、D、+代表操作符，优先级一样。
准备两个栈，左栈作为操作数，右栈作为操作符。遇到数字压入左栈，遇到操作符根据规则进行计算即可。
"""
from typing import List


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

    def calPoints(self, ops: List[str]) -> int:
        for op in ops:
            if self.is_number(op):
                self.left_stack.push(int(op))
            else:
                if op == 'C':
                    self.left_stack.pop()
                elif op == 'D':
                    self.left_stack.push(self.left_stack.peek() * 2)
                elif op == '+':
                    self.left_stack.push(self.left_stack.peek() + self.left_stack.first.next.val)
        return sum(self.left_stack)

    def is_number(self, str_):
        try:
            int(str_)
            return True
        except ValueError:
            return False


if __name__ == '__main__':
    print(Solution().calPoints(["5", "2", "C", "D", "+"]))
