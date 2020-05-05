#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# 前i个最小数
"""
    Topic: sample
    Desc : 前i个最小数
        先通过找到第i小的数，然后将这个数作为pivot去划分这个数组，
        左边 + 这个pivot即是解
"""
from algorithms.ch02sort.m12_imin_select2 import iminSelect2


def iminList(A, i):
    seq = A[:]  # 不改变A
    imin = iminSelect2(seq, i)
    print('imin=%d' % imin)
    pivotIndex = __midPartition(seq, 0, len(seq) - 1, imin)
    return seq[0: pivotIndex + 1]


def __midPartition(A, p, r, midNum):
    """分解子数组： 指定pivot的版本"""
    midIndex = p
    for ii in range(p, r + 1):
        if A[ii] == midNum:
            midIndex = ii
            break
    A[midIndex], A[r] = A[r], A[midIndex]  # 还是将这个pivot放到最后
    x = A[r]
    i = p - 1
    for j in range(p, r):
        if A[j] <= x:
            i += 1
            A[i], A[j] = A[j], A[i]
    A[i + 1], A[r] = A[r], A[i + 1]
    return i + 1


if __name__ == '__main__':
    print(iminList([4, 23, 65, 3, 22, 3, 34, 3, 67, 3, 12, 3, 7, 1, 1, 256, 3, 34, 27], 10))
