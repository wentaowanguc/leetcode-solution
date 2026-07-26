from typing import Final


class ArrayReader:
    INT_MAX_VALUE: Final[int] = 2**31 - 1

    def __init__(self):
        self.nums = []


    def get(self, index: int) -> int:
        if index < 0 or index >= len(self.nums):
            return self.INT_MAX_VALUE
        else:
            return self.nums[index]


    def append(self, value: int):
        self.nums.append(value)



def search(reader: ArrayReader, target: int) -> int:
    left, right = 0, 1
    while reader.get(right) < target:
        right *= 2

    while left < right:
        mid = (left + right) // 2
        mid_val = reader.get(mid)
        if mid_val == target:
            return mid
        elif mid_val < target:
            left = mid + 1
        else:
            right = mid - 1

    if reader.get(left) == target:
        return left
    elif reader.get(right) == target:
        return right
    else:
        return -1