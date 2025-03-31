from typing import List
from math import floor

def max_heap(numbers: List[int]) -> List[int]:

    current_index = floor(len(numbers) / 2) - 1
    while current_index > 0:
        print(f"Index of first first leaf: {current_index}")
        for index in range(current_index, len(numbers) - 1):

            parent = floor(index - 1 / 2)
            left = 2 * parent + 1
            right = 2 * parent + 2

            if left < len(numbers):
                if left > 0 and right > 0:
                    print(f"Before swap  Parent: {numbers[parent]}, Left: {numbers[left]} Right: {numbers[right]}")
                if numbers[parent] < numbers[left]:
                    numbers[parent], numbers[left] = numbers[left], numbers[parent]
            if right < len(numbers):
                if numbers[parent] < numbers[right]:
                    numbers[parent], numbers[right] = numbers[right], numbers[parent]
                if left > 0 and right > 0:
                    print(f"After swap  Parent: {numbers[parent]}, Left: {numbers[left]} Right: {numbers[right]}")
        current_index -= 1