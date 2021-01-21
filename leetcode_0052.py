class Solution_clever:
    def totalNQueens(self, n: int) -> int:
        """
        We need three sets to store the conflicted index:
        (1). Column; (2). Top-left diagonal; (3). Top-right diagonal.
        For the first case, column, the two column-conflicted Queens have the same column index.
        For the second case, top-left diagonal, two Queens [row][col] and [row-i][col-i] have the same difference of row index and col index. Namely, row-col == (row-i)-(col-i).
        For the third case, top-right diagonal, two Queens [row][col] and [row-i][col+i] have the same summation of row index and col index. Namely row+col == (row-i)+(col+i).
        We only need to store the above three types of conflict-info.
        Additionally, the top-left (top-right) diagonal of current Queen is the bottom-right (bottom-left) diagonal of the prior conflicted Queen.
        """
        def back_track(n: int, row: int, col_set: set, top_left_set: set, top_right_set: set, distinct_plan: int) -> int:
            """
            'row' is the row index of current Queen.
            'col_set' is the conflicted Queens of current Queen in its conlumn.
            'top_left_set' is the conflicted Queens of current Queen in its top-left diagonal.
            'top_right_set' is the conflicted Queens of current Queen in its top-right diagonal.
            """
            if row == n:
                return distinct_plan + 1
            # Scan the col index of current row from left to right.
            for col in range(n):
                if col in col_set or (row-col) in top_left_set or (row+col) in top_right_set:
                    continue
                col_set.add(col)
                top_left_set.add(row-col)
                top_right_set.add(row+col)
                distinct_plan = back_track(n, row+1, col_set, top_left_set, top_right_set, distinct_plan)
                col_set.remove(col)
                top_left_set.remove(row-col)
                top_right_set.remove(row+col)
            return distinct_plan

        col_set = set()
        bottom_right_set = set()     # Actually, it is used to verify the conflicted Queens in the top-left diagonal of current Queen.
        bottom_left_set = set()        # Actually, it is used to verify the conflicted Queens in the top-right diagonal of current Queen.
        distinct_plan = 0

        return back_track(n, 0, col_set, bottom_right_set, bottom_left_set, distinct_plan)


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
