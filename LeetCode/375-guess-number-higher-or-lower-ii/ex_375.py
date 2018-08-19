class Solution(object):
    def getMoneyAmount(self, n):
        """
        :type n: int
        :rtype: int
        """
        dp = [[0] * (n+1) for _ in range(n+1)]
        for lo in range(n, 0, -1):
            for hi in range(lo+1, n+1):
                dp[lo][hi] = sys.maxsize
                for x in range(lo, hi):
                    dp[lo][hi] = min(dp[lo][hi], x + max(dp[lo][x-1], dp[x+1][hi]))
        return dp[1][n]