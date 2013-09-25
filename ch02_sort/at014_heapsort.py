#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# at014_heapsort: 堆排序
"""
    Topic: sample
    Desc : 堆排序
        堆排序的时间复杂度是O(nlg(n))，并且具有空间原址性
        二叉堆heap是一种数据结构，可用来实现优先队列
        给定一个节点的下标i(下标从0开始)，则其父节点、坐孩子、右孩子坐标：
        parent(i) = floor((i+1)/2 - 1) = ((i + 1) >> 1) - 1
        left(i) = 2*i + 1 = (i << 1) + 1
        right(i) = 2*i + 2 = (i + 1) << 1

        最小堆定义： 所有i必须满足A[parent(i)] <= A[i]
        最大堆定义： 所有i必须满足A[parent(i)] >= A[i]

        在堆排序中，我们使用最大堆
        在优先队列算法中，使用最小堆
"""
__author__ = 'Xiong Neng'


def heapSort(heap):
    """
    堆排序算法
    """
    __buildMaxHeap(heap)
    for i in range(heap[2] - 1, 0, -1):
        heap[0][0], heap[0][i] = heap[0][i], heap[0][0]
        heap[1] -= 1
        __maxHeapify(heap, 0)


def __maxHeapify(heap, i):
    """
    前提是i的两棵子树left(i)和right(i)的二叉树都是最大堆了
    现在加入i节点后，要保持这个二叉树为最大堆的性质
    heap: 一个包含[seq，heapSize，length]的数组
    """
    seq = heap[0]
    slen = heap[1]
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
            i = largest
        else:
            break


def __buildMaxHeap(heap):
    """
    由完全二叉树的性质可知：对于 n/2..n-1为下标的元素，都是叶子节点，
    那么可从下标floor((i+1)/2 - 1)开始往前到0的元素调用maxHeapify
    heap: 一个包含[seq，heapSize，length]的数组
    """
    slen = heap[1] = heap[2]
    for i in range(((slen + 1) >> 1) - 1, -1, -1):
        __maxHeapify(heap, i)


if __name__ == '__main__':
    h = [[9, 7, 8, 10, 16, 3, 14, 2, 1, 4], 0, 10]
    heapSort(h)
    print(h[0])

