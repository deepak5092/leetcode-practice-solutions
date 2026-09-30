class Solution:
    def maxEqualAdjacentPairs(self, nums: list[int]) -> int:
        
        pairs = defaultdict(int)
        total = 0

        for i in range(1, len(nums)):
            if nums[i] == nums[i-1]:
                total += 1
            else:
                pairs[tuple(sorted([nums[i], nums[i-1]]))] += 1
        
        return total + max(pairs.values()) if pairs else total