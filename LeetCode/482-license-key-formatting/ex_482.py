class Solution(object):
    def licenseKeyFormatting(self, S, K):
        """
        :type S: str
        :type K: int
        :rtype: str
        """
        newS = S.upper().replace('-', '')
        res = []
        i = len(newS) % K
        if i > 0:
            res.append(newS[0:len(newS) %K])
        while i < len(newS):
            res.append(newS[i: i + K])
            i += K
        return '-'.join(res)