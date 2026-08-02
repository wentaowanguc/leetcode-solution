def search(nums: list[int]) -> int:
    left, right = 0, len(nums) - 1
    # Move to the right most index with same value
    while left < len(nums) - 1 and nums[left] == nums[left + 1]:
        left += 1

    # Move to the left most index with same value
    while right > 0 and nums[right] == nums[right - 1]:
        right -= 1

    while left + 1 < right:
        mid = left + (right - left) // 2
        if nums[mid] <= nums[right]:
            right = mid
            while right > 0 and nums[right] == nums[right - 1]:
                right -= 1
        else:
            left = mid
            while left < len(nums) - 1 and nums[left] == nums[left + 1]:
                left += 1

    return nums[left] if nums[left] <= nums[right] else nums[right]