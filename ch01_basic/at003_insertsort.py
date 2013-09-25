#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# at003_insertsort: 插入排序
"""
    Topic: sample
    Desc : 插入排序
        由于其内层循环非常紧凑，对于小规模的输入，
        插入排序是一种非常快的原址排序算法
        注： 如果输入数组中仅有常数个元素需要在排序过程中存储在数组外，
            则称这种排序算法是原址的。
"""
__author__ = 'Xiong Neng'


def insertSort(seq):
    for j in range(1, len(seq)):
        key = seq[j]
        # insert arrays[j] into the sorted seq[0...j-1]
        i = j - 1
        while i >= 0 and seq[i] > key:
            seq[i + 1] = seq[i]
            i -= 1
        seq[i + 1] = key

if __name__ == '__main__':
    seq = [5, 2, 4, 6, 1, 3]
    insertSort(seq)
    print(seq)