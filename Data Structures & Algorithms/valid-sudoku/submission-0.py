class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        rows = defaultdict(set)
        cols = defaultdict(set)
        squares = defaultdict(set)

        for row in range(9):
            for col in range(9):
                num = board[row][col]
                if num == ".":
                    continue
                #To uniquely identify this square, perform floor division which rounds down quotient.
                #For example, if moved onto the 3rd row and 5th column, 3//3 = 1, 5//3 = 1, so in 1st quare (not 0th square)
                if num in rows[row] or num in cols[col] or num in squares[row // 3, col // 3]:
                    return False
                else:
                    rows[row].add(board[row][col])
                    cols[col].add(board[row][col])
                    squares[row // 3, col // 3].add(board[row][col])


        return True
