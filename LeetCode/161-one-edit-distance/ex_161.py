class Solution(object):
    def isOneEditDistance(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        count = i = j = 0
        len_s = len(s)
        len_t = len(t)
        while i < len_s or j < len_t:
            if i == len_s:
                i -= 1
                count += 1
            elif j == len_t:
                j -= 1
                count += 1
            elif s[i] != t[j]:
                count += 1
                if len_s > len_t:
                    j -= 1
                elif len_s < len_t:
                    i -= 1
            i += 1
            j += 1
        return count == 1
        