#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# 最长公共子序列：longest-common-subsequence
"""
Topic: 一个子序列代表，将一个序列中去掉若干元素后得到的序列，可以间隔。
    公共子序列就是，序列A和序列B的公共子序列
    最长公共子序列就是，公共子序列里面长度最长的。
Desc : 
"""

def lcs(arr1, arr2):
    m = len(arr1)
    n = len(arr2)
    b = [[-1 for kk in range(0, n)] for kk in range(0, m)]
    c = [[0 for kk in range(0, n)] for kk in range(0, m)]

    return None

if __name__ == '__main__':
    x = ['A', 'B', 'D', 'A', 'C', 'K']
    y = ['B', 'D', 'D', 'E', 'C', 'K', 'M']
    lcs(x, y)