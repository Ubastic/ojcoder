class Solution(object):
    def findStrobogrammatic(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        table = {'0':'0', '1':'1','6':'9', '8':'8', '9':'6'}
        half = (n + 1) / 2 
        res = []
        self.helper(n, half, table, res, 0, '')
        return res
        
    def helper(self, n, half, table, res, i, prev):
        if i == half:
            ret = prev
            i = half - 1
            if half != n / 2:
                if prev[-1] in '69':
                    return
                i -= 1
            while i >= 0:
                ret += table[prev[i]]
                i -= 1
            res.append(ret)
            return
        for k in table:
            if i != 0 or k != '0' or n == 1:
                self.helper(n, half, table, res, i + 1, prev + k)