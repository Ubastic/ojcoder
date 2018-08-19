class Solution(object):
    def wallsAndGates(self, rooms):
        """
        :type rooms: List[List[int]]
        :rtype: void Do not return anything, modify rooms in-place instead.
        """
        if not rooms:   return
        for row in xrange(len(rooms)):
            for col in xrange(len(rooms[0])):
                if rooms[row][col] == 0:
                    self.dfs(rooms, row, col, 0)
    
    def dfs(self, rooms, row, col, distance):
        rooms[row][col] = min(distance, rooms[row][col])
        shift = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        for i, j in shift:
            next_row = row + i
            next_col = col + j
            if 0 <= next_row < len(rooms) and 0 <= next_col < len(rooms[0]) and rooms[next_row][next_col] > rooms[row][col]:
                self.dfs(rooms, next_row, next_col, distance + 1)