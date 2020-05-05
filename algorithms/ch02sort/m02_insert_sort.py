#!/usr/bin/env python
"""插入排序
索引从1开始往右边遍历，将元素插入到左边已排序好的数组中，索引左边的所有元素都是有序的，
但是它们的最终位置并不确定，为了给更小元素腾出空间，它们可能会被移动。当索引到达最右端的时候，数组排序完成。

由于其内层循环非常紧凑，对于小规模的输入，插入排序是一种非常快的原址排序算法。
注： 如果输入数组中仅有常数个元素需要在排序过程中存储在数组外，则称这种排序算法是原址的。

算法复杂度：N^2
稳定排序：重复元素排序完后仍然保持原来的相对位置。
"""
from algorithms.ch02sort.base.sortutil import insert_sort
from algorithms.ch02sort.base.template import SortTemplate


class InsertSort(SortTemplate):

    def sort(self):
        insert_sort(self.seq)


if __name__ == '__main__':
    select_sort = InsertSort([4, 2, 5, 1, 6, 3])
    select_sort.main()
