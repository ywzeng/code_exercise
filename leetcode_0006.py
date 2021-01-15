class Solution_better:
    def convert(self, s: str, numRows: int) -> str:
        """
        Leverage the step interval between the characters in one rwo in the zigzag scanning.
        """
        if numRows == 1:
            return s
        index = 0       # save the index of the character in 's'
        step = numRows * 2 - 2
        add = 0
        result_str = ''
        for row in range(numRows):
            index = row
            add = row * 2
            while index < len(s):
                result_str += s[index]
                add = step - add
                index += step if (row == 0 or row == numRows-1) else add
        return result_str


class Solution_stupid:
    def convert(self, s: str, numRows: int) -> str:
        """
        Zig-zag scanning the given string.
        Put the characters into the right position, and then scan the 2-D list.
        """
        if numRows == 1:
            return s
        result_list = [['' for i in range(len(s)//2+1)] for j in range(min(numRows, len(s)))]
        row, col = 0, 0     # indicate the current coordinate.
        is_down = True      # two state: True -> down, False -> upper-right.
        for c in s:
            result_list[row][col] = c
            if row == numRows-1:
                is_down = False
            if row == 0:
                is_down = True
            if is_down:
                row += 1
            else:
                row -= 1
                col += 1
        return ''.join([''.join(temp_row) for temp_row in result_list])
