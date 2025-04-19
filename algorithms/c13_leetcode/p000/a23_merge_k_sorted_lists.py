# -*- encoding: utf-8 -*-
"""
23. 合并 K 个升序链表

给你一个链表数组，每个链表都已经按升序排列。
请你将所有链表合并到一个升序链表中，返回合并后的链表。

输入：lists = [[1,4,5],[1,3,4],[2,6]]
输出：[1,1,2,3,4,4,5,6]
"""
from typing import List, Optional

from algorithms.c01_data_structure.linkedlist import ListNode
from queue import PriorityQueue


class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists:
            return None
        p = None
        p_head = None
        pq = PriorityQueue()
        for list_idx, each in enumerate(lists):
            if each:
                pq.put((each.val, list_idx, each))
        while not pq.empty():
            node = pq.get()
            if p:
                p.next = node[2]
                p = p.next
            else:
                p = node[2]
                p_head = node[2]
            if node[2].next:
                pq.put((node[2].next.val, node[1], node[2].next))
        return p_head


if __name__ == '__main__':
    """
    输入：lists = [[1,4,5],[1,3,4],[2,6]]
    输出：[1,1,2,3,4,4,5,6]
    """
    node1 = ListNode(5)
    node1 = ListNode(4, node1)
    node1 = ListNode(1, node1)
    node2 = ListNode(4)
    node2 = ListNode(3, node2)
    node2 = ListNode(1, node2)
    node3 = ListNode(6)
    node3 = ListNode(2, node3)
    lists = [node1, node2, node3]
    head = Solution().mergeKLists(lists)
    while head:
        print(head.val, end=' ')
        head = head.next
    ...
