#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# 在数组中同时找出最小和最大的
"""
    Topic: sample
    Desc : 在数组中同时找出最小和最大的
        算法描述：如果n是奇数，最小和最大初始化为第一个元素，
        如果是偶数，先对前两个元素比较，决定最小和最大初值。
"""
__author__ = 'Xiong Neng'


def minMax(A):
    n = len(A)
    if n % 2 == 0:
        lastMin, lastMax = (A[0], A[1]) if A[0] < A[1] else (A[1], A[0])
    else:
        lastMin = lastMax = A[0]
    for i in range(0, (n + 1) // 2 - 1):
        tmp1 = A[2 * i + 1]
        tmp2 = A[2 * i + 2]
        tmpMin, tmpMax = (tmp1, tmp2) if tmp1 < tmp2 else (tmp2, tmp1)
        lastMin = lastMin if lastMin < tmpMin else tmpMin
        lastMax = lastMax if lastMax > tmpMax else tmpMax
    return lastMin, lastMax


if __name__ == '__main__':
    print(minMax([4, 23, 65, 22, 12, 4, 1, 1, 256, 34, 27]))
