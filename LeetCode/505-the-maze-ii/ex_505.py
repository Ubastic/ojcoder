class Solution(object):
    def shortestDistance(self, maze, start, destination):
        """
        :type maze: List[List[int]]
        :type start: List[int]
        :type destination: List[int]
        :rtype: int
        """
        destination = tuple(destination)
        visited = {}
        q = []
        res = None
        heapq.heappush(q, (0, tuple(start)))
        while q:
            moves, curr = heapq.heappop(q)
            if curr in visited and visited[curr] <= moves:  continue
            visited[curr] = moves
            if curr == destination:
                res = min(res, moves) if res else moves
            for i , j in [[0, 1], [1, 0], [0, -1], [-1, 0]]:
                if not self.valid_move(maze, curr[0] + i, curr[1] + j):   
                    continue
                new_moves, coords = self.move(maze, [i, j], curr[0], curr[1])
                heapq.heappush(q, (moves + new_moves, coords))
        return res if res else -1
        
    def valid_move(self, maze, x, y):
        if x < 0 or x >= len(maze) or y < 0 or y >= len(maze[0]) or maze[x][y] == 1:   return False
        return True
        
    def move(self, maze, direction, x, y):
        step = 0
        while self.valid_move(maze, x + direction[0], y + direction[1]):
            x += direction[0]
            y += direction[1]
            step += 1
        return step, (x, y)