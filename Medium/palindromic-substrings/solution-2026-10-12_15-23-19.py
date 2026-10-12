class Solution:
    def countSubstrings(self, s: str) -> int:

        res = 0
        
        for i in range(len(s)):
    
            # odd length 
            left, right = i, i 
            while left > -1 and right < len(s) and s[left] == s[right]:
                res += 1
                if (right - left + 1) > res:
                    res = right - left + 1
                left -= 1
                right += 1

            # even length
            left, right = i, i + 1  
            while left > -1 and right < len(s) and s[left] == s[right]:
                res += 1
                if (right - left + 1) > res:
                    res = right - left + 1

                left -= 1
                right += 1
            
        return res 