#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# 最长公共子序列
# author: XiongNeng
"""
一个子序列代表，将一个序列中去掉若干元素后得到的序列，可以间隔。
公共子序列就是，序列A和序列B的公共子序列
最长公共子序列就是，公共子序列里面长度最长的。

思路：
接受两个序列<x1,x2,...xm>和<y1,y2,...yn>作为输入
将两个序列按照下标变成矩阵或者是二维数组c(m+1 * n+1)
按行主次序(row-major-order)计算表项，即首先计算C的第一行，然后是第二行。。
另外还维护一个二维数组b(m * n)，b[i,j]指向的表项对应计算c[i,j]时选择的子问题最优解
c[m-1][n-1]保存了X和Y的LCS的长度
"""


def lcs(arr1, arr2):
    m = len(arr1)
    n = len(arr2)
    c = [[0 for kk in range(n + 1)] for kk in range(m + 1)]
    b = [[-1 for kk in range(n)] for kk in range(m)]
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if arr1[i - 1] == arr2[j - 1]:
                c[i][j] = c[i - 1][j - 1] + 1
                b[i - 1][j - 1] = '↖'  # 代表此元素放入LCS
            elif c[i - 1][j] >= c[i][j - 1]:
                c[i][j] = c[i - 1][j]
                b[i - 1][j - 1] = '↑'  # 行减1，往上
            else:
                c[i][j] = c[i][j - 1]
                b[i - 1][j - 1] = '←'  # 列减1，往左
    rlcs = []
    get_lcs_arr(b, arr1, len(arr1) - 1, len(arr2) - 1, rlcs)
    print('LCS长度为:%d' % c[m][n])
    print('一个最优解:%s' % str(rlcs))
    return c[m][n], rlcs


def get_lcs_arr(b, X, i, j, arr):
    if i < 0 or j < 0:
        return
    if b[i][j] == '↖':
        get_lcs_arr(b, X, i - 1, j - 1, arr)
        arr.append(X[i])
    elif b[i][j] == '↑':
        get_lcs_arr(b, X, i - 1, j, arr)
    else:
        get_lcs_arr(b, X, i, j - 1, arr)


if __name__ == '__main__':
    x = ['A', 'B', 'D', 'A', 'C', 'K']
    y = ['B', 'D', 'D', 'E', 'C', 'K', 'M']
    lcs(x, y)
