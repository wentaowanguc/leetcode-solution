class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
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