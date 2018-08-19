class Solution(object):
    def minTotalDistance(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        rows = []
        cols = []
        for i in xrange(len(grid)):
            for j in xrange(len(grid[0])):
                if grid[i][j] == 1:
                    rows.append(i)
                    cols.append(j)
        rows.sort()
        cols.sort()
        x = rows[len(rows)/2]
        y = cols[len(cols)/2]
        res = 0
        for i in xrange(len(grid)):
            for j in xrange(len(grid[0])):
                if grid[i][j] == 1:
                    res += abs(i - x) + abs(j - y)
        return res