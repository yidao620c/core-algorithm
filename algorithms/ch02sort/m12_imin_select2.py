#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# 顺序统计量的选择算法(最坏情况下O(n))
"""
    Topic: sample
    Desc : 顺序统计量的选择算法(最坏情况下O(n))
        利用中位数的中位数作为pivot划分数组
"""
from algorithms.ch02sort.base.sortutil import insert_sort


def iminSelect2(A, i):
    """
    返回数组A中第i小的元素，返回结果也就是A从小到大排序后第i个元素
    """
    return __iminSelect2(A, 0, len(A) - 1, i)


def __iminSelect2(A, p, r, nn):
    """
    返回数组A[p..r]中第i小的元素
    利用中位数的中位数作为pivot划分数组
    """
    if p == r:
        return A[p]
    midOfMid = __selectMidOfMid(A[p: r + 1])
    midIndex = p
    for i in range(p, r + 1):
        if A[i] == midOfMid:
            midIndex = i
            break
    q = __midPartition(A, p, r, midIndex)
    k = q - p + 1
    if nn == k:
        return A[q]
    elif nn < k:
        return __iminSelect2(A, p, q - 1, nn)
    else:
        return __iminSelect2(A, q + 1, r, nn - k)


def __selectMidOfMid(seq):
    """获取中位数的中位数算法"""
    while len(seq) > 1:
        grpNum, lastNum = divmod(len(seq), 5)  # 分组，每组5个
        midArr = []  # 每组的中位数列表
        for i in range(0, grpNum):
            eachGroup = seq[i * 5: (i + 1) * 5]
            insert_sort(eachGroup)
            midArr.append(eachGroup[2])
        if lastNum > 0:
            lastGroup = seq[grpNum * 5: grpNum * 5 + lastNum]
            insert_sort(lastGroup)
            midArr.append(lastGroup[(lastNum - 1) // 2])
        seq = midArr
    return seq[0]


def __midPartition(A, p, r, midIndex):
    """分解子数组： 中位数作为pivot的版本"""
    A[midIndex], A[r] = A[r], A[midIndex]  # 还是将这个pivot放到最后
    x = A[r]
    i = p - 1
    for j in range(p, r):
        if A[j] <= x:
            i += 1
            A[i], A[j] = A[j], A[i]
    A[i + 1], A[r] = A[r], A[i + 1]
    return i + 1


if __name__ == '__main__':
    bb = [4, 23, 65, 3, 22, 3, 34, 3, 67, 3, 12, 3, 7, 1, 1, 256, 3, 34, 27]
    print(sorted(bb))
    print(iminSelect2(bb, 10))
