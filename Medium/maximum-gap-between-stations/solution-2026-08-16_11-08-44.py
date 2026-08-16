class Solution:
    def maximumGap(self, skill: str, station: str) -> int:
        
        res = 0
        left_sol = []
        i, j = 0, 0 
        while j < len(skill):
            while i < len(station) and skill[j] != station[i]:
                i += 1
            left_sol.append(i)
            j += 1
            i += 1
        
        right_sol = [0] * len(skill)
        i, j = len(station) - 1, len(skill) - 1
        while j >= 0:
            while i >= 0 and skill[j] != station[i]:
                i -= 1
            right_sol[j] = i
            i -= 1
            j -= 1

        for i in range(len(skill) - 1):
            res = max(res, right_sol[i + 1] - left_sol[i])
        
        return res