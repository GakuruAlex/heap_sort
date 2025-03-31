
from typing import List
from heap_sort import max_heap

def main()-> None:
    numbers: List[int] = [9,4,3,8,10,2,5]
    max_heap(numbers= numbers)
    print(numbers)

if __name__ == "__main__":
    main()