class Solution:
    def maxAlternatingSum(self, nums: List[int]) -> int:

        temp = []
        res = 0
        for num in nums:
            temp.append(abs(num))
        
        temp.sort(reverse=True)

        for i in range(len(temp)):
            if i < (len(temp)+1) // 2:
                res += (temp[i]*temp[i])
            else:
                res -= (temp[i]*temp[i])
        
        return res