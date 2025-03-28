from node import Node
from typing import List
class BinaryTree:
    def __init__(self):
        self.root = None
    def __str__(self)-> str:
        return str(self.root)
    def __repr__(self):
        return self.__str__()

    def create_binary_tree(self, node = None, numbers: List[int] = None, index = 0)-> Node:
        """_Create binary tree given a list of numbers_

        Args:
            node (_type_, optional): _Current node_. Defaults to None.
            numbers (List[int], optional): _A list of integers_. Defaults to None.
            index (int, optional): _current index in list_. Defaults to 0.

        Returns:
            Node: _Root node of the binary tree_
        """
        if len(numbers) == 0:
            return None
        if  index == 0:
            node = Node(numbers[index])
            self.root = node
        if node == None:
            return None
        left = 2 * index + 1
        right = 2 * index + 2
        if left < len(numbers):
                node.left = Node(numbers[left])
        if right < len(numbers):
                node.right = Node(numbers[right])
        self.create_binary_tree(numbers= numbers, node = node.left, index= index + left)
        self.create_binary_tree(numbers= numbers, node= node.right, index= index + right)
        return node


    def tree_traversal(self, node):
        """_Traverse the binary tree pre-order_
        Args:
            node (_type_): _Root of the binary tree_

        Returns:
            _type_: _A list of keys of the binary tree_
        """
        if node == None:
            return []
        return [node.key] + self.tree_traversal(node.left) + self.tree_traversal(node.right)

