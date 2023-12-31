# -*- encoding: utf-8 -*-
"""
单向循环链表数据结构
"""
from algorithms.c01_data_structure import Node


class LinkedListSingleCycle:
    """
    单向循环链表，带哨兵
    """

    def __init__(self):
        self.head = Node(None)
        self.head.next = self.head

    def insert_node(self, node, new_node):
        """
        :param node:插入点节点
        :param new_node:新节点
        :return:
        """
        new_node.next = node.next
        node.next = new_node

    def remove_node(self, node):
        """
        :param node:待删除节点
        :return:
        """
        pre_node = self.head
        while pre_node.next != node:
            pre_node = pre_node.next
        pre_node.next = node.next

    def search(self, data):
        """
        直接比较原始数据
        :param data: 待查询数据
        :return: 查询到的节点
        """
        target = self.head.next
        while target != self.head and target.data != data:
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
        while target != self.head and equal(target.data, data):
            target = target.next
        return target
