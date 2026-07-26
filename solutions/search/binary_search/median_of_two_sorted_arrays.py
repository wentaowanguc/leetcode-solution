def findMedianSortedArrays(nums1: list[int], nums2: list[int]) -> float:
    total_length = len(nums1) + len(nums2)
    merged_nums = []
    index1, index2 = 0, 0
    while index1 < len(nums1) and index2 < len(nums2):
        if nums1[index1] < nums2[index2]:
            merged_nums.append(nums1[index1])
            index1 += 1
        elif nums1[index1] > nums2[index2]:
            merged_nums.append(nums2[index2])
            index2 += 1
        else:
            merged_nums.append(nums1[index1])
            merged_nums.append(nums2[index2])
            index1 += 1
            index2 += 1

    while index1 < len(nums1):
        merged_nums.append(nums1[index1])
        index1 += 1

    while index2 < len(nums2):
        merged_nums.append(nums2[index2])
        index2 += 1

    mid = (total_length - 1) // 2

    if total_length % 2 == 0:
        return (merged_nums[mid] + merged_nums[mid + 1]) / 2
    else:
        return merged_nums[mid]