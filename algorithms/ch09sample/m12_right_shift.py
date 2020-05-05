#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# 数组循环右移
"""
    Topic: sample
    Desc : 数组循环右移
"""
__author__ = 'Xiong Neng'


def right_shift(seq, k):
    n = len(seq)
    k %= n
    seq[0:n - k] = seq[n - k - 1::-1]
    seq[n - k: n] = seq[:n - k - 1:-1]
    seq[:] = seq[::-1]


if __name__ == '__main__':
    s = list('abcd1234')
    right_shift(s, 4)
    print(s)
