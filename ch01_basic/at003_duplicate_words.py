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
    print(find_count(r'D:\work\projects\gitprojects\core-algorithm\files\names.txt'))

