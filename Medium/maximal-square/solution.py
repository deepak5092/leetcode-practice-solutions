class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        
        rows = len(matrix)
        cols = len(matrix[0])
        res = 0
        dp = [0] * (cols + 1) 




        for r in range(rows):
            new_dp = [0] * (cols + 1) 
            for c in range(cols):
                if matrix[r][c] == "1":
                    new_dp[c + 1] = 1 + min(dp[c], dp[c + 1], new_dp[c])
                res = max(res, new_dp[c + 1])
            dp = new_dp

        return (res * res)