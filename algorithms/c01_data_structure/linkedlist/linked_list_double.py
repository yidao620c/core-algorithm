# -*- encoding: utf-8 -*-
"""
双向链表数据结构
"""
from algorithms.c01_data_structure import NodeDouble


class LinkedListDouble:
    """
    双向链表，带哨兵
    """

    def __init__(self):
        self.head = NodeDouble(None)

    def insert_node(self, node, new_node):
        """
        :param node:插入点节点
        :param new_node:新节点
        :return:
        """
        new_node.next = node.next
        new_node.pre = node
        node.next = new_node

    def remove_node(self, node):
        """
        :param node:待删除节点
        :return:
        """
        if not node.pre:  # 空表
            return
        node.pre.next = node.next
        if node.next:  # 如果node有下一个节点
            node.next.pre = node.pre

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
