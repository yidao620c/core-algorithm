#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# at007_mergesort: 归并排序中对小数组采用插入排序
"""
    Topic: sample
    Desc : 归并排序中对小数组采用插入排序
        纯归并排序的复杂度为： O(nlgn)，而纯插入排序的时间复杂度为：O(n^2)。数据量很大的时候采用归并排序
        但是在n较小的时候插入排序可能运行的会更快点。因此在归并排序中当子问题变得足够小时，
        采用插入排序来使得递归的叶子变粗可以加快排序速度。那么这个足够小到底怎么去衡量呢？ 请看下面：
        这么几个我不证明了，比较简单：
        A，插入排序最坏情况下可以在O(nk)时间内排序每个长度为k的n/k个子列表
        B，在最坏情况下可在O(nlg(n/k))的时间内合并这些子表
        C，修订后的算法的最坏情况运行时间复杂度是O(nk + nlg(n/k))
        那么，O(nk+nlg(n/k))=O(nlgn).只能最大是k=O(lgn).等式左边中第一项是高阶项。
        k如果大于lgn,则比归并排序复杂度大了。左边可以写成nk+nlgn-nlgk，k等于lgn时，
        就是2nlgn-nlglgn.忽略恒定系数，则与归并排序是一样的。
        最后结论：  k < lg(n)的时候，使用插入排序
"""
from at003_insertsort import insertSort
from math import log

__author__ = 'Xiong Neng'


def mergeSort(seq):
    mergeSortRange(seq, 0, len(seq) - 1, log(len(seq)) - 1)


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


def mergeSortRange(seq, start, end, threshold):
    """
    归并排序一个序列的子序列
    start: 子序列的start下标
    end: 子序列的end下标
    threshold: 待排序长度低于这个值，就采用插入排序
    """
    if end - start < threshold:
        tempSeq = seq[start: end + 1]
        insertSort(tempSeq)
        seq[start: end + 1] = tempSeq[:]
    elif start < end:  # 如果start >= end就终止递归调用
        middle = (start + end) / 2
        mergeSortRange(seq, start, middle, threshold)  # 排好左边的一半
        mergeSortRange(seq, middle + 1, end, threshold)  # 再排好右边的一半
        mergeOrderedSeq(seq, start, middle, end)  # 最后合并排序结果


if __name__ == '__main__':
    aa = [4, 2, 5, 1, 6, 3, 7, 9, 8]
    mergeSort(aa)
    print(aa)