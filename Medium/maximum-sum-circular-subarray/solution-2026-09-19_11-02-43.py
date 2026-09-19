class Solution:
    def maxSubarraySumCircular(self, nums: list[int]) -> int:

        cur_max, global_max = 0, float('-inf')
        cur_min, global_min = 0, float('inf')
        total = 0

        for num in nums:
            total += num

            cur_max += num 
            cur_max = max(cur_max, num)
            global_max = max(cur_max, global_max)
            
            cur_min += num
            cur_min = min(cur_min, num)
            global_min = min(cur_min, global_min)  


        if global_max < 0:
            return global_max
        else:
            print(global_max, total, global_min)
            return max(global_max, total - global_min)