# -*- encoding: utf-8 -*-
"""将重复的方法抽取出来
Some of description...
"""


def insert_sort(seq_):
    """插入排序"""
    for j in range(1, len(seq_)):
        key = seq_[j]
        # insert arrays[j] into the sorted seq[0...j-1]
        i = j - 1
        while i >= 0 and key < seq_[i]:
            seq_[i + 1] = seq_[i]  # element move forward
            i -= 1
        seq_[i + 1] = key  # at last, put key to right place
