# -*- encoding: utf-8 -*-
"""
224. 基本计算器

给你一个字符串表达式 s ，请你实现一个基本计算器来计算并返回它的值。

注意:不允许使用任何将字符串作为数学表达式计算的内置函数，比如 eval()。

输入：s = "1 + 1"
输出：2

输入：s = " 2-1 + 2 "
输出：3

输入：s = "(1+(4+5+2)-3)+(6+8)"
输出：23

算法描述：使用两个栈来实现。
正常不带括号的+-*/运算的逻辑：
    1）操作数有优先级，+-优先级低，*/优先级高。
    2）左栈压入数字，右栈压入操作数。
    3）每次向右栈压入操作数的时候，先对比栈顶操作数跟当前要入栈操作数优先级。
       i：如果当前入栈优先级高，就直接入栈。
       ii：否则将栈顶操作数弹出，并从左栈弹出2个数来做运算。将结果再次压入左栈
       iii：最后将当前要入栈的操作数入栈
    4）循环结束后，如果操作数栈还有剩余操作数。就每次右栈弹1个操作数，左栈弹2个数做运算。结果入左栈
    5）最后判断左栈是否只剩下一个数，如果是则返回结果。否则表达式有问题，报错。

带括号()的+-*/运算的逻辑：
    1）操作数有优先级，+-优先级低，*/优先级高。
    2）左栈压入数字，右栈压入操作数。
    3）每次向右栈压入操作数的时候逻辑如下：
       i：如果碰到(直接入栈。
       ii：如果当前为操作符+-*/，并且栈顶为(，直接入栈。
       iii：如果当前为操作符+-*/，并且栈顶不为(，则对比两者优先级
           iii-a：如果当前入栈优先级高，就直接入栈。
           iii-b：否则将栈顶操作数弹出，并从左栈弹出2个数来做运算。将结果再次压入左栈。然后再将当前操作符压入右栈
       IV：如果当前为操作符)，则循环从右栈弹1个操作数，左栈弹2个数做运算压入左栈。直到弹出第一个(为止。
    4）循环结束后，如果操作数栈还有剩余操作数。就每次右栈弹1个操作数，左栈弹2个数做运算。结果入左栈
    5）最后判断左栈是否只剩下一个数，如果是则返回结果。否则表达式有问题，报错。
"""
import re


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


class Solution:
    def __init__(self):
        self.left_stack = LinkedStack()
        self.right_stack = LinkedStack()
        self.calc_funcs = {
            '+': lambda a, b: a + b,
            '-': lambda a, b: a - b,
            '*': lambda a, b: a * b,
            '/': lambda a, b: a / b,
        }

    def calculate(self, s: str) -> int:
        expression = s.replace(' ', '')  # 去掉空格
        expression = '0' + expression if expression.startswith('-') else expression
        expression = expression.replace('(-', '(0-')
        expression_list = [s for s in re.split(r'([()+*/])|((?<=[\d)])-)', expression) if s]
        for c in expression_list:
            if self.is_number(c):
                self.left_stack.push(int(c))
            else:
                if c == '(':
                    self.right_stack.push(c)
                elif c in '+-*/' and self.right_stack.peek() == '(':
                    self.right_stack.push(c)
                elif c in '+-*/' and self.right_stack.peek() != '(':
                    if c in '*/' and self.right_stack.peek() in '+-':
                        self.right_stack.push(c)
                    else:
                        self.calc_unit()
                        self.right_stack.push(c)
                elif c == ')':
                    while self.right_stack.peek() != '(':
                        self.calc_unit()
                    self.right_stack.pop()
                else:
                    raise ValueError('wrong cal expression')
        while not self.right_stack.empty():
            self.calc_unit()
        if self.left_stack.first.next is not None:
            raise ValueError('wrong input expression')
        return self.left_stack.pop()

    def is_number(self, str_):
        try:
            int(str_)
            return True
        except ValueError:
            return False

    def calc_unit(self):
        if self.right_stack.empty():
            return
        cal = self.right_stack.pop()
        val2 = self.left_stack.pop()
        val1 = self.left_stack.pop()
        if val2 is None or val1 is None:
            raise ValueError('wrong number expression')
        self.left_stack.push(self.calc_funcs[cal](val1, val2))


if __name__ == '__main__':
    print(Solution().calculate("- (3 - (- (4 + 5) ) )"))
