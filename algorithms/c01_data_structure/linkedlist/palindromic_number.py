# -*- encoding: utf-8 -*-
"""
Question：如果字符串是通过单链表来存储的，那该如何来判断是一个回文串？

快慢指针法实现过程：
由于回文串最重要的就是对称，那么最重要的问题就是找到那个中心，用快指针每步两格走，当他到达链表末端的时候，
慢指针刚好到达中心，慢指针在过来的这趟路上还做了一件事，他把走过的节点反向了，在中心点再开辟一个新的指针用于往回走，
而慢指针继续向前，当慢指针扫完整个链表，就可以判断这是回文串，否则就提前退出。

总的来说时间复杂度按慢指针遍历一遍来算是O(n),空间复杂度因为只开辟了3个额外的辅助，所以是o(1)

1.1 奇数情况，中点位置不需要矫正
1.2 偶数情况，使用偶数定位中点策略，要确定是返回上中位数或下中位数
  1.2.1 如果是返回上中位数，后半部分串头取next <<=这里使用这张上中位数数
  1.2.2 如果是返回下中位数，后半部分串头既是当前节点位置，但前半部分串尾要删除掉当前节点
"""
from algorithms.c01_data_structure import Node
from algorithms.c01_data_structure.linkedlist.linked_list_single import LinkedListSingle


def palindromic(list_single_):
    if list_single_.is_empty() or list_single_.size == 2:
        return True
    if list_single_.size == 3:
        return list_single_.head.next.data == list_single_.head.next.next.data

    slow = list_single_.head.next.next  # slow指向第2个节点
    slow_next = slow.next  # 保存下一步的slow后驱节点
    fast = slow.next  # fast指向第3个节点
    slow.next = list_single_.head.next  # 第一个slow指针反向
    list_single_.head.next.next = None  # 第一个节点下一个指针初始化为None

    while fast.next and fast.next.next:  # 还能继续往前跑
        fast = fast.next.next  # 快指针先往后面走2步
        slow_pre = slow  # 临时保存slow
        slow = slow_next  # slow往后走1步
        slow_next = slow.next  # 保存slow下一步的后驱节点
        slow.next = slow_pre  # 将slow节点的next反转
    if not fast.next:  # 奇数情况
        # 左边指针从slow.next开始，右边指针从slow_next开始
        slow = slow.next
        if not slow:
            return True
        while slow:
            if slow.data != slow_next.data:
                return False
            slow = slow.next
            slow_next = slow_next.next
    else:  # 偶数情况
        # 左边指针从slow开始，右边指针从slow_next开始
        while slow:
            if slow.data != slow_next.data:
                return False
            slow = slow.next
            slow_next = slow_next.next
    return True


if __name__ == '__main__':
    list_single = LinkedListSingle(30)
    list_single.insert(list_single.head, Node('d'))
    list_single.insert(list_single.head, Node('a'))
    list_single.insert(list_single.head, Node('b'))
    list_single.insert(list_single.head, Node('c'))
    list_single.insert(list_single.head, Node('b'))
    list_single.insert(list_single.head, Node('a'))
    list_single.insert(list_single.head, Node('d'))
    list_single.print()
    print(palindromic(list_single))
