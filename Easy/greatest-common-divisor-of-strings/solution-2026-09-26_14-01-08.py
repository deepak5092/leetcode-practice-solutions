class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        
        # ensure str2 is smallest amongst 2
        if len(str1) > len(str2):
            str1, str2 = str2, str1
        len1, len2 = len(str1), len(str2)
    
        res = ""
        for i in range(len(str2)):
            cur_str = str2[:i + 1]
            cur_len = i + 1

            if len1 % cur_len != 0 or len2 % cur_len != 0:
                continue 
            
            # check for str1
            mult1 = len1 // cur_len
            mult2 = len2 // cur_len

            if cur_str * mult1 == str1 and cur_str * mult2 == str2:
                res = cur_str
        
        return res