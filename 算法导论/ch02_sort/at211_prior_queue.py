#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# 最大堆实现最大优先级队列
"""
    Topic: sample
    Desc : 最大堆实现最大优先级队列
"""
from 算法导论 import ch02_sort as hsort

__author__ = 'Xiong Neng'


class Item():
    def __init__(self, val, key, index=-1):
        self.val = val
        self.key = key
        self.index = index

    def __cmp__(self, other):
        if self.key > other.key:
            return 1
        else:
            return -1 if self.key < other.key else 0

    def __str__(self):
        return str((self.val, self.key, self.index))


def heapGetMax(heap):
    """返回最大优先队列中取最大值"""
    return heap.seq[0]


def heapPopMax(heap):
    """弹出最大优先队列中取最大值并返回这个值"""
    if heap.heapSize < 1:
        return None
    re = heap.seq[0]
    heap.seq[0] = heap.seq[heap.heapSize - 1]  # 尾上的弄到头上去
    heap.heapSize -= 1  # heap的大小-1
    __maxHeapify(heap, 0)  # 然后再次将其构建为最大堆
    return re


def heapIncreaseKey(heap, item, newKey):
    """增加队列中元素item的key为新的newKey, key <= newKey"""
    if newKey < item.key:
        return
    item.key = newKey
    while True:
        tmpItem = item
        iindex = tmpItem.index
        pindex = ((tmpItem.index + 1) >> 1) - 1
        if iindex > 0 and heap.seq[pindex] < tmpItem:
            heap.seq[iindex], heap.seq[pindex] = heap.seq[pindex], heap.seq[iindex]
            heap.seq[iindex].index, heap.seq[pindex].index = iindex, pindex
        else:
            break


def heapInsert(heap, item):
    """最大优先队列中插入一条元素item，将其放入队列到最后一个位置，
    然后调用heapIncreaseKey"""
    heap.heapSize += 1
    item.index = heap.heapSize - 1
    heap.seq[heap.heapSize - 1] = item
    heapIncreaseKey(heap, item, item.key)


def __maxHeapify(heap, i):
    """
    前提是i的两棵子树left(i)和right(i)的二叉树都是最大堆了
    现在加入i节点后，要保持这个二叉树为最大堆的性质
    heap: Heap数据结构
    """
    seq = heap.seq
    slen = heap.heapSize
    while True:
        left = (i << 1) + 1
        right = (i + 1) << 1
        if left < slen and seq[left] > seq[i]:
            largest = left
        else:
            largest = i
        if right < slen and seq[right] > seq[largest]:
            largest = right
        if largest != i:
            seq[largest], seq[i] = seq[i], seq[largest]
            seq[largest].index, seq[i].index = seq[i].index, seq[largest].index
            i = largest
        else:
            break


def __buildMaxHeap(heap):
    """
    由完全二叉树的性质可知：对于 n/2..n-1为下标的元素，都是叶子节点，
    那么可从下标floor((i+1)/2 - 1)开始往前到0的元素调用maxHeapify
    heap: Heap数据结构
    """
    slen = heap.heapSize
    for i in range(((slen + 1) >> 1) - 1, -1, -1):
        __maxHeapify(heap, i)
    for i in range(heap.heapSize):
        heap.seq[i].index = i


if __name__ == '__main__':
    iSeq = [9, 7, 8, 10, 16, 3, 14, 2, 1, 4]
    iVal = ['9', '7', '8', '10', '16', '3', '14', '2', '1', '4']
    iVal = [2 * k for k in iVal]
    pa = zip(iVal, iSeq)
    lastParm = [Item(v, k) for (v, k) in pa]
    lastParm.extend([None] * 100)
    heap = hsort.Heap(lastParm, len(iSeq), len(lastParm))
    __buildMaxHeap(heap)
    print([str(k) for k in heap.seq if k])

    heapInsert(heap, Item('Love', 13))
    print([str(k) for k in heap.seq if k])
