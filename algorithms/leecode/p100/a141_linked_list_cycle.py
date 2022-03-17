# -*- encoding: utf-8 -*-
"""
141. 环形链表
给你一个链表的头节点 head ，判断链表中是否有环。

如果链表中有某个节点，可以通过连续跟踪 next指针再次到达，则链表中存在环。
不能直接通过判定next是否为null来决定是否有环，因为如有环则是一个无限循环。

通过快慢指针法，慢指针走一步，快指针走两步。
如果快指针率先走到尽头结束，无环。
否则快指针率先进环，慢指针则在后面进环。快指针一定会追上满指针，一旦追上了，循环结束。
"""
# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if not head or not head.next or not head.next.next:
            return False
        slow = head.next
        fast = head.next.next
        while slow != fast:
            if not fast.next or not fast.next.next:
                return False
            slow = slow.next
            fast = fast.next.next
        return True


if __name__ == '__main__':
    a = ListNode(1)
    b = ListNode(2)
    c = ListNode(3)
    d = ListNode(4)
    f = ListNode(5)
    a.next = b
    b.next = c
    c.next = d
    d.next = f
    f.next = b
    print(Solution().hasCycle(a))
