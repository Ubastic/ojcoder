offsets = [[0, 1], [1, 0], [0, -1], [-1, 0]]

class Solution(object):
    def hasPath(self, maze, start, destination):
        """
        :type maze: List[List[int]]
        :type start: List[int]
        :type destination: List[int]
        :rtype: bool
        """
        visited = set()
        return self.dfs(maze, destination, start, visited)
        
    def dfs(self, maze, destination, curr, visited):
        if tuple(curr) in visited: return False
        visited.add(tuple(curr))
        if curr == destination:
            return True
        x, y = curr
        for i , j in offsets:
            if not self.valid_move(maze, x + i, y + j):   continue
            coords = self.move(maze, [i, j], x, y)
            if self.dfs(maze, destination, coords, visited):   return True
        return False
        
    def valid_move(self, maze, x, y):
        if x < 0 or x >= len(maze) or y < 0 or y >= len(maze[0]) or maze[x][y] == 1:   return False
        return True
        
    def move(self, maze, direction, x, y):
        while self.valid_move(maze, x + direction[0], y + direction[1]):
            x += direction[0]
            y += direction[1]
        return [x, y]