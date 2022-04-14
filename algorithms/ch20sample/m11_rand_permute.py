#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# 随机排列数组算法
"""
    Topic: sample
    Desc : 随机排列数组算法
        第一种算法：
        对给定的数组A，我们对每个A[i]生成一个随机的优先级
        然后根据这个优先级对A进行排序，这个排序需要O(nlg(n))复杂度
        第二种算法：
        原址排列给定数组，在O(n)时间内完成，在进行第i次迭代时，
        A[i]从A[i]至A[n]中随机选取。之后A[i]就再也不变了。
"""
from random import randint, shuffle

__author__ = 'Xiong Neng'


def randPermuteBySort(seq):
    """
    对给定的数组A，我们对每个A[i]生成一个随机的优先级
    然后根据这个优先级对A进行排序，这个排序需要O(nlg(n))复杂度
    """
    maxR = pow(len(seq), 3)
    p = []
    for i in range(0, len(seq)):
        p.append(randint(1, maxR))
    seq[:] = [m for (m, n) in sorted(zip(seq, p), key=lambda k: k[1])]


def randPermuteBySwap(seq):
    """
    原址排列给定数组，在O(n)时间内完成，在进行第i次迭代时，
    A[i]从A[i]至A[n]中随机选取。之后A[i]就再也不变了。
    """
    le = len(seq)
    for i in range(0, le):
        swapIndex = randint(i, le - 1)
        seq[i], seq[swapIndex] = seq[swapIndex], seq[i]


if __name__ == '__main__':
    se = [4, 5, 12, 44, 56, 6]
    randPermuteBySort(se)
    print(se)
    se = [4, 5, 12, 44, 56, 6]
    randPermuteBySwap(se)
    print(se)
    se = [4, 5, 12, 44, 56, 6]
    shuffle(se)  # python中的函数
    print(se)
