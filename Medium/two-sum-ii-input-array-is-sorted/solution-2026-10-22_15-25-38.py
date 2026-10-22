class Solution:
    def twoSum(self, numbers: list[int], target: int) -> list[int]:
        
        l, r = 0, len(numbers) - 1

        while l < r:
            left_num = numbers[l]
            right_num = numbers[r]
            total = left_num + right_num
            if total == target:
                return [l + 1, r + 1]
            elif total > target:
                r -= 1
            else:
                l += 1