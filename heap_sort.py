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
        return node


def main()-> None:
    numbers: List[int] = [1, 4, 8, 9, 10, 20]
    max_heap = BinaryTree.max_heap(numbers)
    print(max_heap)

if __name__ == "__main__":
    main()