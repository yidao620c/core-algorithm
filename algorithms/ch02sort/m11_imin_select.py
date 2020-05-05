#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# 顺序统计量的选择算法
"""
    Topic: sample
    Desc : 顺序统计量的选择算法
        pivot加入了随机特性，算法的期望运行时间是O(n)
"""
from random import randint

__author__ = 'Xiong Neng'


def iminSelect(A, i):
    """
    返回数组A中第i小的元素
    """
    return __iminSelect(A, 0, len(A) - 1, i)


def __iminSelect(A, p, r, i):
    """
    返回数组A[p..r]中第i小的元素
    """
    if p == r:
        return A[p]
    q = __randPartition(A, p, r)
    k = q - p + 1
    if i == k:
        return A[q]
    elif i < k:
        return __iminSelect(A, p, q - 1, i)
    else:
        return __iminSelect(A, q + 1, r, i - k)


def __randPartition(A, p, r):
    """分解子数组： 随机化版本"""
    rinx = randint(p, r)  # 随机的pivot
    A[rinx], A[r] = A[r], A[rinx]  # 还是将这个pivot放到最后
    x = A[r]
    i = p - 1
    for j in range(p, r):
        if A[j] <= x:
            i += 1
            A[i], A[j] = A[j], A[i]
    A[i + 1], A[r] = A[r], A[i + 1]
    return i + 1


if __name__ == '__main__':
    print(iminSelect([4, 23, 65, 22, 12, 3, 7, 1, 256, 34, 27], 3))
