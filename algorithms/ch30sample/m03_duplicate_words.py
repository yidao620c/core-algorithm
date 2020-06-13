#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
Topic: 找重名的单词
Desc : 
"""


def find_count(filename):
    count_map = {}
    with open(filename, encoding='utf-8') as f:
        for line in f:
            if line in count_map:
                count_map[line] += 1
            else:
                count_map[line] = 1
    return {k: v for k, v in count_map.items() if v > 1}


if __name__ == '__main__':
    # filename = sys.argv[1]
    # print(find_count(filename))

    arr = [3, 5, 200, 304, 22, 34, 5, 12, 99, 567]
    max_num = 1000000  # 比这些数字里面最大的数大即可
    init_arr = [0 for i in range(max_num)]  # 初始化数组
    for n in arr:
        init_arr[n] += 1
        if init_arr[n] > 1:
            print('找到重复的了，{}'.format(n))
            break
