import sys


class TreeNode(object):
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        # cause height leaf is 1
        self.height = 1

class AVLTree(object):
    """
    Time Complexity: O(logN)
    """
    
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
            # comparing values
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
    
    # right rotate
    def right_rotate(self, z):
        y = z.left
        T3 = y.right

        # swapping
        y.right = z
        z.left = T3

        # updating heights
        z.height = 1 + max(self.get_height(z.left), self.get_height(z.right))
        y.height = 1 + max(self.get_height(y.left), self.get_height(y.right))

        # return new root node
        return y

    def delete_node(self, root, value):
        if not root:
            return root
        elif value < root.value:
            root.left = self.delete_node(root.left, value)
        elif value > root.value:
            root.right = self.delete_node(root.right, value)

        else:
            if root.left is None:
                # return right node and set root node to None if root.left doesn't exist
                temp_node = root.right
                root = None
                return temp_node
            elif root.right is None:
                temp_node = root.left
                root = None
                return temp_node
            temp_node = self.get_min_value_node(root.right)
            # set root value to lowest
            root.value = temp_node.value

            root.right = self.delete_node(root.right, temp_node.value)

        if root == None:
            return root

        # update and get balance factor
        root.height = 1 + max(self.get_height(root.left), self.get_height(root.right))

        balance_factor = self.get_balance_factor(root)

        # balance tree
        if balance_factor > 1:
            if self.get_balance_factor(root.left) >= 0:
                return self.right_rotate(root)
            else:
                # rotate twice to balance
                root.left = self.left_rotate(root.left)
                return self.right_rotate(root)
        
        if balance_factor < -1:
            if self.get_balance_factor(root.right) <= 0:
                return self.left_rotate(root)
            else:
                root.right = self.right_rotate(root.right)
                return self.left_rotate(root)
        
        return root


    # recursive method to get node with smallest value
    def get_min_value_node(self, root):
        if root is None or root.left is None:
            return root
        return self.get_min_value_node(root.left)

    def printHelper(self, currPtr, indent, last):
        if currPtr != None:
            sys.stdout.write(indent)
            if last:
                sys.stdout.write("R--")
                indent += "     "
            else:
                sys.stdout.write("L--")
                indent += "|    "
            print(currPtr.value)
            self.printHelper(currPtr.left, indent, False)
            self.printHelper(currPtr.right, indent, True)



myTree = AVLTree()
root = None
nums = [33, 13, 52, 9, 21, 61, 8, 11]
for num in nums:
    root = myTree.insert_node(root, num)
myTree.printHelper(root, "", True)
key = 13
root = myTree.delete_node(root, key)
print("After Deletion: ")
myTree.printHelper(root, "", True)



