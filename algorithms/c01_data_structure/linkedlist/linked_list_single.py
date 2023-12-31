# -*- encoding: utf-8 -*-
"""
单向链表数据结构
"""
from algorithms.c01_data_structure import Node


class LinkedListSingle:
    """
    单向链表，带哨兵
    """

    def __init__(self, limit):
        self.head = Node(None)
        self.size = 1
        self.limit = limit + 1  # 预留一个给哨兵头节点

    def insert(self, node, new_node):
        """
        :param node: 插入点节点
        :param new_node: 新节点
        :return:
        """
        if self.size >= self.limit:
            raise IndexError('list is full')
        new_node.next = node.next
        node.next = new_node
        self.size += 1

    def is_full(self):
        return self.size >= self.limit

    def is_empty(self):
        return self.size == 1

    def remove(self, node):
        """
        :param node: 待删除节点
        :return:
        """
        if self.is_empty():
            return
        pre_node = self.head
        while pre_node.next != node:
            pre_node = pre_node.next
        pre_node.next = node.next
        self.size -= 1

    def get_tail(self):
        target = self.head
        while target.next:
            target = target.next
        return target

    def search(self, data):
        """
        直接比较原始数据
        :param data: 待查询数据
        :return: 查询到的节点
        """
        target = self.head.next
        while target and target.data != data:
            target = target.next
        return target

    def search_equal(self, data, equal):
        """
        通过传入equal比较函数来进行相等判断
        :param data: 待查询数据
        :param equal: 相等函数
        :return: 查询到的节点
        """
        target = self.head.next
        while target and equal(target.data, data):
            target = target.next
        return target

    def __iter__(self):
        node = self.head.next
        while node:
            yield node.data
            node = node.next

    def print(self):
        print(list(x for x in self))
