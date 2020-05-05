#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
Josephus排列
Topic: n个人围成一圈，从某个指定人开始，沿着环将遇到的每第m个人移出去。
        每个人移出去后，继续沿着环将剩下的人按同样规则移出去
        默认队列第一个编号为1，以此类推。。。
"""


def circle_out(n, m):
    # 初始化数组，1表示在队列中，0表示已经出了队列
    queue_status = [1 for n in range(0, n)]
    result = []  # 出队序列
    out_count = 0  # 出队人数
    pass_num = 0  # 每次小循环经过的人数
    index = 0  # 循环下标
    while out_count < n:
        while True:
            if queue_status[index] == 1:
                pass_num += 1
            if pass_num >= m:
                break
            index = (index + 1) % n
        # 出队
        queue_status[index] = 0
        out_count += 1
        result.append(index + 1)
        pass_num = 0
    print(result)
    return result


if __name__ == '__main__':
    circle_out(7, 3)
