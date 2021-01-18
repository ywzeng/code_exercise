class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        def is_valid(board: list, row: int, col: int):
            # Col
            for i in range(row):
                if board[i][col] == 'Q':
                    return False
            # Top left
            min_dis = min(row, col)
            for i in range(1, min_dis+1):
                if board[row-i][col-i] == 'Q':
                    return False
            # Top right
            min_dis = min(row, len(board)-col-1)
            for i in range(1, min_dis+1):
                if board[row-i][col+i] == 'Q':
                    return False
            return True

        def back_track(board: list, current_row: int, result_list: list) -> None:
            # Have proccessed the prior (N-1) rows, the last row now has only one valid position to set a Queue.
            if len(board) == current_row:
                temp_list = [''.join(temp_row) for temp_row in board]
                result_list += [temp_list]
                return
            
            # Verify whether the current col in appropriate place to set a Queue.
            for col in range(len(board)):
                if not is_valid(board, current_row, col):
                    continue
                board[current_row][col] = 'Q'
                back_track(board, current_row+1, result_list)
                board[current_row][col] = '.'       # Back track.

        board = [['.' for i in range(n)] for i in range(n)]
        result_list = []
        back_track(board, 0, result_list)
        return result_list

