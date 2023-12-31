# -*- encoding: utf-8 -*-
"""
70. 爬楼梯
假设你正在爬楼梯。需要 n阶你才能到达楼顶。
每次你可以爬 1 或 2 个台阶。你有多少种不同的方法可以爬到楼顶呢？
注意：给定 n 是一个正整数。
"""


class Solution:
    def climb_stairs(self, n: int) -> int:
        if n == 1:
            return 1
        if n == 2:
            return 2
        a, b = 1, 2
        for i in range(3, n + 1):
            a, b = b, a + b

        return b


if __name__ == '__main__':
    import sys

    while True:
        line = sys.stdin.readline().strip()
        if line == '':
            break
        print(Solution().climb_stairs(int(line)))
