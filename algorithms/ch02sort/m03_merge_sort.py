#!/usr/bin/env python
"""归并排序(分治法)
    归并排序算法完全遵循分治模式，操作如下：
    分解： 分解待排序的n个元素序列成各具n/2个元素的两个子序列
    解决： 使用归并排序递归的排序两个子序列
    合并： 合并两个已排序的子序列以产生已排序的答案

复杂度：N*lg(N)
稳定排序：重复元素排序完后仍然保持原来的相对位置。
"""
from algorithms.ch02sort.base.template import SortTemplate


class MergeSort(SortTemplate):

    def sort(self):
        self.merge_sort_range(0, len(self.seq) - 1)

    def merge_sort_range(self, start, end):
        """
        归并排序一个序列的子序列
        start: 子序列的start下标
        end: 子序列的end下标
        """
        if start < end:  # 如果start >= end就终止递归调用
            middle = (start + end) // 2
            self.merge_sort_range(start, middle)  # 排好左边的一半
            self.merge_sort_range(middle + 1, end)  # 再排好右边的一半
            self.merge_ordered_seq(start, middle, end)  # 最后合并排序结果

    def merge_ordered_seq(self, left, middle, right):
        """
        seq: 待排序序列
        left <= middle <= right
        子数组seq[left..middle]和seq[middle+1..right]都是排好序的
        该排序的时间复杂度为O(n)
        """
        temp_seq = []
        i = left
        j = middle + 1
        while i <= middle and j <= right:
            if self.seq[i] <= self.seq[j]:
                temp_seq.append(self.seq[i])
                i += 1
            else:
                temp_seq.append(self.seq[j])
                j += 1
        if i <= middle:
            temp_seq.extend(self.seq[i:middle + 1])
        else:
            temp_seq.extend(self.seq[j:right + 1])
        self.seq[left:right + 1] = temp_seq[:]


if __name__ == '__main__':
    merge_sort = MergeSort([4, 2, 5, 1, 6, 3])
    merge_sort.main()
