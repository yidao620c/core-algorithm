# -*- encoding: utf-8 -*-
"""
20. 有效的括号

给定一个只包括 '('，')'，'{'，'}'，'['，']' 的字符串s ，判断字符串是否有效。

有效字符串需满足：

左括号必须用相同类型的右括号闭合。
左括号必须以正确的顺序闭合。

示例 2：
输入：s = "()[]{}"
输出：true

示例 4：
输入：s = "([)]"
输出：false

例 5：
输入：s = "{[]}"
输出：true

算法思路：栈的最简单的应用。左括号入栈，右括号出栈+对比匹配。不匹配则False，最后栈空则True
"""
from algorithms.c01_data_structure.stack.stack_linked_list import LinkedStack


class Solution:
    def isValid(self, s: str) -> bool:
        p_map = {'{': '}', '[': ']', '(': ')'}
        stack = LinkedStack()
        for ch in s:
            if ch in p_map:
                stack.push(ch)
            else:
                stack_item = stack.pop()
                if stack_item not in p_map or ch != p_map[stack_item]:
                    return False
        return stack.is_empty()


if __name__ == '__main__':
    # print(Solution().isValid(']]]'))
    print(Solution().isValid(']'))
    # s = input('input something: ')
    # print(s)
    # while True:
    #     s = input()
    #     if not s:
    #         break
    #     print(Solution().isValid(s))
