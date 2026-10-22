class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        
        dict_words = defaultdict(list)

        for s in strs:
            arr = [0] * 26
            for ch in s:
                arr[ord(ch) - ord('a')] += 1
            dict_words[tuple(arr)].append(s)
        
        return list(dict_words.values())