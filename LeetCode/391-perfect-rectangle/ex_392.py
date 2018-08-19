class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        len_s = len(s)
        len_t = len(t)
        i = j = 0
        while i < len_s and j < len_t:
            if s[i] == t[j]: i += 1
            j += 1
        return len_s == i