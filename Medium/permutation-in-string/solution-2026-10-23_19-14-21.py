class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False 
        
        dict_s1 = defaultdict(int)
        for ch in s1:
            dict_s1[ch] += 1

        l, r = 0, 0
        window = {}
        while r < len(s2):
            curr = s2[r]
            if curr not in dict_s1:
                window = {}
                l = r + 1
                r += 1
                continue

            window[curr] = 1 + window.get(curr, 0)
            while window[curr] > dict_s1[curr]:
                window[s2[l]] -= 1
                l += 1
            
            if window == dict_s1:
                return True
            
            r += 1
            
            
        
        return False