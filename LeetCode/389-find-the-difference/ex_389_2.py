class Solution(object):
    def findTheDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        if not s:   return t
        res = ord(s[0])
        for i in range(1, len(s)):
            res ^= ord(s[i])
        for i in range(len(t)):
            res ^= ord(t[i])
        return chr(res)