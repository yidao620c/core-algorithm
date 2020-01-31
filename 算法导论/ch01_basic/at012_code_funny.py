#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# 编程之美的几个小算法
"""
    Topic: sample
    Desc : 编程之美的几个小算法
"""
__author__ = 'Xiong Neng'


def list_chess():
    """
    打印连个将/帅的所有合法的位置，
    用1..9标明第一个将9个位置，1..9标明第二个帅
    """
    for i in range(1, 10):
        print([(i, k) for k in range(1, 10) if abs(k - i) % 3 != 0])


if __name__ == '__main__':
    list_chess()
