#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# at301_bisearchtree: 二叉搜索树
"""
    Topic: sample
    Desc : 二叉搜索树
        二叉搜索树是指：对每个节点，其左子树元素不大于它，右子树元素不小于它
"""
__author__ = 'Xiong Neng'


class Tree():
    def __init__(self, root):
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
    root = tree.root
    if root:
        inOrderWalk(root.left)
        print root.key
        inOrderWalk(root.right)


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


def treeMinimum(tree):
    root = tree.root
    while root.left:
        root = root.left
    return root


def treeMaximum(tree):
    root = tree.root
    while root.right:
        root = root.right
    return root


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
    if not y:  # empty tree
        tree.root = node
    elif node.key < y.key:
        y.left = node
    else:
        y.right = node

