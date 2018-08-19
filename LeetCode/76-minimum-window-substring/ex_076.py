class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        i = I = J = 0
        need = collections.Counter(t)
        missing = len(t)
        for j, c in enumerate(s, 1):
            if need[c] > 0:
                missing -= 1
            need[c] -= 1    # if c is not in need, insert c as key with value of -1
            if not missing:
                while i < j and need[s[i]] < 0:
                    need[s[i]] += 1
                    i += 1
                if not J or J - I > j - i:
                    J, I = j, i
        return s[I:J]