class Solution_stupid:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        from collections import Counter
        # Scan rows.
        for row in board:
            row_map = Counter(row)
            if '.' in row_map and len(row_map)+row_map['.'] < 10:
                return False
            elif '.' not in row_map and len(row_map) < 9:
                return False
        # Scan cols.
        for i in range(9):     # Col index.
            col_map = Counter()
            for j in range(9):     # Row index.
                col_map[board[j][i]] += 1
            if '.' in col_map and len(col_map)+col_map['.'] < 10:
                return False
            elif '.' not in col_map and len(col_map) < 9:
                return False
        # Scan sub-squares. [i][j] indicates the top-left point of each sub-squares.
        for i in range(0, 7, 3):
            for j in range(0, 7, 3):
                subsquare_map = Counter()
                for sub_i in range(3):
                    for sub_j in range(3):
                        subsquare_map[board[i+sub_i][j+sub_j]] += 1
                if '.' in subsquare_map and len(subsquare_map)+subsquare_map['.'] < 10:
                    return False
                elif '.' not in subsquare_map and len(subsquare_map) < 9:
                    return False
        return True
