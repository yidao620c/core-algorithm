# -*- encoding: utf-8 -*-
"""
链表数据结构

练习题LeetCode对应编号：206，141，21，19，876

* 单链表反转
* 链表中环的检测
* 两个有序的链表合并
* 删除链表倒数第 n 个结点
* 求链表的中间结点
"""


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
