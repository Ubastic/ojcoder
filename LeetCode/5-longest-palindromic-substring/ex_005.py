class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        if not s:   return ''
        longest = s[0]
        for i in range(len(s)):
            temp = self.expand(s, i, i)
            if len(temp) > len(longest):
                longest = temp
            temp2 = self.expand(s, i, i + 1)
            if len(temp2) > len(longest):
                longest = temp2
        return longest

    def expand(self, s, start, end):
        while start >= 0 and end <= len(s) - 1 and s[start] == s[end]:
            start -= 1
            end += 1
        return s[start + 1: end]