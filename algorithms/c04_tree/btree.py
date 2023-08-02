# -*- encoding: utf-8 -*-
"""
description
"""


class BTreeNode:
    def __init__(self, leaf=False):
        self.keys = []
        self.children = []
        self.leaf = leaf

    def split(self, parent, key):
        new_node = BTreeNode(self.leaf)

        mid = len(self.keys) // 2
        split_key = self.keys[mid]

        parent.add_key(split_key)

        new_node.children = self.children[mid + 1:]
        self.children = self.children[:mid + 1]

        new_node.keys = self.keys[mid + 1:]
        self.keys = self.keys[:mid]

        parent.children = parent.add_child(new_node)

        if key < split_key:
            return self
        else:
            return new_node

    def add_key(self, key):
        self.keys.append(key)
        self.keys.sort()

    def add_child(self, new_node):
        i = len(self.children) - 1
        while i >= 0 and self.children[i].keys[0] > new_node.keys[0]:
            i -= 1
        return self.children[:i + 1] + [new_node] + self.children[i + 1:]

    def __str__(self):
        return str(self.keys)


class BTree:
    def __init__(self, t):
        self.t = t
        self.root = BTreeNode(leaf=True)

    def insert(self, key):
        node = self.root

        if len(node.keys) == (2 * self.t) - 1:
            new_root = BTreeNode()
            new_root.children.append(self.root)
            new_root.leaf = False

            node = node.split(new_root, key)
            self.root = new_root
        while not node.leaf:
            i = 0
            while i < len(node.keys) and key > node.keys[i]:
                i += 1

            if len(node.children[i].keys) == (2 * self.t) - 1:
                node = node.split(node, i)
                if key > node.keys[i]:
                    i += 1

            node = node.children[i]

        if key not in node.keys:
            node.add_key(key)

            if len(node.keys) == (2 * self.t) - 1:
                self.split(node)

    def split(self, node):
        new_node = BTreeNode(node.leaf)

        mid = len(node.keys) // 2
        split_key = node.keys[mid]

        parent = node
        parent.add_key(split_key)

        new_node.children = node.children[mid + 1:]
        node.children = node.children[:mid + 1]

        new_node.keys = node.keys[mid + 1:]
        node.keys = node.keys[:mid]

        parent.children = parent.add_child(new_node)

    def __str__(self):
        return str(self.root)


# Example usage:
tree = BTree(t=2)

tree.insert(1)
tree.insert(3)
tree.insert(7)
tree.insert(10)
tree.insert(11)
tree.insert(13)
tree.insert(14)
tree.insert(15)
tree.insert(18)
tree.insert(16)
tree.insert(19)
tree.insert(24)
tree.insert(25)
tree.insert(26)
tree.insert(21)
tree.insert(4)
tree.insert(5)
tree.insert(20)
tree.insert(22)
tree.insert(2)
tree.insert(17)
tree.insert(12)
tree.insert(6)

print(tree)
