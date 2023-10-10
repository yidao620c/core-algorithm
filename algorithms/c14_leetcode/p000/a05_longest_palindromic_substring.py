# -*- encoding: utf-8 -*-
"""
5. 最长回文子串
给你一个字符串 s，找到 s 中最长的回文子串。
如果字符串的反序与原始字符串相同，则该字符串称为回文字符串。

示例 1：
输入：s = "babad"
输出："bab"
解释："aba" 同样是符合题意的答案。
"""


class Solution:
    def longestPalindrome(self, s: str) -> str:
        res = ''
        for i in range(len(s)):
            s1 = self._max_palindrome(s, i, i)
            s2 = self._max_palindrome(s, i, i + 1)
            res = res if len(res) > len(s1) else s1
            res = res if len(res) > len(s2) else s2
        return res

    def _max_palindrome(self, s: str, l: int, r: int) -> str:
        step = 0
        max_index = len(s) - 1
        while True:
            left = l - step
            right = r + step
            if left < 0 or right > max_index:
                break
            if s[left] != s[right]:
                break
            step += 1
        return s[left + 1:right]


if __name__ == '__main__':
    print(Solution().longestPalindrome("babad"))
