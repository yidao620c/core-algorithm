#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
    Topic: 动态规划，切割钢管，使得收益最大化
    Desc :
    给定一段长度为n的钢条和一个价格表p[i](i=1,2,3,4...n)，
    求切割方案，使得销售收益r[n]最大。
    注意，如果长度为n的钢条价格p[n]足够大，最优解可能是完全不需要切割。
"""
__author__ = 'Xiong Neng'


def bottom_up_cut_rod(p, n):
    """自顶向上版本的动态规划
    自底向上版本采用子问题的自然顺序，若i<j，则规模为i的子问题比规模为j的子问题更小。
    因此，过程依次求解规模为j=0,1...n的子问题

    param p: 价格数组，长度为i的钢条价格为p[i]
    param n: 钢条总长度
    """
    # 先初始化数组r
    r = [0] * (n + 1)
    # 用来保存每个最优解二维数组，ans[i]表示长度为i的最优解
    ans = [[]]
    for j in range(1, n + 1):
        q = -999
        # 下面这个内层循环保证长度为j时候所有情况都考虑到了
        # 因为i会从1迭代到j，也就是切割方案中左边方案为1,2...j的时候，跟右边已经有最优解的加起来，
        # 然后算所有的加起来的和的最大值，那肯定就是最优解了！ NB啊
        for i in range(1, j + 1):
            if q < p[i] + r[j - i]:
                q = p[i] + r[j - i]
                ii = i
        r[j] = q
        ans.append([ii] + ans[j-ii])
    return r[n], ans[len(ans) - 1]


if __name__ == '__main__':
    parry = [0, 1, 5, 8, 9, 10, 17, 17, 20, 24, 30]
    for k in range(1, 11):
        print(bottom_up_cut_rod(parry, k))

