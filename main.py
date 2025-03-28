from heap_sort import BinaryTree
def main()-> None:
    tree = BinaryTree()
    result = tree.create_binary_tree(numbers = [3, 9, 2, 1, 4, 5])
    print(f"Root: {tree.root}")
    elements = tree.tree_traversal(result)
    print(elements)
    print(f"result : {result}")

if __name__ == "__main__":
    main()