class Solution(object):
    def islandPerimeter(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        if not grid:    return 0
        count = 0
        for x in range(len(grid)):
            for y in range(len(grid[0])):
                count += grid[x][y] * 4
                if grid[x][y] == 1:
                    count -= self.adjacent(grid, x, y)
        return count
    
    def adjacent(self, grid, x, y):
        offset = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        count = 0
        for i, j in offset:
            nx, ny = x + i, y + j
            if 0 <= nx < len(grid) and 0 <= ny < len(grid[0]) and grid[nx][ny] == 1:
                count += 1
        return count