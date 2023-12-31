# -*- encoding: utf-8 -*-
"""
冒泡排序
当某次冒泡操作已经没有数据交换时，说明已经达到完全有序，不用再继续执行后续的冒泡操作。

算法复杂度：N^2
稳定排序：重复元素排序完后仍然保持原来的相对位置。
"""
from algorithms.c04_sort.base.template import SortTemplate


class BubbleSort(SortTemplate):

    def sort(self):
        le = len(self.seq)
        for i in range(le):
            # 提前退出排序的标志，本次循环是否有数据交换
            has_exchange = False
            for j in range(0, le - i - 1):
                if self.seq[j] > self.seq[j + 1]:
                    self.seq[j], self.seq[j + 1] = self.seq[j + 1], self.seq[j]
                    has_exchange = True  # 表示有数据交换
            if not has_exchange:
                break


if __name__ == '__main__':
    bubble_sort = BubbleSort([4, 2, 5, 1, 6, 3])
    bubble_sort.main()
