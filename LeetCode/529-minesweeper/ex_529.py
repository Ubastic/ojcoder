class Solution(object):
    def updateBoard(self, board, click):
        """
        :type board: List[List[str]]
        :type click: List[int]
        :rtype: List[List[str]]
        """
        if board[click[0]][click[1]] == 'M':
            board[click[0]][click[1]] = 'X'
        else:
            self.dfs(board, click[0], click[1])
        return board
    
    def dfs(self, board, x, y):
        if x >= len(board) or y >= len(board[0]) or x < 0 or y < 0:
            return
        mine_count = self.count_adjacent(board, x, y)
        if mine_count:
            board[x][y] = str(mine_count)
        else:
            board[x][y] = 'B'
            offset = [-1, 0, 1]
            for i in offset:
                for j in offset:
                    if self.valid_move(board, x, y, i, j) and board[x + i][y + j] == 'E':
                        self.dfs(board, x + i, y + j)
                        
    def count_adjacent(self, board, x, y):
        offset = [-1, 0, 1]
        count = 0
        for i in offset:
            for j in offset:
                if self.valid_move(board, x, y, i, j) and board[x + i][y + j] == 'M':
                    count += 1
        return count
        
    def valid_move(self, board, x, y, i, j):
        return not (i == 0 and j == 0) and 0 <= x + i < len(board) and 0 <= y + j < len(board[0])