#!/usr/bin/env python
"""插入排序
我们将数组中的数据分为两个区间，已排序区间和未排序区间。初始已排序区间只有一个元素，就是数组的第一个元素。
插入算法的核心思想是取未排序区间中的元素，在已排序区间中找到合适的插入位置将其插入，并保证已排序区间数据一直有序。
重复这个过程，直到未排序区间中元素为空，算法结束。

由于其内层循环非常紧凑，对于小规模的输入，插入排序是一种非常快的原址排序算法。
注：如果输入数组中仅有常数个元素需要在排序过程中存储在数组外，则称这种排序算法是原址的。

冒泡排序的数据交换要比插入排序的数据移动要复杂，冒泡排序需要3个赋值操作，而插入排序只需要1个。
所以，虽然冒泡排序和插入排序在时间复杂度上是一样的，都是 O(n2)，但是如果我们希望把性能优化做到极致，
那肯定首选插入排序。

算法复杂度：N^2
稳定排序：重复元素排序完后仍然保持原来的相对位置。
"""
from algorithms.c04_sort.base.sortutil import insert_sort
from algorithms.c04_sort.base.template import SortTemplate


class InsertSort(SortTemplate):

    def sort(self):
        insert_sort(self.seq)


if __name__ == '__main__':
    select_sort = InsertSort([4, 2, 5, 1, 6, 3])
    select_sort.main()
