#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
Topic: 排序模板
"""


class SortTemplate:

    def __init__(self, seq):
        self.seq = seq

    def sort(self):
        """
        排序方法
        """
        pass

    def less(self, val1, val2):
        """
        对比两个元素，如果从小到大则返回True
        """
        return val1 <= val2

    def show(self, vals):
        for val in vals:
            print("{}".format(val), end=' ')

    def is_sorted(self, vals):
        for i in range(1, len(vals)):
            if self.less(vals[i], vals[i - 1]):
                return False
        return True

    def main(self):
        self.sort()
        assert self.is_sorted(self.seq)
        self.show(self.seq)
