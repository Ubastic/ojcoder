class Solution(object):
    def countBattleships(self, board):
        """
        :type board: List[List[str]]
        :rtype: int
        """
        def has_battleship(x, y):
            if x < 0 or y < 0:  return False
            return board[x][y] == 'X'
        
        def should_count(x, y):
            return has_battleship(x, y) and not has_battleship(x, y - 1) and not has_battleship(x - 1, y)
        
        count = 0
        for x in xrange(len(board)):
            for y in xrange(len(board[0])):
                if should_count(x, y):  count += 1
        return count
        