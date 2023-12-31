#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
Topic: 动态规划O(n)时间内实现fibonacci数列
Desc :
"""


def dynamic_fibo(n):
    r = [1, 1]
    for i in range(2, n):
        r.append(r[i - 2] + r[i - 1])
    return r


if __name__ == '__main__':
    print(dynamic_fibo(10))
