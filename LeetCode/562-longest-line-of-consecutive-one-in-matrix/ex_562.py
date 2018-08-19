class Solution(object):
    def longestLine(self, M):
        """
        :type M: List[List[int]]
        :rtype: int
        """
        if not M:   return 0
        res = 0
        mem = [[[0,0,0,0] if i == 0 else [1,1,1,1] for i in row] for row in M]
        # [h, v, d, ad]
        for i in range(len(M)):
            for j in range(len(M[0])):
                if M[i][j] == 1:
                    mem[i][j][0] += mem[i][j-1][0] if j > 0 else 0
                    mem[i][j][1] += mem[i-1][j][1] if i > 0 else 0
                    mem[i][j][2] += mem[i-1][j-1][2] if i > 0 and j > 0 else 0
                    mem[i][j][3] += mem[i-1][j+1][3] if i > 0 and j < len(M[0]) - 1 else 0
                    res = max(res, max(mem[i][j]))
        return res