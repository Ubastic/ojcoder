class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        maxlength = 0
        start = 0
        table = {}
        for i in range(len(s)):
            if s[i] in table and start <= table[s[i]]:
                start = table[s[i]] + 1
            else:
                maxlength = max(maxlength, i - start + 1)
            table[s[i]] = i
        return maxlength