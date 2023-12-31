# -*- encoding: utf-8 -*-
"""
Question：怎样用单链表实现LRU缓存淘汰算法？

我们维护一个单链表，越靠近链表尾部的结点是越早之前访问的。当有一个新的数据被访问时，
我们从链表头开始顺序遍历链表。

1. 如果此数据之前已经被缓存在链表中了，我们遍历得到这个数据对应的结点，并将其从原来的位置删除，
然后再插入到链表的头部。
2. 如果此数据没有在缓存链表中，又可以分为两种情况：
  2.1 如果此时缓存未满，则将此结点直接插入到链表的头部；
  2.2 如果此时缓存已满，则链表尾结点删除，将新的数据结点插入链表的头部。
"""
from algorithms.c01_data_structure import Node
from algorithms.c01_data_structure.linkedlist.linked_list_single import LinkedListSingle


def lru(list_single_, data):
    find_node = list_single_.search(data)
    if find_node:
        list_single_.remove(find_node)
        list_single_.insert(list_single_.head, find_node)
    else:
        if not list_single_.is_full():
            list_single_.insert(list_single_.head, new_node=Node(data))
        else:
            tail = list_single_.get_tail()
            new_node = Node(data)
            list_single_.remove(tail)
            list_single_.insert(list_single_.head, new_node)
    list_single_.print()


if __name__ == '__main__':
    list_single = LinkedListSingle(3)
    lru(list_single, 2)
    lru(list_single, 3)
    lru(list_single, 2)
    lru(list_single, 1)
    lru(list_single, 5)
    lru(list_single, 6)
