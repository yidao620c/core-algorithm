#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# 选择排序
"""
    Topic: sample
    Desc : 选择排序
"""
__author__ = 'Xiong Neng'


def selectSort(seq):
    le = len(seq)
    for i in range(le - 1):
        minIndx = i
        for j in range(i, le):
            if seq[minIndx] > seq[j]:
                minIndx = j
        if i != minIndx:
            seq[i], seq[minIndx] = seq[minIndx], seq[i]

if __name__ == '__main__':
    se = [4, 2, 5, 1, 6, 3]
    selectSort(se)
    print(se)