from typing import List
class BinaryTree:
    def __init__(self, node):
        self.key = node
        self.left = None
        self.right = None
    def __str__(self):
        return str(f"left: ({self.left}) node:({self.key}) right:({self.right})")
    def __repr__(self):
        return self.__str__()
    @staticmethod
    def max_heap(numbers: List[int]):
        node = BinaryTree(numbers[0])
        for index in range(1, len(numbers)):
            new_node = BinaryTree(numbers[index])
            if new_node.key > node.key and node.left == None and node.right == None:
                node, new_node.left = new_node, node
            elif new_node.key > node.key:
                if node.left != None and node.right == None:
                    node, new_node = new_node, node
                    node.left = new_node.key
                    node.right = new_node.left
                elif node.left != None and node.right != None:
                    node, new_node = new_node, node
                    node.left = new_node.key
                    node.right = BinaryTree(new_node.left)
                    node.right.left = new_node.right
                elif node.right != None and node.left == None:
                    node, new_node = new_node, node
                    node.left = new_node.key
                    node.right = new_node.right
            elif new_node.key < node.key:
                pass
        return node


def main()-> None:
    numbers: List[int] = [1, 4, 8, 9, 10, 20]
    max_heap = BinaryTree.max_heap(numbers)
    print(max_heap)

if __name__ == "__main__":
    main()