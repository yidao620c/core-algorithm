# -*- encoding: utf-8 -*-
"""
线性表数据结构：数组、链表、队列、栈。
"""


class Node:
    """
    单指针节点
    """

    def __init__(self, data_, next_=None):
        self.data = data_
        self.next = next_

    def __str__(self):
        return str(self.data)


class NodeDouble:
    """
    双指针节点
    """

    def __init__(self, data_, next_=None, pre_=None):
        self.data = data_
        self.next = next_
        self.pre = pre_

    def __str__(self):
        return str(self.data)
