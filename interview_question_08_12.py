class Solution:
    def __init__(self):
        self.result_list = []

    def solveNQueens(self, n: int) -> List[List[str]]:
        board = [['.' for i in range(n)] for i in range(n)]
        self.back_track(board, 0)       # Start with the first row.
        return self.result_list

    def is_valid(self, board, row, col):
        """
        Check whether the target place, board[row][col] is approciate to set a QUEEN.
        """
        # The same column.
        for i in range(row):
            if board[i][col] == 'Q':
                return False
        # The upper-left diagonal.
        for i in range(0, min(row, col)):
            if board[row-i-1][col-i-1] == 'Q':
                return False
        # The upper-right diagonal.
        for i in range(0, min(row, len(board)-col-1)):
            if board[row-i-1][col+i+1] == 'Q':
                return False
        return True
        
    def back_track(self, board: list, row: int) -> None:
        """
        board is the current board, row is the current processed row.
        """
        if row == len(board):
            temp_board = [''.join(temp_row) for temp_row in board]
            self.result_list += [temp_board]
            return
        
        for col in range(len(board)):
            if not self.is_valid(board, row, col):
                continue
            board[row][col] = 'Q'
            self.back_track(board, row+1)
            board[row][col] = '.'
