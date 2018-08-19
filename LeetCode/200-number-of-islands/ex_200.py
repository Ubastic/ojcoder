class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        def dfs(x, y):
            if x < 0 or y < 0 or x >= len(grid) or y >= len(grid[0]) or grid[x][y] != '1':   return
            grid[x][y] = '0'
            for i in range(4):
                dfs(x + shift[i][0], y + shift[i][1])
        
        if not grid or not grid[0]: return 0
        count = 0
        shift = [[1,0],[0,1],[-1,0],[0,-1]]
        for x in range(len(grid)):
            for y in range(len(grid[0])):
                if grid[x][y] == '1':
                    dfs(x,y)
                    count += 1
        return count