class Solution(object):
    def findDiagonalOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        res = []
        if not matrix or not matrix[0]: return res
        m = len(matrix)
        n = len(matrix[0])
        flip = False
        for i in range(n + m - 1):
            level = []
            z1 = 0 if i < n else i - n + 1
            z2 = 0 if i < m else i - m + 1
            j = i - z2
            while j >= z1:
                level.append(matrix[j][i - j])
                j -= 1
            if flip:
                res.extend(reversed(level))
            else:
                res.extend(level)
            flip = not flip
        return res