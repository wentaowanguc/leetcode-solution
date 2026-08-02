def search(nums: list[int], target: int) -> int:
    length = len(nums)
    pivot = 0
    while nums[pivot] > nums[length - 1]:
        pivot += 1

    if target <= nums[length - 1]:
        left = pivot
        right = length - 1
    else:
        left = 0
        right = pivot - 1

    while left < right:
        mid = left + (right - left) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    if nums[left] == target:
        return left
    elif nums[right] == target:
        return right
    else:
        return -1