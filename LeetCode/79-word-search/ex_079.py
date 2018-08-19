class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        def dfs(x, y, i):
            if i == len(word):  return True
            if x < 0 or y < 0 or x >= len(board) or y >= len(board[0]) or visited[x][y] or board[x][y] != word[i]: return False
            visited[x][y] = True
            for m, n in zip([1,-1,0,0],[0,0,-1,1]):
                if dfs(x+m, y+n, i+1):  return True
            visited[x][y] = False
            return False
        if not board:
            return False
        visited = [[False] * len(board[0]) for i in board]
        for x in range(len(board)):
            for y in range(len(board[0])):
                if dfs(x, y, 0):
                    return True
        return False