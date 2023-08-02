# -*- encoding: utf-8 -*-
"""
活动选择问题。
活动序列a[1..n]，开始时间序列s[1..n]，结束时间序列f[1..n]。
每个a[i]活动时间为<s[i], f[i]>。并且满足按照结束时间升序排列
"""


def greedy_activity_selector(s, f):
    n = len(s)
    ans = [0]  # 初始选择第一个活动，必定在其中，这里保存最终活动下标即可。
    for m in range(1, n):
        if s[m] >= f[ans[-1]]:
            ans.append(m)
    return ans


if __name__ == '__main__':
    s = [1, 3, 0, 5, 3, 5, 6, 8, 8, 2, 12]
    f = [4, 5, 6, 7, 9, 9, 10, 11, 12, 14, 16]
    print(greedy_activity_selector(s, f))
