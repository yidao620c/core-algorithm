#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# 桶排序
"""
    Topic: sample
    Desc : 桶排序
        桶排序假设数据服从均匀分布，平均情况下它的代价为O(n)
        桶排序假定输入是由一个随机过程产生，该过程将元素均匀、独立分布在[0,1)区间上
        将[0,1)区间划分成n个相同大小的子区间，称为桶。然后将n个输入数分别放入桶中
        然后循环n个桶，对每个桶排序，采用插入排序算法
"""
from math import floor

from algorithms.ch02sort.base.sortutil import insert_sort


def bucketSort(A):
    n = len(A)
    B = [[] for i in range(n)]
    for i in range(0, n):
        ind = int(floor(n * A[i]))
        B[ind].append(A[i])
    for i in range(0, n):
        insert_sort(B[i])
    res = []
    for i in range(0, n):
        res.extend(B[i])
    A[:] = res[:]


if __name__ == '__main__':
    AA = [9, 15, 17, 10, 16, 3, 14, 12, 1, 4]
    BB = [i / 20.0 for i in AA]
    print(BB)
    bucketSort(BB)
    print(BB)
