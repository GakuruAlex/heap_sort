from typing import List
from math import floor

def max_heap(numbers: List[int]) -> List[int]:
    current_index = 0

    first_leaf = floor(len(numbers) / 2) - 1
    print(f"Index of first first leaf: {first_leaf}")
    for n in range(first_leaf, len(numbers) - 1):
        current_index = n

        parent = floor(current_index - 1 / 2)
        left = 2 * parent + 1
        right = 2 * parent + 2
        print(f"Parent : {parent}, Left: {left} Right: {right}")
        if left < len(numbers):
            if numbers[parent] < numbers[left]:
                numbers[parent], numbers[left] = numbers[left], numbers[parent]
        if right < len(numbers):
            if numbers[parent] < numbers[right]:
                numbers[parent], numbers[right] = numbers[right], numbers[parent]
        print(f"Parent : {parent}, Left: {left} Right: {right}")