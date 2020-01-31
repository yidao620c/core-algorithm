#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# 歌曲投票
"""
    Topic: 找出7号歌曲包揽5项大奖的投票组合
    Desc :
    云宏歌词比赛投票，总共166人参与投票
    每人从1-13编号的歌曲中选5首不同的歌，依次放入1-5号大奖箱中，
    最后分别将每个奖箱中得票数最多的那个号码提取出来。
    请找出一个组合使得7号歌曲包揽5项大奖的投票组合
"""

__author__ = 'Xiong Neng'


def lucky_seven(rows=166, cols=5, choices=13, lucky=7, start=1):
    """
    找出一个7号包揽5项大奖的投票组合
    rows: 行数，也就是投票人数
    cols：列数，也就是每人允许投几票
    choices：被投票的歌曲的数量，从1-choices编号
    lucky：幸运数字，终止这首歌包揽5项大奖
    start：列填充循环时候的起始数
    """
    # 先初始化一个二维输入数组
    votes = [[None] * cols for x in range(rows)]
    # 第一步用7斜线填充
    for i in range(rows):
        votes[i][i % cols] = lucky
        # 第二步，填充每一列
    for col in range(cols):
        nextnum = start
        for row in range(rows):
            if votes[row][col] is None:
                while nextnum in votes[row]:
                    nextnum += 1
                    if nextnum > choices:
                        nextnum -= choices
                if nextnum > choices:
                    nextnum -= choices
                votes[row][col] = nextnum
                nextnum += 1
    return votes


def analyse_votes(votes):
    rows = len(votes)
    cols = len(votes[0])
    result = []
    for col in range(cols):
        counts = {}
        for row in range(rows):
            num = votes[row][col]
            if num in counts:
                counts[num] += 1
            else:
                counts[num] = 1
        sort_row = sorted(counts.items(), key=lambda x: x[1], reverse=True)
        result.append(sort_row[0])
        counts.clear()

    print('The Champion'.center(50, '*'))
    for r in range(len(result)):
        print('column %2d: ' % (r + 1,), result[r])

    print('Last votes: '.center(50, '*'))
    for r in votes:
        print(r)


def main():
    votes = lucky_seven()
    analyse_votes(votes)


if __name__ == '__main__':
    main()
