#!/usr/bin/env python

class BinaryTreeNode:
    """Implementation of a binary tree node

    Args:
        value (Object): The value associated with the node
        left (BinaryTreeNode): The left child of the node
        right (BinaryTreeNode): The right child of the node
        parent (BinaryTreeNode): The parent of the node
    Attributes:
        value (Object): The value associated with the node
        left (BinaryTreeNode): The left child of the node
        right (BinaryTreeNode): The right child of the node
        parent (BinaryTreeNode): The parent of the node

    """
    
    def __init__(self, value, left=None,
                 right=None, parent=None):
        self.value = value
        self.left = left
        self.right = right
        self.parent = parent

    def set_left_child(self, left):
        """Function to add a left child to the node, or replace
        if child already exists

        Args:
            left (BinaryTreeNode): The left child node object
        """
        self.left = left

    def set_right_child(self, right):
        """Function to add a right child to the node, or replace
        if child already exists

        Args:
            right (BinaryTreeNode): The right child node object
        """
        self.right = right

    def get_left_child(self):
        """Return the left child of the node, or return None if no
        child exists

        Returns:
            self.left (BinaryTreeNode): The right child node object
        """
        return self.left

    def get_right_child(self):
        """Return the right child of the node, or return None if no
        child exists

        Returns:
            self.right (BinaryTreeNode): The right child node object
        """
        return self.right

    def has_left_child(self): 
        """Determines if the node contains a left child object

        Returns:
            (bool): Indicates is node contains left child or not
        """
        if self.left == None:
            return False
        else:
            return True

    def has_right_child(self):
        """Determines if the node contains a right child object

        Returns:
            (bool): Indicates is node contains right child or not
        """
        if self.right == None:
            return False
        else:
            return True

class BinaryTree:
    """Impelemntation of a binary tree

    Args:
        root_value (Object): The value of the root node
    Attributes:
        tree (BinaryTreeNode): The root node that represents the tree
    """
    
    def __init__(self, root_value):
        self.tree = BinaryTreeNode(root_value)

    def add_child(self, new_value):
        """Adds a child node in the next available spot that is available
        under a current node

        Args:
            new_value (Object): Value of new node object
        """
        current_node = self.tree
        if not current_node.has_left_child():
            current_node.set_left_child(BinaryTreeNode(new_value))
            current_node = current_node.get_left_child()
        elif not current_node.has_right_child():
            current_node.set_right_child(BinaryTreeNode(new_value))
            current_node = current_node.get_right_child()
        else:
            current_node = current_node[1]

if __name__ == "__main__":
    t = BinaryTree(1)
    t.add_child(3)
    t.add_child(4)
    
