#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# 寻找最大子数组(非递归的线性时间算法)
"""
    Topic: sample
    Desc : 寻找最大子数组(非递归的线性时间算法)
        从数组A的左边界开始，从左至右记录目前已经找到了的最大子数组
        若已知A[0..j]的最大子数组为A[m..n]，基于如下性质扩展到A[0..j+1]：
        A[0..j+1]的最大子数组要么就是A[0..j]的最大子数组，要么是某个子数组
        A[i..j+1](0<=i<=j+1)。这样可以在线性时间内找到这个子数组
"""
__author__ = 'Xiong Neng'


def maxSubArr(seq):
    maxSubTuple = (0, 0, seq[0])  # 最大子数组先初始化为数组第一个元素
    for i in range(1, len(seq)):
        tmpMax = float('-Inf')
        tmpSum = 0
        for j in range(i, maxSubTuple[1], -1):
            tmpSum += seq[j]
            if tmpSum > tmpMax:
                tmpMax = tmpSum
                tmpLow = j
        r1 = (tmpLow, i, tmpMax)
        r2 = (maxSubTuple[0], i, maxSubTuple[2] + tmpSum)
        maxSubTuple = max([maxSubTuple, r1, r2], key=lambda k: k[2])
    return maxSubTuple


if __name__ == '__main__':
    print(maxSubArr([13, -3, -25, 20, -3, -16, -23, 18, 20, -7, 12, -5, -22, 15, -4, 7]))
