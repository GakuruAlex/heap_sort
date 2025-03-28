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
        # if index == 0:
        #     node = Node(numbers[index])
        #     self.root = node
        # if node == None:
        #     return None
        # while index < len(numbers):
        #     node_index_left = 2 * index + 1
        #     node_index_right = 2 * index + 2
        #     if  node_index_left  < len(numbers):
        #         node.left = Node(numbers[node_index_left])
        #     if  node_index_right < len(numbers):
        #         node.right = Node(numbers[node_index_right])
        #     index += 1
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
        if (index + left) % 2 != 0:
                self.create_binary_tree(numbers= numbers, node = node.left, index= left)
        if (index + right) % 2 == 0:
                self.create_binary_tree(numbers= numbers, node= node.right, index= right)
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