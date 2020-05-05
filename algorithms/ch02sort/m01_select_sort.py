#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""选择排序
1. 找到数组中最小的元素，将其与第一个元素交换位置（如果第一个元素最小，就啥也不做）。
2. 在剩下的元素中找到最小元素，将其与数组第二个元素交换位置。
3. 如此反复，直到剩下元素为1个，整个数组排序完。

复杂度：O(N^2)，大约需要N^2/2次比较和N次交换。
"""
from algorithms.ch02sort.base.template import SortTemplate


class SelectSort(SortTemplate):

    def sort(self):
        le = len(self.seq)
        for i in range(le - 1):
            min_index = i
            for j in range(i, le):
                if self.seq[min_index] > self.seq[j]:
                    min_index = j
            if i != min_index:
                self.seq[i], self.seq[min_index] = self.seq[min_index], self.seq[i]


if __name__ == '__main__':
    select_sort = SelectSort([4, 2, 5, 1, 6, 3])
    select_sort.main()
