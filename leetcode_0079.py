class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        def back_track(board: list, visited: list, row: int, col: int, word: str, char_index: int) -> bool:
            """
            Four directions:
                1. up: [row-1][col];
                2. right: [row][col+1];
                3. down: [row+1][col];
                4. left: [row][col-1].
            """
            if char_index == len(word)-1:
                return board[row][col] == word[char_index]

            if board[row][col] == word[char_index]:
                visited[row][col] = True
                # Four directions: up, right, down, left.
                direction_list = [(-1, 0), (0, 1), (1, 0), (0, -1)]
                for direction in direction_list:
                    next_row, next_col = row + direction[0], col + direction[1]
                    if 0 <= next_row < len(board) and 0 <= next_col < len(board[row]):
                        # Only choose the unvisited directions.
                        if not visited[next_row][next_col]:
                            if back_track(board, visited, next_row, next_col, word, char_index+1):
                                return True
                visited[row][col] = False
            return False
        
        visited = [[False for i in range(len(board[0]))] for i in range(len(board))]
        # Search the target word from head to tail.
        for i in range(len(board)):
            for j in range(len(board[i])):
                if back_track(board, visited, i, j, word, 0):
                    return True
        return False
