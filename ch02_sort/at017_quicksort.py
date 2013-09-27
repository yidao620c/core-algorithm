#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# at017_quicksort: 快速排序
"""
    Topic: sample
    Desc : 快速排序
        采用分治法思想：
        分解： 将数组A[p..r]划分成两个(也可能是空)的子数组A[p..q-1]和A[q+1..r]，
            使得左边数组中的元素都小于A[p]，而右边数组元素都大于A[p]
        解决： 通过递归调用快速排序，对子数组A[p..q-1]和A[q+1..r]进行排序
        合并： 原址排序，不需要合并，数组已经排好序了

        快速排序的优点：
        最坏情况下时间复杂度为O(n^2)，但是期望时间是O(nlg(n))，
        而且O(nlg(n))隐含常数因子非常的小，而且还是原址排序，
        所以实际中使用最多的排序算法就是快速排序
"""
from random import randint
__author__ = 'Xiong Neng'


def quickSort(seq):
    # __quickSubSort(seq, 0, len(seq) - 1)
    __quickSubSortTail(seq, 0, len(seq) - 1)


def __partition(A, p, r):
    """分解子数组"""
    x = A[r]
    i = p - 1
    for j in range(p, r):
        if A[j] <= x:
            i += 1
            A[i], A[j] = A[j], A[i]
    A[i + 1], A[r] = A[r], A[i + 1]
    return i + 1


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


def __quickSubSort(seq, p, r):
    """递归版本的"""
    if p < r:
        q = __randPartition(seq, p, r)
        __quickSubSort(seq, p, q - 1)
        __quickSubSort(seq, q + 1, r)


def __quickSubSortTail(seq, p, r):
    """循环版本，模拟尾递归，可以大大减少递归栈深度，而且时间复杂度不变"""
    while p < r:
        q = __randPartition(seq, p, r)
        if q - p < r - q:
            __quickSubSortTail(seq, p, q - 1)
            p = q + 1
        else:
            __quickSubSortTail(seq, q + 1, r)
            r = q - 1

if __name__ == '__main__':
    s = [9, 7, 8, 10, 16, 3, 14, 2, 1, 4]
    quickSort(s)
    print(s)
