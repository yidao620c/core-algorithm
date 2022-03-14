# -*- encoding: utf-8 -*-
"""
206. 反转链表
给你单链表的头节点 head ，请你反转链表，并返回反转后的链表。
输入：head = [1,2,3,4,5]
输出：[5,4,3,2,1]

提示：
链表中节点的数目范围是 [0, 5000]
-5000 <= Node.val <= 5000

进阶：链表可以选用迭代或递归方式完成反转。你能否用两种方法解决这道题？
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __str__(self):
        return str(self.val)


class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        if not head:
            return None
        head_next = head.next  # 下一跳
        while head_next:
            head_next_next = head_next.next
            head_next.next = head
            if head.next == head_next:  # 头节点变尾结点
                head.next = None
            head = head_next  # head指针前移
            head_next = head_next_next  # 重新赋值下一跳
        return head


if __name__ == '__main__':
    # 本地运行需要以下输入输出的补充
    list_input = list(input('input list: ').split())

    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(3)
    head.next.next.next = ListNode(4)
    head.next.next.next.next = ListNode(5)

    # solve
    solution = Solution()
    res = solution.reverseList(head)
    print()
    # output


