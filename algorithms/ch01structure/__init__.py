# -*- encoding: utf-8 -*-
"""常见的数据结构
"""


class Node:
    """
    节点信息
    """
    def __init__(self, item_, next_=None):
        self.item = item_
        self.next = next_

    def __str__(self):
        return str(self.item)
