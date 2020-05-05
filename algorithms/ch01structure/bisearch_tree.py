#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
Desc : 二叉搜索树
    二叉搜索树是指：对每个节点，其左子树元素不大于它，右子树元素不小于它
"""


class Tree():
    def __init__(self, root=None):
        self.root = root


class Node():
    """节点元素定义"""

    def __init__(self, key, p=None, left=None, right=None):
        self.key = key
        self.p = p
        self.left = left
        self.right = right


def inOrderWalk(tree):
    """中序遍历二叉搜索树，从小到大输出元素"""
    inOrderWalkNode(tree.root)
    print('')


def inOrderWalkNode(node):
    """中序遍历二叉搜索树，从小到大输出元素"""
    if node:
        inOrderWalkNode(node.left)
        print(node.key),
        inOrderWalkNode(node.right)


def treeSearch(tree, x):
    """二叉树搜索，递归版本"""
    root = tree.root
    if not root or x == root.key:
        return root
    if x < root.key:
        return treeSearch(root.left, x)
    else:
        return treeSearch(root.right, x)


def treeSearch2(tree, x):
    """"二叉树搜索，迭代版本"""
    root = tree.root
    while root and x != root.key:
        if x < root.key:
            root = root.left
        else:
            root = root.right
    return root


def treeMinimum(node):
    while node.left:
        node = node.left
    return node


def treeMaximum(node):
    while node.right:
        node = node.right
    return node


def nextNode(node):
    """查找后继节点"""
    if node.right:
        return treeMinimum(node.right)
    p = node.p
    while p and node == p.right:
        node = p
        p = node.p
    return p


def preNode(node):
    """查找前驱节点"""
    if node.left:
        return treeMaximum(node.left)
    p = node.p
    while p and node == p.left:
        node = p
        p = node.p
    return p


def treeInsert(tree, node):
    """二叉搜索树的插入算法"""
    y = None
    root = tree.root
    while root:
        y = root
        if node.key < root.key:
            root = root.left
        else:
            root = root.right
    node.p = y
    if y is None:  # empty tree
        tree.root = node
    elif node.key < y.key:
        y.left = node
    else:
        y.right = node


def treeDelete(T, z):
    """
    二叉搜索树的删除算法
    算法思想：
    1，如果z没有孩子节点，简单简单的将其删除，并修改它的父节点，用None作为孩子来替换
    2，如果z只有一个孩子，那么将这个孩子提升到树中z的位置，并修改z的父节点，用z的孩子替换z
    3，如果z有两个孩子，那么寻找z的后继节点y（一定在z的右子树中），找到后：
        i：如果y是z的右孩子，那么用y替换z，并仅留下y的右孩子。（y肯定没有左孩子）
        ii：否则，先用y的右孩子替换，然后再用y替换z
    """
    if z.left is None:
        transplant(T, z, z.right)
    elif z.right is None:
        transplant(T, z, z.left)
    else:
        y = treeMinimum(z.right)
        if y.p != z:
            transplant(T, y, y.right)
            y.right = z.right
            y.right.p = y
        transplant(T, z, y)
        y.left = z.left
        y.left.p = y


def transplant(T, u, v):
    """子树替换：在树T中用根节点节点为v的子树替换根节点为u的子树"""
    if u.p is None:
        T.root = v
    elif u == u.p.left:
        u.p.left = v
    else:
        u.p.right = v
    if v:
        v.p = u.p


if __name__ == '__main__':
    ss = [4, 23, 65, 22, 12, 3, 7, 1, 256, 34, 27]
    tree = Tree()
    for i in ss:
        treeInsert(tree, Node(i))
    n = Node(26)
    treeInsert(tree, n)
    inOrderWalk(tree)
    treeDelete(tree, n)
    inOrderWalk(tree)
