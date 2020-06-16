#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
Topic: 动态规划：最优矩阵链乘法括号化算法
Desc :
    对于矩阵A[1]A[2]...A[n]相乘，由于满足结合律，求一个最优括号算法使得计算的次数最少
    对于矩阵A[i]*A[j]的计算次数为：p[i-1]*p[i]*p[j] => row(左)*column(左)*column(右)
    算法思路：
    给定一个序列p:<p[0],p[1],p[2]...p[n]>，对每个Ai<p[i-1],p[i]>
    定义一个n*n二维数组m，其中m[i,j]=min(i<= k < j){m[i,k]+m[k+1,j]+p[i-1]*p[k]*p[j]}
    再定义一个n-1*n-1二维数组s，其中s[i,j]表示m[i,j]时候的括号分割点，利用s可以获得最后的括号序列
"""


def matrix_order(p):
    """:param p: 矩阵规模序列，A[i]行列分别为p[i-1],p[i]"""
    INF = float('inf')  # 无穷大
    n = len(p) - 1  # 矩阵长度
    vals = [[0 for _ in range(n)] for _ in range(n)]  # 保存子问题A[i]...A[j]最优值
    ans = [[-1 for _ in range(n)] for _ in range(n)]  # 保存子问题A[i]...A[j]最优值时候的括号分割点
    for chain_len in range(2, n + 1):  # chain_len表示每次循环计算链的长度2..n
        for i in range(0, n - chain_len + 1):
            j = i + chain_len - 1
            vals[i][j] = INF  # 上面两层循环则是对m方阵的右上三角(除对角线)进行某个赋值MAX
            for k in range(i, j):  # 然后对每个计算最小值
                # 此时m[i][k]和m[k + 1][j]一定已经有值了。why???
                # 因为对于某个i，比j小的肯定赋值过
                # 对于某个j，比i大的肯定也赋值过
                # 上面循环方向示意图可以画下，是从右上三角，斜右下右下的循环。
                q = vals[i][k] + vals[k + 1][j] + p[i] * p[k + 1] * p[j + 1]
                if q < vals[i][j]:
                    vals[i][j] = q
                    ans[i][j] = k
    for mm in vals:
        print(mm)
    for ss in ans:
        print(ss)
    print_optimal(ans, 0, n - 1)
    return vals, ans


def print_optimal(s, i, j):
    """根据保存的括号位置表打印出最后的括号最优解"""
    if i == j:
        print('A', end='')
    else:
        print('(', end='')
        print_optimal(s, i, s[i][j])
        print_optimal(s, s[i][j] + 1, j)
        print(')', end='')


if __name__ == '__main__':
    p = [30, 35, 15, 5, 10, 20, 25]
    matrix_order(p)
