#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# 基数排序
"""
    Topic: sample
    Desc : 基数排序
        有时需要对记录的几个关键字分别排序，比如用三个关键字年、月、日对日期排序。
        可以用基数排序，用一种稳定排序算法(比如计数排序)对这些信息进行三次排序：
        优先级从低到高，权重从低到高。
"""


def radixSort(A, digit, base):
    """
    digit: 代表排序数组的最大位数
    base:  代表进制
    """
    for di in range(1, digit + 1):
        B = [0] * len(A)  # 最终输出的排序数组
        C = [0] * base  # 临时存储数组
        for i in range(0, len(A)):
            # split the specified digit from the element
            tmpSplitDigit = A[i] // pow(10, di - 1) - (A[i] // pow(10, di)) * 10
            C[tmpSplitDigit] += 1  # C[i]现在代表数组A中元素等于i的个数
        for i in range(1, base):
            C[i] += C[i - 1]  # C[i]现在代表数组A中元素小于等于i的个数
        for j in range(len(A) - 1, -1, -1):
            tmpSplitDigit = A[j] // pow(10, di - 1) - (A[j] // pow(10, di)) * 10
            B[C[tmpSplitDigit] - 1] = A[j]
            C[tmpSplitDigit] -= 1  # 防止数组A有重复的数，占据了相同的位置
        A[:] = B[:]


if __name__ == '__main__':
    A = [9, 7, 8, 10, 16, 3, 14, 2, 1, 4]
    radixSort(A, 2, 10)
    print(A)
