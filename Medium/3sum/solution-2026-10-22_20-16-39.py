class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        
        nums.sort()
        res = []
        visit = set()


        for i, first in enumerate(nums):
            if first in visit:
                continue
            j, k = i + 1, len(nums) - 1
            while j < k:
                second = nums[j]
                third = nums[k]
                total = first + second + third

                if total == 0:
                    print(i, j, k)
                    res.append([first, second, third])
                    while k - 1 > j and nums[k] == nums[k - 1]:
                        k -= 1
                    while j + 1 < k and nums[j] == nums[j + 1]:
                        j += 1
                    j += 1
                    k -= 1
                elif total > 0:
                    while k - 1 > j and nums[k] == nums[k - 1]:
                        k -= 1
                    k -= 1
                else:
                    while j + 1 < k and nums[j] == nums[j + 1]:
                        j += 1
                    j += 1
            visit.add(first)
        
        return res