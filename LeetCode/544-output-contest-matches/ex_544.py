class Solution(object):
    def findContestMatch(self, n):
        """
        :type n: int
        :rtype: str
        """
        res = map(str, range(1, n+1))
        k = 1
        while k != n:
            i = 0
            j = len(res) - 1
            temp = []
            while i < j:
                temp.append('(' + res[i] + ',' + res[j] + ')')
                i += 1
                j -= 1
            res = temp
            k *= 2
        return res[0]
            