class Solution(object):
    def reverseStr(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        res = []
        r = True
        for i in range(0, len(s), k):
            sub = s[i: i + k]
            if r:   sub = sub[::-1]
            res.append(sub)
            r = not r
        return ''.join(res)