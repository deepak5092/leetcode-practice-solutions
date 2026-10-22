class Solution:
    def isValidSudoku(self, board: list[list[str]]) -> bool:
        
        dict_rows = defaultdict(set)
        dict_cols = defaultdict(set)
        dict_boxes = defaultdict(set)
        rows = len(board)
        cols = len(board[0])

        for r in range(rows):
            for c in range(cols):
                cur = board[r][c]
                if cur == ".":
                    continue
                if cur in dict_rows[r] or cur in dict_cols[c] or cur in dict_boxes[(r//3, c//3)]:
                    return False
                dict_rows[r].add(cur)
                dict_cols[c].add(cur)
                dict_boxes[(r//3,c//3)].add(cur)
        
        return True 