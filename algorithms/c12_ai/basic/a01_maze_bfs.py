# -*- encoding: utf-8 -*-
"""
迷宫搜索：广度优先算法
"""

from algorithms.c01_linear.queue.linked_queue import LinkedQueue
from algorithms.c01_linear.stack.stack_linked_list import LinkedStack


class Point:
    def __init__(self, row, column):
        self.row = row
        self.column = column
        self.parent = None

    def __eq__(self, other):
        return self.row == other.row and self.column == other.column

    def __str__(self):
        return f'({self.row},{self.column})'

    def path(self):
        point = self
        stack = LinkedStack()
        while point is not None:
            stack.push(self)
            point = point.parent
        for point in stack:
            print(point, sep=',')


def run_bfs(maze, current_point, visited_points):
    q = LinkedQueue()
    q.enqueue(current_point)
    visited_points.add(current_point)
    while not q.is_empty():
        current_point = q.dequeue()
        # 当前节点的东南西北节点作为邻居节点
        neighbors = []
        for neighbor in neighbors:
            if neighbor not in visited_points:
                neighbor.parent = current_point
                q.enqueue(neighbor)
                visited_points.add(neighbor)
                if neighbor == maze.goal:
                    neighbor.path()
                    return
    print('find no path')
