# -*- encoding: utf-8 -*-
"""基于二叉堆实现的优先队列
Some of description...
"""
from functools import total_ordering

from algorithms.ch01structure.stack.linked_stack import Stack


class MaxPriorQueue:
    """
    使用一个数组存储二叉堆，所有元素存储在seq[1..max_size]中，se[0]不存储任何东西。
    优先队列支持插入和删除操作。
        1. 插入元素放到最后一个，然后向上游到自己的位置。
        2. 删除元素是移除第一个，然后将最后一个放到第一个，并向下沉到自己的位置。
    """

    def __init__(self, max_size):
        self._seq = [None] * (max_size + 1)  # 初始化长度为max_size+1的数组
        self._size = 0  # 元素长度为0

    def is_empty(self):
        """判断队列是否为空"""
        return self._size == 0

    def size(self):
        return self._size

    def insert(self, item):
        self._size += 1
        self._seq[self._size] = item
        self._swim(self._size)  # 末端插入元素后向上游，游到自己合适的位置去

    def del_max(self):
        item = self._seq[1]  # 根节点拿到最大元素，保留下来后面会作为结果返回
        self._exchange(1, self._size)  # 跟最后一个元素做交换
        self._seq[self._size] = None  # 清空最后一个元素
        self._size -= 1  # 长度-1
        self._sink(1)  # 下沉操作，将第一个元素下沉至合适自己的位置
        return item

    def _less(self, i, j):
        """比较两个元素大小，如果左边小于等于右边，返回True"""
        if self._seq[i] is None or self._seq[j] is None:
            raise IndexError('index error')
        return self._seq[i] < self._seq[j]

    def _exchange(self, i, j):
        """交换两个元素"""
        self._seq[i], self._seq[j] = self._seq[j], self._seq[i]

    def _swim(self, index):
        """向上游上去，游到合适的位置"""
        while index > 1 and self._less(index // 2, index):
            self._exchange(index // 2, index)
            index = index // 2

    def _sink(self, index):
        """向下沉下去，把老大的位置叫出来，谁更牛逼谁做老大"""
        while 2 * index <= self._size:
            j = 2 * index
            if j < self._size and self._less(j, j + 1):
                j += 1  # 如果有两个下属，把最牛逼的下属拿出来做对比
            if not self._less(index, j):
                break  # 如果比最牛逼的那个下属还要厉害，说明这个老大位置没问题了
            self._exchange(index, j)  # 如果没有下属厉害，就自己乖乖把位置让出来，跟他交换一下
            index = j  # 现在index的值修改成新的位置，继续向下做对比，直到找到自己合适的位置


@total_ordering
class Item:
    def __init__(self, key, val, index=-1):
        self.key = key
        self.val = val
        self.index = index

    def __eq__(self, other):
        return self.key == other.key

    def __lt__(self, other):
        return self.key < other.key

    def __str__(self):
        return str((self.val, self.key, self.index))


if __name__ == '__main__':
    prior_queue = MaxPriorQueue(20)
    items = [
        Item(2, "22222"),
        Item(5, "55555"),
        Item(5, "5===="),
        Item(3, "33333"),
        Item(9, "99999"),
    ]
    for item in items:
        prior_queue.insert(item)

    stack = Stack()
    while not prior_queue.is_empty():
        stack.push(prior_queue.del_max())
    for item in stack:
        print(item)
