# -*- encoding: utf-8 -*-
"""
回溯法框架代码
"""


def backtrack(state, choices, res):
    # 判断是否为解
    if is_solution(state):
        # 记录解
        record_solution(state, res)
        # 不再继续搜索
        return
    # 遍历所有选择
    for choice in choices:
        # 剪枝
        if is_valid(state, choice):
            # 尝试：做出选择，更新状态
            make_choice(state, choice)
            # 使用新的状态继续寻找
            backtrack(state, choices, res)
            # 回退：撤销选择，恢复到之前的状态
            undo_choice(state, choice)


def is_solution(state) -> bool:
    return True


def record_solution(state, res):
    pass


def is_valid(state, choice) -> bool:
    return True


def make_choice(state, choice):
    pass


def undo_choice(state, choice):
    pass
