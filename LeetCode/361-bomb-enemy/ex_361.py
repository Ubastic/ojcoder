class Solution(object):
    def maxKilledEnemies(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        if not grid or not grid[0]: return 0
        res = 0
        row_hits = 0
        col_hits = [0] * len(grid[0])
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if not j or grid[i][j-1] == 'W':
                    row_hits = 0
                    k = j
                    while k < len(grid[0]) and grid[i][k] != 'W':
                        row_hits += int(grid[i][k] == 'E')
                        k += 1
                if not i or grid[i-1][j] == 'W':
                    col_hits[j] = 0
                    k = i
                    while k < len(grid) and grid[k][j] != 'W':
                        col_hits[j] += int(grid[k][j] == 'E')
                        k += 1
                if grid[i][j] == '0':
                    res = max(res, row_hits + col_hits[j])
        return res