#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# 冒泡排序
"""
    Topic: sample
    Desc : 冒泡排序
"""
__author__ = 'Xiong Neng'


def bubbleSort(seq):
    for i in range(len(seq)):
        for j in range(len(seq) - 1, i, -1):
            if seq[j] < seq[j - 1]:
                seq[j - 1], seq[j] = seq[j], seq[j - 1]


if __name__ == '__main__':
    s = [4, 6, 2, 5, 7, 9, 8, 1]
    bubbleSort(s)
    print(s)
