class Solution(object):
    def checkInclusion(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        if len(s1) > len(s2):   return False
        need = [0] * 26
        window = [0] * 26
        n = len(s1)
        for i in range(n):
            need[ord(s1[i]) - ord('a')] += 1
            window[ord(s2[i]) - ord('a')] += 1
        if need == window:  return True
        for i in range(n, len(s2)):
            window[ord(s2[i]) - ord('a')] += 1
            window[ord(s2[i-n]) - ord('a')] -= 1
            if need == window:  return True
        return False
        