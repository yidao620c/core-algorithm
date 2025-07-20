# -*- encoding: utf-8 -*-
"""
给你一个链表的头节点 head 和一个特定值 x ，请你对链表进行分隔，使得所有 小于 x 的节点都出现在 大于或等于 x 的节点之前。

你应当 保留 两个分区中每个节点的初始相对位置。

输入：head = [1,4,3,2,5,2], x = 3
输出：[1,2,2,4,3,5]

输入：head = [2,1], x = 2
输出：[1,2]
"""
from typing import Optional

from algorithms.c01_data_structure.linkedlist import ListNode


class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        p1 = None  # 小于x的链表
        p1_head = None
        p2 = None  # 大于等于x的链表
        p2_head = None
        p = head  # 循环原链表
        while p:
            if p.val < x:
                if not p1:
                    p1 = p
                    p1_head = p
                else:
                    p1.next = p
                    p1 = p1.next
            else:
                if not p2:
                    p2 = p
                    p2_head = p
                else:
                    p2.next = p
                    p2 = p2.next
            temp = p.next
            p.next = None
            p = temp
        if p1:
            p1.next = p2_head
        return p1_head if p1_head else p2_head


if __name__ == '__main__':
    # [1,4,3,2,5,2]
    head = ListNode(2)
    head = ListNode(5, head)
    head = ListNode(2, head)
    head = ListNode(3, head)
    head = ListNode(4, head)
    head = ListNode(1, head)
    head = Solution().partition(head, 3)
    while head:
        print(head.val, end=' ')
        head = head.next
