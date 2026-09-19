class Solution:
    def maxSubArray(self, nums: list[int]) -> int:

        res = max(nums)
        curr = 0

        for num in nums:
            curr += num
            res = max(res, curr)
            if curr < 0:
                curr = 0
        
        return res