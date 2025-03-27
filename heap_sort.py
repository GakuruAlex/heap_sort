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
        #node = Node(numbers[0])
        # if isinstance(numbers, list) and len(numbers) == 3:
        #     node.left = Node(numbers[1])
        #     node.right = Node(numbers[2])
        #     return node
        # if isinstance(numbers, list) and len(numbers) == 2:
        #     node.left = Node(numbers[1])
        #     return node
        # if isinstance(numbers, list) and len(numbers) == 1:
        #     return Node(numbers[0])
        # if len(numbers) > 3:
        #     node.left = self.create_binary_tree()
        if index == 0:
            node = Node(numbers[index])
            self.root = node
        if node == None:
            return
        if index < len(numbers):
            i = 2 * index
            if i + 1 < len(numbers):
                if node.left == None:
                    node.left = Node(numbers[i + 1])
            if i + 2 < len(numbers):
                if node.right == None:
                    node.right = Node(numbers[i + 2])
            if index % 2 == 0:
                self.create_binary_tree(node = node.right, numbers= numbers, index= index + 1)
            if index % 2 != 0:
                self.create_binary_tree(node= node.left, numbers= numbers, index = index + 1)
        else:
            return
        return node


    def tree_traversal(self, node):
        if node == None:
            return []
        return [node.key] + self.tree_traversal(node.left) + self.tree_traversal(node.right)



def main()-> Node:
    tree = BinaryTree()
    tree.create_binary_tree(numbers = [3, 9, 2, 1, 4, 5])
    print(tree.root)
    elements = tree.tree_traversal(tree.root)
    print(elements)

if __name__ == "__main__":
    main()