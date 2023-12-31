# -*- encoding: utf-8 -*-
"""
迷宫搜索：深度优先算法，通过栈来实现
"""

from algorithms.c01_data_structure.stack.stack_linked_list import LinkedStack


class Point:
    def __init__(self, row, column):
        self.row = row
        self.column = column
        self.parent = None

    def __eq__(self, other):
        return self.row == other.row and self.column == other.column

    def __str__(self):
        return f'({self.row},{self.column})'


def print_path(point):
    """打印路径"""
    stack = LinkedStack()
    while point is not None:
        stack.push(stack)
        point = point.parent
    for point in stack:
        print(point, sep=',')


def run_dfs(maze, root_point, visited_points):
    s = LinkedStack()
    s.push(root_point)
    while not s.is_empty():
        current_point = s.pop()
        if current_point not in visited_points:
            visited_points.add(current_point)
            if current_point == maze.goal:
                print_path(current_point)
                return current_point
            # 构造当前节点的东南西北节点作为邻居节点
            neighbors = []
            for neighbor in neighbors:
                neighbor.parent = current_point
                s.push(neighbor)
    print('find no path')
