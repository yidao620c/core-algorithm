#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
Topic: 从1到9，组成3个三位数，要求每个数字只用一次，
要求结果第二个数是第一个数的两倍，第三个数是第一个数的三倍。求所有的组合

算法思想：
使用三层循环先计算第一个数each1，要求三个位不一样
然后先计算符合倍数关系的第二个数each2=2*each1，第三个数each3=3*each1，
然后判断each1、each2和each3这三个数是否每个位都各不相同，
这个将它们拆成单个字符然后放入集合中，如果集合个数=9就符合条件
"""


def nine_number():
    nine = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    result = []
    for i in nine:
        each1 = 0
        each1 += i * 100
        for j in nine:
            if j == i: continue
            each1 += j * 10
            for k in nine:
                if k == j or k == i: continue
                each1 += k
                each2 = 2 * each1
                each3 = 3 * each1
                if each2 > 999 or each3 > 999: continue
                all_num = []
                all_num.extend(list(str(each1)))
                all_num.extend(list(str(each2)))
                all_num.extend(list(str(each3)))
                num_set = set(all_num)
                if len(num_set) == 9:
                    result.append((each1, each2, each3))
    return result


if __name__ == '__main__':
    print(nine_number())
