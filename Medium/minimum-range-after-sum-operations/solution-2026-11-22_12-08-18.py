class Solution:
    def minRange(self, a: int, b: int, c: int) -> int:

        res = [a, b, c]
        res.sort()
        return min(res[2] - res[0], res[2], res[1])