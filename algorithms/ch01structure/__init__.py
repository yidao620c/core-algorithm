# -*- encoding: utf-8 -*-
"""常见的数据结构
"""


class Node:
    """
    节点信息
    """
    def __init__(self, val_, next_=None):
        self.val = val_
        self.next = next_

    def __str__(self):
        return str(self.val)
