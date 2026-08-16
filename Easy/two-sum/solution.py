class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        mapNums = {}

        for i, n in enumerate(nums):
            mapNums[n] = i 
        
        for i, n in enumerate(nums):
            t = target - n
            if t in mapNums and mapNums[t] != i:
                return [mapNums[t], i]