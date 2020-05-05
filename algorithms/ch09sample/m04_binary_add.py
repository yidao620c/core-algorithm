#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# 两个N位的二进制数相加
"""
    Topic: sample
    Desc : 两个N位的二进制数相加
"""
__author__ = 'Xiong Neng'


def biAdd(a, b):
    res = []
    m = 0
    r = list(range(0, len(a)))
    r.reverse()
    for i in r:
        m, n = divmod(a[i] + b[i] + m, 2)
        res.insert(0, n)
    res.insert(0, m)
    return res


if __name__ == '__main__':
    print(biAdd([0, 1, 0, 1, 1, 0], [1, 1, 0, 1, 1, 0]))
