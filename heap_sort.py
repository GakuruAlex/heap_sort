from typing import List
from math import floor

def max_heap(numbers: List[int]) -> List[int]:

    current_index = floor(len(numbers) / 2)
    times = (len(numbers) - current_index)
    while current_index > 0:
        print(f"Index of current: {current_index}")
        for index in range(current_index, times + 1):
            print(f"Index: {index}, times to loop: {(times + 1) - index}")
            parent = floor((index - 1) / 2)
            left = (2 * parent) + 1
            right = (2 * parent) + 2
            print(f"Parent: {parent} Left index {left} Right index: {right}")

            if left < len(numbers) and left > 0:
                    print(f"Before swap on the left Parent: {numbers[parent]}, Left: {numbers[left]}")
                    if numbers[parent] < numbers[left]:
                        numbers[parent], numbers[left] = numbers[left], numbers[parent]
                        print(f"After swap on the left Parent: {numbers[parent]}, Left: {numbers[left]}")
                    print()
            if right < len(numbers) and right > 0:
                    print(f"Before swap on the right ,  Parent: {numbers[parent]}, Right: {numbers[right]}")
                    if numbers[parent] < numbers[right]:
                        numbers[parent], numbers[right] = numbers[right], numbers[parent]
                        print(f"After swap on the right ,  Parent: {numbers[parent]}, Right: {numbers[right]}")
                    print()

        current_index -= 1
        times = times // 2
    return numbers

def sort_list(numbers: List[int]) -> List[int]:
    ...