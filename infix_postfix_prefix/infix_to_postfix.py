#!/usr/bin/env python

class BinaryTreeNode:
    def __init__(self, value, left=None,
                 right=None, parent=None):
        self.value = value
        self.left = left
        self.right = right
        self.parent = parent

    def set_left_child(self, left):
        self.left = left

    def set_right_child(self, right):
        self.right = right

    def get_left_child(self):
        return self.left

    def get_right_child(self):
        return self.right

    def has_left_child(self):
        if self.left == None:
            return False
        else:
            return True

    def has_right_child(self):
        if self.right == None:
            return False
        else:
            return True

class BinaryTree:
    def __init__(self, root_value):
        self.tree = [root_value,[]]

    def add_left_child(self, key, new_value):
        for elem in self.tree:
            

def infix_to_postfix(exp):
    exp = exp.replace(" ","")
    operations = []
    for char in exp:
        print(char)

if __name__ == "__main__":
    exp = input("Expression to Convert: ")
    infix_to_postfix(exp)
