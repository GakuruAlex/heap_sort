class Node:
    def __init__(self, key)-> None:
        self.key = key
        self.left = None
        self.right = None
    def __str__(self)-> str:
        return f"{self.key}"
    def __repr__(self):
        return self.__str__()