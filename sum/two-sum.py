class TwoSum:
    def two_sum_dictionary(self, nums: List[int], target: int) -> List[int]:
        output = []
        if nums is not None:
            pairs = {}
            for index, num in enumerate(nums):
                if pairs.get(num) is not None: # if obj checks 'Truely' or 'Faly' of obj, like zeroes, if obj is not None checks if obj is singleton None
                    output.append(pairs.get(num))
                    output.append(index)
                    return output
                    
                else:
                    paris[target - num] = index
        return output

    
    def two_sum_sorting(self, nums: List[int], target: int) -> List[int]:
        if nums is not None:
            sorted_nums = sorted(enumerate(nums), key=lambda x: x[1]) # output example [(1,10), (0, 20), (4, 30), (2, 40), (3, 50)]
            left, right = 0, len(nums) - 1
            while (left < right):
                total = sorted_nums[left][1] + sorted_nums[right][1]
                if total == target:
                    return [sorted_nums[left][0], sorted_nums[right][0]]
                elif total < target:
                    left += 1
                else:
                    right -=1
        
        return []