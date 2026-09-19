class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        
        dict_words = defaultdict(list)

        for st in strs:
            arr = [0] * 26
            for s in st:
                arr[ord(s) - ord('a')] += 1
            dict_words[tuple(arr)].append(st)
        
        return list(dict_words.values())