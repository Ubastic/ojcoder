class Solution(object):
    def findPermutation(self, s):
        """
        :type s: str
        :rtype: List[int]
        """
        if not s:   return []
        res = []
        i = 1
        for c in s:
            if c == 'I':
                res.extend(range(i, len(res), -1))
            i += 1
        res.extend(range(i, len(res), -1))
        return res