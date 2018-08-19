class Solution(object):
    def findMaxForm(self, strs, m, n):
        """
        :type strs: List[str]
        :type m: int
        :type n: int
        :rtype: int
        """
        if not strs or not (m or n):    return 0
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        strs = map(self.countStr, strs)
        for z, o in strs:
            for i in reversed(range(z, m+1)):
                for j in reversed(range(o, n+1)):
                    dp[i][j] = max(dp[i-z][j-o] + 1, dp[i][j])
        return dp[-1][-1]
        
    def countStr(self, s):
        z, o = 0, 0
        for c in s:
            if c == '0':
                z += 1
            else:
                o += 1
        return (z, o)