import sys


class TreeNode(object):
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        # cause height leaf is 1
        self.height = 1

class AVLTree(object):
    
    def insert_node(self, root, value):
        # find the proper location in tree to add node 
        if not root:
            return TreeNode(value)
        elif value < root.value:
            root.left = self.insert_node(root.left, value)
        else:
            root.right = self.insert_node(root.right, value)

        root.height = 1 + max(self.get_height(root.left), self.get_height(root.right))

        # get balance factor and balance tree
        balance_factor = self.get_balance_factor(root)

    
    def get_height(self, root):
        if not root:
            return 0
        return root.height



