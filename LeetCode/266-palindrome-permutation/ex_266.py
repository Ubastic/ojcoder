class Solution(object):
    def canPermutePalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        myset = set()
        for c in s:
            if c in myset:
                myset.remove(c)
            else:
                myset.add(c)
        return len(myset) < 2