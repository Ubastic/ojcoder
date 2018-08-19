class Solution(object):
    def repeatedSubstringPattern(self, s):
        """
        :type str: str
        :rtype: bool
        """
        return s in (s * 2)[1: -1]