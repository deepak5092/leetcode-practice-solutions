class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 0:
           return 1

        def recursion(div_min):
            if div_min == 1:
                return x
            mult = recursion(div_min // 2)
            return mult * mult if div_min % 2 == 0 else x * mult * mult
        
        res = recursion(abs(n))
        return res if n > 0 else (1/res)