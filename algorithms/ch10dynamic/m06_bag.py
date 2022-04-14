# -*- encoding: utf-8 -*-
"""
动态规划解决0-1背包问题
有n个商品a[0..n]，价值v[0..n]美元，重量w[0..n]磅。一个背包最多能承重top磅。
怎样装商品能获得最大价值。
"""


def bag_choice(v, w, top):
    n = len(v) - 1
    # 先初始化最优解值二维数组
    # vals[i][w]表示：对于前i个物品，当前背包的容量为w时，这种情况下可以装下的最大价值
    vals = [[0 for _ in range(top + 1)] for _ in range(n + 1)]
    # 用来保存每个最优方案三维数组，ans[i][j]表示前i个物品上限为j时候的最优方案
    ans = [[[0 for _ in range(i + 1)] for _ in range(top + 1)] for i in range(n + 1)]
    for i in range(1, n + 1):  # 物品选择从1到n
        for j in range(1, top + 1):  # 重量上限从1到top
            if j - w[i] < 0:
                # 这时候只能选择不选i
                vals[i][j] = vals[i - 1][j]
                # 方案为前i-1最优方案+不选择i
                ans[i][j] = ans[i - 1][j] + [0]
            else:
                # 不选择i的时候，则最优解就是前i-1个物品上限为j的最优解
                unchoose_val = vals[i - 1][j]
                # 选择i的时候，则最优解就是前i-1个物品上限为j-w[i]最优解+v[i]的和
                choose_val = vals[i - 1][j - w[i]] + v[i]
                if unchoose_val > choose_val:
                    vals[i][j] = unchoose_val
                    # 方案为前i-1最优方案+不选择i
                    ans[i][j] = ans[i - 1][j] + [0]
                else:
                    vals[i][j] = choose_val
                    # 方案为前i-1最优方案+选择i
                    ans[i][j] = ans[i - 1][j - w[i]] + [1]
    return vals[n][top], ans[n][top]


if __name__ == '__main__':
    w = [0, 1, 2, 12, 1, 4]  # 重量数组
    v = [0, 1, 2, 4, 2, 10]  # 价值数组
    top = 7  # 背包重量上限
    print(bag_choice(v, w, top))
