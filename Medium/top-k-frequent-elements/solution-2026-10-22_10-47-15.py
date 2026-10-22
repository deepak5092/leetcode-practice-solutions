class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        
        res = []
        cntr = defaultdict(int)
        freq_arr = [[] for _ in range(len(nums) + 1)]

        for n in nums:
            cntr[n] += 1
        
        for num, val in cntr.items():
            freq_arr[val].append(num)

        for i in range(len(nums), -1, -1):
            for num in freq_arr[i]:
                res.append(num)
                if len(res) == k:
                    return res

        return res