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

        # updating root height of current node
        root.height = 1 + max(self.get_height(root.left), self.get_height(root.right))

        # get balance factor and balance tree
        balance_factor = self.get_balance_factor(root)

        # if balance_factor difference is greater than 1 then need to rotate
        if balance_factor > 1:
            if value < root.left.value:
                return self.right_rotate(root)
            else:
                # you have to rotate twice 
                root.left = self.left_rotate(root.left)
                return self.right_rotate(root)
        if balance_factor < -1:
            if value > root.right.value:
                return self.left_rotate(root)
            else:
                # you have to rotate twice 
                root.right = self.right_rotate(root.right)
                return self.left_rotate(root)
        
        return root

    def get_height(self, root):
        if not root:
            return 0
        return root.height

    def get_balance_factor(self, root):
        if not root:
            return 0
        return self.get_height(root.left) - self.get_height(root.right)

    # z could be root?
    # left rotation
    def left_rotate(self, z):
        y = z.right
        T2 = y.left

        # swapping
        y.left = z
        z.right = T2

        # updating the node's heights
        z.height = 1 + max(self.get_height(z.left), self.get_height(z.right))
        y.height = 1 + max(self.get_height(y.left), self.get_height(y.right))

        # return new root node
        return y
    
    def right_rotate(self, z):
        y = z.left
        T3 = y.right

        y.right = z
        z.left = T3

        z.height = 1 + max(self.get_height(z.left), self.get_height(z.right))
        y.height = 1 + max(self.get_height(y.left), self.get_height(y.right))

        return y






