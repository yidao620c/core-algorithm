#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# at006_mergesort: 归并排序(分治法)
"""
    Topic: sample
    Desc : 归并排序
        归并排序算法完全遵循分治模式，操作如下：
        分解： 分解待排序的n个元素序列成各具n/2个元素的两个子序列
        解决： 使用归并排序递归的排序两个子序列
        合并： 合并两个已排序的子序列以产生已排序的答案
"""
__author__ = 'Xiong Neng'


def mergeSort(seq):
    mergeSortRange(seq, 0, len(seq) - 1)


def mergeOrderedSeq(seq, left, middle, right):
    """
    seq: 待排序序列
    left <= middle <= right
    子数组seq[left..middle]和seq[middle+1..right]都是排好序的
    该排序的时间复杂度为O(n)
    """
    tempSeq = []
    i = left
    j = middle + 1
    while i <= middle and j <= right:
        if seq[i] <= seq[j]:
            tempSeq.append(seq[i])
            i += 1
        else:
            tempSeq.append(seq[j])
            j += 1
    if i <= middle:
        tempSeq.extend(seq[i:middle + 1])
    else:
        tempSeq.extend(seq[j:right + 1])
    seq[left:right + 1] = tempSeq[:]


def mergeSortRange(seq, start, end):
    """
    归并排序一个序列的子序列
    start: 子序列的start下标
    end: 子序列的end下标
    """
    if start < end:  # 如果start >= end就终止递归调用
        middle = (start + end) / 2
        mergeSortRange(seq, start, middle)  # 排好左边的一半
        mergeSortRange(seq, middle + 1, end)  # 再排好右边的一半
        mergeOrderedSeq(seq, start, middle, end)  # 最后合并排序结果


if __name__ == '__main__':
    aa = [4, 2, 5, 1, 6, 3, 7, 9, 8]
    mergeSort(aa)
    print(aa)