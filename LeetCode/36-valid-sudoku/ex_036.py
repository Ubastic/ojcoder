class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        def is_duplicated(board, outer_start, outer_end, inner_start, inner_end):
            table = set()
            for i in range(outer_start, outer_end):
                for j in range(inner_start, inner_end):
                    if board[i][j] == '.':
                        pass
                    elif board[i][j] not in table:
                        table.add(board[i][j])
                    else:
                        return True
            return False
        for i in range(9):
            if is_duplicated(board, i, i+1, 0, 9):
                return False
        for i in range(9):
            if is_duplicated(board, 0, 9, i, i+1):
                return False
        for i in range(3):
            for j in range(3):
                row = i * 3
                col = j * 3
                if is_duplicated(board, row, row + 3, col, col +3):
                    return False
        return True
            