#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# at003_insertsort: 插入排序
"""
    Topic: sample
    Desc : 插入排序
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