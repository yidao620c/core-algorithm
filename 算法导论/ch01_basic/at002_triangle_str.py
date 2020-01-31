#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# 三角打印字符串
"""
    Topic: sample
    Desc : 三角打印字符串
"""
__author__ = 'Xiong Neng'


# 三角打印
def triangleDisplay(mystr):
    # mystr = unicode(mystr, 'utf-8')
    mystr += ' '
    result = []
    le = len(mystr)
    for i in range(1, le):
        result.append(mystr[-i: -1])
    for i in range(le):
        result.append(mystr[i: -1])
    return result


for each in triangleDisplay(u"我和我的小伙伴们都惊呆了"):
    print(each)
