class TicTacToe(object):

    def __init__(self, n):
        """
        Initialize your data structure here.
        :type n: int
        """
        self.board = [[0 for i in xrange(n)] for j in xrange(n)]
        self.n = n

    def move(self, row, col, player):
        """
        Player {player} makes a move at ({row}, {col}).
        @param row The row of the board.
        @param col The column of the board.
        @param player The player, can be either 1 or 2.
        @return The current winning condition, can be either:
                0: No one wins.
                1: Player 1 wins.
                2: Player 2 wins.
        :type row: int
        :type col: int
        :type player: int
        :rtype: int
        """
        self.board[row][col] = player
        r = c = d = rd = 0
        for i in range(self.n):
            if self.board[row][i] == player:        c += 1
            if self.board[i][col] == player:        r += 1
            if self.board[i][i] == player:          d += 1
            if self.board[i][self.n-i-1] == player: rd += 1
        if r == self.n or c == self.n or d == self.n or rd == self.n:
            return player
        return 0

# Your TicTacToe object will be instantiated and called as such:
# obj = TicTacToe(n)
# param_1 = obj.move(row,col,player)