class Solution_stupid:
    def totalNQueens(self, n: int) -> int:
        def is_valid(board: list, row: int, col: int) -> bool:
            """ The argument 'row' and 'col' represent the target index of the new Queen. """
            # Same column.
            for i in range(row):
                if board[i][col] == 'Q':
                    return False
            # Same top-left diagonal.
            for i in range(0, min(row, col)):
                if board[row-i-1][col-i-1] == 'Q':
                    return False
            # Same top-right diagonal.
            for i in range(0, min(row, len(board)-col-1)):
                if board[row-i-1][col+i+1] == 'Q':
                    return False
            return True

        def back_track(board: list, row: int, result_num: int) -> None:
            if row == len(board):
                result_num += 1
                return result_num
            
            for col in range(len(board[row])):
                if not is_valid(board, row, col):
                    continue
                
                board[row][col] = 'Q'
                result_num = back_track(board, row+1, result_num)
                board[row][col] = '.'
            return result_num
        
        board = [['.' for i in range(n)] for i in range(n)]
        result_num = back_track(board, 0, 0)
        return result_num
