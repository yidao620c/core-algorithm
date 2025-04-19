# -*- encoding: utf-8 -*-
"""
19. 删除单链表的倒数第N个结点

给你一个单链表，删除链表的倒数第 n 个结点，并且返回链表的头结点。

两轮循环：
1、第一轮循环获取链表的节点总数size。
2、第二轮循环删除第size-n位置上的节点。
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __str__(self):
        return str(self.val)


class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        if not head:
            return head
        size = 0
        temp = head
        while temp:
            size += 1
            temp = temp.next
        if n > size:
            return head

        pre = None
        remove_item = head
        for _ in range(size - n):
            pre = remove_item
            remove_item = remove_item.next
        if pre:
            pre.next = remove_item.next
        else:
            head = remove_item.next
        return head


if __name__ == '__main__':
    # 本地运行需要以下输入输出的补充
    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(3)
    head.next.next.next = ListNode(4)
    head.next.next.next.next = ListNode(5)

    # solve
    solution = Solution()
    res = solution.removeNthFromEnd(head, 5)
    print()
    # output
