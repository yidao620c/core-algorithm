# -*- encoding: utf-8 -*-
"""
21. 合并两个有序链表

将两个升序链表合并为一个新的 升序 链表并返回。新链表是通过拼接给定的两个链表的所有节点组成的。

可使用类似贪吃蛇的算法。当前指针就像一条贪吃蛇一样，将两个队列节点一个个吃掉。
任何时刻，都有一个队列是蛇，一个队列是食物。但是贪吃蛇一次只能吃一边的一个节点，
当它吃掉一个节点时，该节点所在的队列成为蛇的身体，另外一个队列成为食物。最后食物吃完循环结束。
"""

# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __str__(self):
        return self.val


class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list1:
            return list2
        if not list2:
            return list1
        result = list1 if list1.val <= list2.val else list2
        snake = result  # 贪吃蛇指针
        food = list2 if list1.val <= list2.val else list1  # 要吞并的食物，跟蛇身取反
        while food:  # 只要食物还在就一直吃下去
            if not snake.next:  # 贪吃蛇自己到头了，就一口吃掉剩余所有食物，循环结束。
                snake.next = food
                break
            if snake.next.val <= food.val:
                snake = snake.next  # 自己的身体的下一部分比较小，就先吃自己。
            else:
                temp_food = snake.next
                snake.next = food  # 食物比较小，先吃食物，让食物变成蛇的一部分
                food = temp_food  # 将原来剩余的蛇身变成食物。这样完成了蛇身和食物的交换。
        return result


if __name__ == '__main__':
    a = ListNode(1)
    b = ListNode(2)
    c = ListNode(4)
    a.next = b
    b.next = c

    aa = ListNode(1)
    bb = ListNode(3)
    cc = ListNode(4)
    aa.next = bb
    bb.next = cc

    r = Solution().mergeTwoLists(a, aa)
    print(r)
