class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        def get_dict_chars(st):
            dict_chars = defaultdict(int)
            for ch in st:
                dict_chars[ch] += 1
            return dict_chars

        return get_dict_chars(s) == get_dict_chars(t)