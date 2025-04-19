# -*- encoding: utf-8 -*-
"""
392. 判断子序列
给定字符串 s 和 t ，判断 s 是否为 t 的子序列。

字符串的一个子序列是原始字符串删除一些（也可以不删除）字符而不改变剩余字符相对位置形成的新字符串。
（例如，"ace"是"abcde"的一个子序列，而"aec"不是）。

进阶：
如果有大量输入的 S，称作 S1, S2, ... , Sk 其中 k >= 10亿，你需要依次检查它们是否为 T 的子序列。
在这种情况下，你会怎样改变代码？

算法思路：
通过双指针遍历两个序列，两个相等时，左指针向前一步，直到左指针跑完左边字符串s即可。
python中可通过生成器方式简化算法的写法。

输入：s = "abc", t = "ahbgdc"
输出：true

输入：s = "axc", t = "ahbgdc"
输出：false
"""


class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        t_iter = iter(t)  # 这里需要单独提取出来，否则for中每次都会生成新的迭代器。
        return all(i in t_iter for i in s)


if __name__ == '__main__':
    print(Solution().isSubsequence('abc', 'ahbgdc'))
    print(Solution().isSubsequence('axc', 'ahbgdc'))
    print(Solution().isSubsequence('acb', 'ahbgdc'))
