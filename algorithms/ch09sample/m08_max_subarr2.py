#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# 寻找最大子数组(对小数组采用暴力算法)
"""
    Topic: sample
    Desc : 寻找最大子数组(对小数组采用暴力算法)
        理论跟归并排序中对小数组采用插入排序一样，有个阀值，直接写结论：
        最后结论：  k < lg(n)的时候，使用暴力算法
"""
from math import log

__author__ = 'Xiong Neng'


def maxSubArr(seq):
    return __findMaxSubArr(seq, 0, len(seq) - 1, log(len(seq), 2))


def __findMaxSubArr(seq, low, high, threshold):
    if high - low + 1 < threshold:
        return __violentSubArr(seq, low, high)
    elif low == high:
        return low, high, seq[low]
    else:
        mid = (low + high) // 2
        l = lefLow, leftHigh, leftSum = __findMaxSubArr(seq, low, mid, threshold)
        r = rightLow, rightHigh, right_sum = __findMaxSubArr(seq, mid + 1, high, threshold)
        c = crossLow, crossHigh, crossSum = __maxCrossingSubArr(seq, low, mid, high)
        return max([l, r, c], key=lambda k: k[2])  # 这个太cool了


def __violentSubArr(seq, low, high):
    maxSum = float('-Inf')
    for i in range(low, high + 1):
        eachSum = 0
        for j in range(i, high + 1):
            eachSum += seq[j]
            if eachSum > maxSum:
                low, high = i, j
                maxSum = eachSum
    return low, high, maxSum


def __maxCrossingSubArr(seq, low, mid, high):
    """
    寻找seq[low..high]跨越了中点mid的最大子数组
    总循环次数为high-low+1，线性的
    """
    leftSum = float('-Inf')
    sumTemp = 0
    for i in range(mid, low - 1, -1):
        sumTemp += seq[i]
        if sumTemp > leftSum:
            leftSum = sumTemp
            maxLeft = i
    rightSum = float('-Inf')
    sumTemp = 0
    for j in range(mid + 1, high + 1):
        sumTemp += seq[j]
        if sumTemp > rightSum:
            rightSum = sumTemp
            maxRight = j
    return maxLeft, maxRight, leftSum + rightSum


if __name__ == '__main__':
    print(maxSubArr([13, -3, -25, 20, -3, -16, -23, 18, 20, -7, 12, -5, -22, 15, -4, 7]))
