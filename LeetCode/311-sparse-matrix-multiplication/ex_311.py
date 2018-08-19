class Solution(object):
    def multiply(self, A, B):
        """
        :type A: List[List[int]]
        :type B: List[List[int]]
        :rtype: List[List[int]]
        """
        row = len(A)
        col = len(B[0])
        res = [[0 for i in xrange(col)] for j in xrange(row)]
        for i in xrange(row):
            for j in xrange(len(A[0])):
                if (A[i][j] != 0):
                    for k in range(col):
                        res[i][k] += A[i][j] * B[j][k]
        return res
        