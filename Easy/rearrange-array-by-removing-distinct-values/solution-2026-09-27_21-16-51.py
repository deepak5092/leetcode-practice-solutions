from collections import defaultdict
class Solution:
    def rearrangeArray(self, nums: list[int]) -> list[int]:

        cntr = defaultdict(int)
        ans = []
        for num in nums:
            cntr[num] += 1

        total = len(nums)
        curr = 0 

        while curr != total:
            freq = []
            new_cntr = defaultdict(int)
            for num, cnt in cntr.items():
                curr += 1
                freq.append(num)
                if cnt > 1:
                    new_cntr[num] = cnt - 1 
            cntr = new_cntr
            freq.sort()
            ans += freq 

        return ans