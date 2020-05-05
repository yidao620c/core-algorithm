# -*- encoding: utf-8 -*-
"""使用二叉堆实现堆排序最优雅代码
原理：如果左右子树都已经是最大堆了，则通过下沉当前根节点操作即可重新构造为一个最大堆。
"""
from algorithms.ch02sort.base.template import SortTemplate


class HeapSort(SortTemplate):

    def __init__(self, seq):
        super().__init__(seq)
        self._size = len(seq)

    def sort(self):
        """最简的堆排序算法"""
        # 第一步：首先通过下沉操作构造最大二叉堆
        k = self._size // 2  # 从中间开始往前循环
        while k >= 1:
            self._sink(k, self._size)
            k -= 1

        # 第二步：通过每次将堆顶元素跟后面元素交换，堆大小减少1。
        # 然后再下沉堆顶元素重新构造堆，直到堆大小为1
        k = self._size
        while k > 1:
            self._exchange(1, k)
            k -= 1
            self._sink(1, k)

    def _sink(self, index, n):
        """向下沉下去，把老大的位置叫出来，谁更牛逼谁做老大"""
        while 2 * index <= n:
            j = 2 * index
            if j < n and self._less(j, j + 1):
                j += 1  # 如果有两个下属，把最牛逼的下属拿出来做对比
            if not self._less(index, j):
                break  # 如果比最牛逼的那个下属还要厉害，说明这个老大位置没问题了
            self._exchange(index, j)  # 如果没有下属厉害，就自己乖乖把位置让出来，跟他交换一下
            index = j  # 现在index的值修改成新的位置，继续向下做对比，直到找到自己合适的位置

    def _less(self, i, j):
        """
        比较两个元素大小，如果左边小于等于右边，返回True
        注意，这里索引都减1，用来支持索引值从1开始的序列
        """
        if self.seq[i - 1] is None or self.seq[j - 1] is None:
            raise IndexError('index error')
        return self.seq[i - 1] < self.seq[j - 1]

    def _exchange(self, i, j):
        """交换两个元素，这里索引也都减1"""
        self.seq[i - 1], self.seq[j - 1] = self.seq[j - 1], self.seq[i - 1]


if __name__ == '__main__':
    heap_sort = HeapSort([9, 7, 8, 10, 16, 3, 14, 2, 1, 4])
    heap_sort.main()
