class Solution(object):
    def updateMatrix(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[List[int]]
        """
        if not matrix or not matrix[0]: return
        res = [[0] * len(matrix[0]) for _ in range(len(matrix))]
        m, n = len(matrix), len(matrix[0])
        s = m * n
        for i in range(m):
            for j in range(n):
                if matrix[i][j]:
                    up = res[i-1][j] if i > 0 else s
                    left = res[i][j-1] if j > 0 else s
                    res[i][j] = min(up, left) + 1
        for i in range(m-1, -1, -1):
            for j in range(n-1, -1, -1):
                if matrix[i][j]:
                    down = res[i+1][j] if i < m - 1 else s
                    right = res[i][j+1] if j < n - 1 else s
                    res[i][j] = min(min(down, right) + 1, res[i][j])
        return res