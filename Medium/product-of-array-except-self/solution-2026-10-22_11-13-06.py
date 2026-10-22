class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        
        pre_prod = [1] * len(nums)
        pre = 1

        for i, n in enumerate(nums):
            pre_prod[i] *= pre
            pre *= n
        
        post = 1
        for i in range(len(nums) - 1, -1, -1):
            curr = nums[i]
            nums[i] = post * pre_prod[i]
            post *= curr
        
        return nums