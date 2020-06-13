#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# 动态规划：电梯调度算法
"""
    Topic: sample
    Desc : 电梯调度算法
        电梯停在哪一层楼，能够保证这次乘坐电梯的所有乘客爬楼梯的层数之和最少
        这个属于动态规划问题
        动态规划。假设电梯停在第x层，已知目的楼层
        在x层以下的有N1人,
        在x层的有N2人，
        在x层以上的有N3人。
        此时总花费为sum。
        则往上走一层的话，总花费变为sum + N2 + N1 - N3。
        那么初始状态电梯停在第一层，向上进行状态的变迁，开始时N2 + N1 - N3 < 0。
        sum越来越小，直到某一层N2 + N1 >= N3，就没有必要在往上走了。
        这时已求出最合适的楼层了
"""
__author__ = 'Xiong Neng'


def elevatorSchedule(seq):
    """
    seq: 去往每层的人数， 下标代表楼层号， 很明显0和1层都是0
    """
    N1 = N2 = 0  # 到当前层以下的有N1人， 到当前层的有N1人
    N3 = 0  # 到当前层以上的有N3人
    nMinFloors = 0  # 所有乘客要爬的楼层最小总和
    nTargetFloor = 1  # 达到最小值时候的楼层
    for i in range(2, len(seq)):
        N3 += seq[i]
        nMinFloors += seq[i] * (i - 1)
    for i in range(2, len(seq)):
        if N1 + N2 < N3:
            nTargetFloor = i
            nMinFloors += (N1 + N2 - N3)
            N1 += N2
            N2 = seq[i]
            N3 -= seq[i]
        else:
            break
    return nTargetFloor, nMinFloors


if __name__ == '__main__':
    s = [0, 0, 2, 4, 5, 7, 2, 1]
    print(elevatorSchedule(s))
