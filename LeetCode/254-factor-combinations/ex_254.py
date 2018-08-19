class Solution(object):
    def getFactors(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        res = []
        self.dfs(res, [], n, 2)
        return res
        
    def dfs(self, res, prev, n, start):
        if prev:
            res.append(prev + [n])
        for i in range(start, int(n**0.5)+1):
            if n % i == 0:
                self.dfs(res, prev + [i], n / i, i)