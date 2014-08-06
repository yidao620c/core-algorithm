#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# 括号匹配
"""
    Topic: 输入字符串，判断是否是合法的括号组合
    Desc :
    大括号{}，中括号[]，小括号()的合法匹配
    比如{[()()]}合法，但是[{()(})]不合法
"""

__author__ = 'Xiong Neng'


def match(arr):
    left = ['{', '[', '(']
    mmap = {'}': '{', ']': '[', ')': '('}
    stack = []
    for c in arr:
        if c in left:
            stack.append(c)
        else:
            if mmap[c] != stack.pop(): return False
    return True


if __name__ == '__main__':
    print(match('[[()()]]'))
    print(match('[[()(])]'))
