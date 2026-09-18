class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:

        num_idx = {}

        for i, num in enumerate(nums):
            num_idx[num] = i 
        
        for i, num in enumerate(nums):
            check = target - num 
            if check in num_idx and num_idx[check] != i:
                return [i, num_idx[check]]