#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# 计数排序
"""
    Topic: sample
    Desc : 计数排序
        实际工作中，如果k=O(n)，那么选择计数排序，线性时间。
        比如排序数组[1, 10*2, 10*3, .... 10*100]，n = 100， k=10n=O(n)，
        那么可以用这个计数排序
        计数排序是稳定的：原数组中相同元素在输出数组中的次序是一样的
"""


def countSort(A, k, offset=0):
    """
    A: 待排序数组
    k: 数组A区间-offset后的最大值
    offset: 有时候A在一个区间内[a,b]，这时候，可以设置offset为a
    """
    if offset > 0:
        A[:] = [p - offset for p in A]
    B = [0] * len(A)  # 最终输出的排序数组
    C = [0] * k  # 临时存储数组
    for i in range(0, len(A)):
        C[A[i]] += 1  # C[i]现在代表数组A中元素等于i的个数
    for i in range(1, k):
        C[i] += C[i - 1]  # C[i]现在代表数组A中元素小于等于i的个数
    for j in range(len(A) - 1, -1, -1):
        B[C[A[j]] - 1] = A[j]
        C[A[j]] -= 1  # 防止数组A有重复的数，占据了相同的位置
    A[:] = B[:]
    if offset > 0:
        A[:] = [p + offset for p in A]


if __name__ == '__main__':
    A = [9, 7, 8, 10, 16, 3, 14, 2, 1, 4]
    countSort(A, 20)
    print(A)
    A = [9, 7, 8, 10, 16, 3, 14, 2, 1, 4]
    B = [100 + p for p in A]
    countSort(B, 30, 96)
    print(B)
