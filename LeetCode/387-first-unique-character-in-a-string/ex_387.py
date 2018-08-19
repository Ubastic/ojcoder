class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        alphabet = [0] * 26
        for c in s:
            alphabet[ord(c) - ord('a')] += 1
        length = len(s)
        i = 0
        while i < length and alphabet[ord(s[i]) - ord('a')] > 1:
            i += 1
        return -1 if i == length else i