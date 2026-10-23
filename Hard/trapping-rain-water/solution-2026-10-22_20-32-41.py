class Solution:
    def trap(self, height: list[int]) -> int:
        
        right_max = [0] * len(height)
        right_max[len(height) - 1] = 0
        res = 0

        for i in range(len(height) - 2, -1, -1):
            right_max[i] = max(height[i+1], right_max[i+1])
        
        left_max = 0 

        for i, h in enumerate(height):
            res += max((min(left_max, right_max[i]) - h), 0)
            left_max = max(left_max, h)
        
        return res