#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
Desc : 红黑树
    红黑树是满足下面红黑性质的二叉搜索树：
        1，每个结点或者是红色的，或者是黑色的
        2，根结点黑色
        3，每个叶子结点（None）是黑色的
        4，如果一个结点是红色的，则它的两个子结点都是黑色的
        5，对每个结点，从该结点到其所有后代叶结点的简单路径上，均包含相同数目的黑色结点。
一个有n个内部结点的红黑树的高度最多为2lg(n+1)
"""
from algorithms.ch01structure.tree.bisearch_tree import treeMinimum


class RBTree():
    COLOR_RED = 0
    COLOR_BLACK = 1

    def __init__(self, root=None):
        self.root = root
        self.nil = RBNode('', RBTree.COLOR_BLACK)
        if root is None:
            self.root = self.nil


class RBNode():
    """节点元素定义"""

    def __init__(self, key, color=RBTree.COLOR_RED, p=None, left=None, right=None):
        self.key = key
        self.color = color
        self.p = p
        self.left = left
        self.right = right


def leftRotate(T, x):
    """
    左旋：
        假设x的右孩子为y，且不为None，以x到y的链作为支轴，
        使y成为该子树新的根结点，x成为y的左孩子，y的左孩子成为x的右孩子
    """
    y = x.right
    x.right = y.left
    if y.left != T.nil:
        y.left.p = x
    y.p = x.p
    if x.p == T.nil:
        T.root = y
    elif x == x.p.left:
        x.p.left = y
    else:
        x.p.right = y
    y.left = x
    x.p = y


def rightRotate(T, x):
    y = x.left
    x.left = y.right
    if y.right != T.nil:
        y.right.p = x
    y.p = x.p
    if x.p == T.nil:
        T.root = y
    elif x == x.p.left:
        x.p.left = y
    else:
        x.p.right = y
    y.right = x
    x.p = y


def rbTreeInsert(T, z):
    """
     红黑树的插入算法
    """
    RED = RBTree.COLOR_RED
    y = T.nil
    x = T.root
    while x != T.nil:
        y = x
        if z.key < x.key:
            x = x.left
        else:
            x = x.right
    z.p = y
    if y == T.nil:
        T.root = z
    elif z.key < y.key:
        y.left = z
    else:
        y.right = z
    z.left = T.nil
    z.right = T.nil
    z.color = RED
    rbInsertFixup(T, z)


def rbInsertFixup(T, z):
    """给结点重新着色，将其保持为红黑树"""
    RED = RBTree.COLOR_RED
    BLACK = RBTree.COLOR_BLACK
    while z.p.color == RED:
        if z.p == z.p.p.left:
            y = z.p.p.right
            if y.color == RED:
                z.p.color = BLACK
                y.color = BLACK
                z.p.p.color = RED
                z = z.p.p
            else:
                if z == z.p.right:
                    z = z.p
                    leftRotate(T, z)
                z.p.color = BLACK
                z.p.p.color = RED
                rightRotate(T, z.p.p)
        elif z.p == z.p.p.right:
            y = z.p.p.left
            if y.color == RED:
                z.p.color = BLACK
                y.color = BLACK
                z.p.p.color = RED
                z = z.p.p
            else:
                if z == z.p.left:
                    z = z.p
                    rightRotate(T, z)
                z.p.color = BLACK
                z.p.p.color = RED
                leftRotate(T, z.p.p)
    T.root.color = BLACK


def rbTransplant(T, u, v):
    """红黑树中子树的替换算法"""
    if u.p == T.nil:
        T.root = v
    elif u == u.p.left:
        u.p.left = v
    else:
        u.p.right = v
    v.p = u.p


def rbTreeDelete(T, z):
    """红黑树删除算法"""
    BLACK = RBTree.COLOR_BLACK
    y = z
    yOriginalColor = y.color
    if z.left == T.nil:
        x = z.right
        rbTransplant(T, z, z.right)
    elif z.right == T.nil:
        x = z.left
        rbTransplant(T, z, z.left)
    else:
        y = treeMinimum(z.right)
        yOriginalColor = y.color
        x = y.right
        if y.p == z:
            x.p = y
        else:
            rbTransplant(T, y, y.right)
            y.right = z.right
            y.right.p = y
        rbTransplant(T, z, y)
        y.left = z.left
        y.left.p = y
        y.color = z.color
    if yOriginalColor == BLACK:
        rbDeleteFixup(T, x)


def rbDeleteFixup(T, x):
    """红黑树删除时的调整算法"""
    RED = RBTree.COLOR_RED
    BLACK = RBTree.COLOR_BLACK
    while x != T.root and x.color == BLACK:
        if x == x.p.left:
            w = x.p.right
            if w.color == RED:
                w.color = BLACK
                x.p.color = RED
                leftRotate(T, x.p)
                w = x.p.right
            if w.left.color == BLACK and w.right.color == BLACK:
                w.color = RED
                x = x.p
            else:
                if w.right.color == BLACK:
                    w.left.color = BLACK
                    w.color = RED
                    rightRotate(T, w)
                    w = x.p.right
                w.color = x.p.color
                x.p.color = BLACK
                w.right.color = BLACK
                leftRotate(T, x.p)
                x = T.root
        elif x == x.p.right:
            w = x.p.left
            if w.color == RED:
                w.color = BLACK
                x.p.color = RED
                rightRotate(T, x.p)
                w = x.p.left
            if w.left.color == BLACK and w.right.color == BLACK:
                w.color = RED
                x = x.p
            else:
                if w.left.color == BLACK:
                    w.right.color = BLACK
                    w.color = RED
                    leftRotate(T, w)
                    w = x.p.left
                w.color = x.p.color
                x.p.color = BLACK
                w.left.color = BLACK
                rightRotate(T, x.p)
                x = T.root
    x.color = BLACK


def inOrderRBWalk(tree):
    """中序遍历二叉搜索树，从小到大输出元素"""
    inOrderRBWalkNode(tree.root, tree.nil)
    print('')


def inOrderRBWalkNode(node, ni):
    """中序遍历二叉搜索树，从小到大输出元素"""
    if node and node != ni:
        inOrderRBWalkNode(node.left, ni)
        print(node.key),
        inOrderRBWalkNode(node.right, ni)


if __name__ == '__main__':
    ss = [4, 23, 65, 22, 12, 3, 7, 1, 256, 34, 27]
    tree = RBTree()
    for i in ss:
        rbTreeInsert(tree, RBNode(i))
    inOrderRBWalk(tree)
    n = RBNode(26)
    rbTreeInsert(tree, n)
    inOrderRBWalk(tree)
    rbTreeDelete(tree, n)
    inOrderRBWalk(tree)
