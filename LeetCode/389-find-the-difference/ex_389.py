class Solution(object):
    def findTheDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        table = {}
        for c in s:
            if c not in table:
                table[c] = 0
            table[c] += 1
        for c in t:
            if c not in table or table[c] == 0:
                return c
            else:
                table[c] -= 1