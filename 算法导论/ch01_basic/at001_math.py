#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# 最大公约数，公倍数，素因子分解，闰年判断，找零钱，斐波那契数列
"""
    基本的初等数学类
    最大公约数，公倍数，素因子分解，闰年判断，找零钱，斐波那契数列
"""
__author__ = 'Xiong Neng'


# 闰年判断
def isLeapYear(year):
    return (not year % 4 and year % 100) or (not year % 400)


# 找零钱
def mod(money):
    cent = int(money * 100)
    all_cent = {25: 0, 10: 0, 5: 0, 1: 0}
    for k in all_cent:
        all_cent[k], cent = divmod(cent, k)
    return all_cent


# 最大公约数，辗转相除法
def maxCommonDivisor(m, n):
    while True:
        remainder = m % n
        if not remainder:
            return n
        else:
            m, n = n, remainder


# 最小公倍数
def minCommonMultiple(m, n):
    return m * n / maxCommonDivisor(m, n)


# 素数的判断
def isprime(n):
    result = True
    for i in range(n / 2, 1, -1):
        if n % i == 0:
            result = False
            break
    return result


# 获取n的所有因子
def getfactors(n):
    result = [n]
    for i in range(n / 2, 0, -1):
        if n % i == 0:
            result.append(i)
    return result


# 素因子分解
def decompose(n):
    all_factors = getfactors(n)
    all_factors.remove(1)
    all_factors.remove(n)
    prime_factors = [x for x in all_factors if isprime(x)]
    prime_factors.sort(reverse=True)
    result = []
    remainder = n
    for f in prime_factors:
        while remainder >= f:
            qut, rem = divmod(remainder, f)
            if rem != 0:
                break
            else:
                remainder = qut
                result.append(f)
    return result


# 获取前N个斐波那契数列
def fibonacci(n):
    result = []
    if n == 1:
        result.append(1)
    elif n >= 2:
        result.append(1)
        result.append(1)
        for i in range(2, n):
            result.append(result[-1] + result[-2])
    return result


def main():
    print(fibonacci(8))
    mod(0.78)
    print(maxCommonDivisor(24, 36))
    print(minCommonMultiple(24, 36))


if __name__ == '__main__':
    main()
