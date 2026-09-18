class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        
        res = ""
        min_len = min(len(s) for s in strs)

        for i in range(min_len):
            valid = True
            first_char = strs[0][i]
            for word in strs[1:]:
                if word[i] != first_char:
                    valid = False
                    break
            if not valid:
                return res
            res += first_char

        return res