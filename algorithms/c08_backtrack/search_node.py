# -*- encoding: utf-8 -*-
"""
在二叉树中搜索所有值为的节点，请返回根节点到这些节点的路径。
使用回溯框架代码实现
"""


def backtrack(state: list[int], choices: list[int], res: list[list[int]]):
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


def is_solution(state: list[int]) -> bool:
    return state[-1] == 7


def record_solution(state, res):
    pass


def is_valid(state, choice) -> bool:
    return True


def make_choice(state, choice):
    pass


def undo_choice(state, choice):
    pass
