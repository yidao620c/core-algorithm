#!/usr/bin/env python
"""快速排序
    采用分治法思想：
    分解： 将数组A[p..r]划分成两个(也可能是空)的子数组A[p..q-1]和A[q+1..r]，
        使得左边数组中的元素都小于A[p]，而右边数组元素都大于A[p]
    解决： 通过递归调用快速排序，对子数组A[p..q-1]和A[q+1..r]进行排序
    合并： 原址排序，不需要合并，数组已经排好序了

    快速排序的优点：
    最坏情况下时间复杂度为O(n^2)，但是期望时间是O(nlg(n))，
    而且O(nlg(n))隐含常数因子非常的小，而且还是原址排序，
    所以实际中使用最多的排序算法就是快速排序

    性质T：快速排序是最快的通用排序算法。
"""
from random import randint

from algorithms.ch02sort.base.template import SortTemplate


class QuickSort(SortTemplate):

    def sort(self):
        # self._quick_sub_sort_recursive(seq, 0, len(seq) - 1)
        self._quick_sub_sort_tail(0, len(self.seq) - 1)

    def _quick_sub_sort_tail(self, start, end):
        """循环版本，模拟尾递归，可以大大减少递归栈深度，而且时间复杂度不变"""
        while start < end:
            pivot = self._rand_partition(start, end)
            if pivot - start < end - pivot:
                self._quick_sub_sort_tail(start, pivot - 1)
                start = pivot + 1
            else:
                self._quick_sub_sort_tail(pivot + 1, end)
                end = pivot - 1

    def _rand_partition(self, start, end):
        """分解子数组： 随机化版本"""
        pivot = randint(start, end)  # 随机的pivot
        # 还是将这个pivot放到最后
        self.seq[pivot], self.seq[end] = self.seq[end], self.seq[pivot]
        pivot_value = self.seq[end]
        i = start - 1  # 以退为进，先初始化为start-1
        for j in range(start, end):
            if self.seq[j] <= pivot_value:
                i += 1
                self.seq[i], self.seq[j] = self.seq[j], self.seq[i]
        self.seq[i + 1], self.seq[end] = self.seq[end], self.seq[i + 1]
        return i + 1

    def _quick_sub_sort_recursive(self, start, end):
        """递归版本的"""
        if start < end:
            q = self._rand_partition(start, end)
            self._quick_sub_sort_recursive(start, q - 1)
            self._quick_sub_sort_recursive(q + 1, end)


if __name__ == '__main__':
    quick_sort = QuickSort([9, 7, 8, 10, 16, 3, 14, 2, 1, 4])
    quick_sort.main()
