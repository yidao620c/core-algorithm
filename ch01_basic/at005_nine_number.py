#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
Topic: 从1到9，组成3个三位数，要求每个数字只用一次，
要求结果第二个数是第一个数的两倍，第三个数是第二个数的三倍。求所有的组合
"""


def nine_number():
    nine = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    result = []
    for i in nine:
        each = 0
        each += i * 100
        for j in nine:
            if j == i: continue
            each += j * 10
            for k in nine:
                if k == j or k == i: continue
                each += k
                each2 = 2 * each
                each3 = 3 * each
                if each2 > 999 or each3 > 999: continue
                all_num = []
                all_num.extend(list(str(each)))
                all_num.extend(list(str(each2)))
                all_num.extend(list(str(each3)))
                num_set = set(all_num)
                if len(num_set) == 9:
                    result.append((each, each2, each3))
    return result

if __name__ == '__main__':
    print(nine_number())
