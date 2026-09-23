class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        
        freq = defaultdict(int)

        for n in nums:
            freq[n] += 1
        
        for key, val in freq.items():
            if val > len(nums) / 2:
                return key
            