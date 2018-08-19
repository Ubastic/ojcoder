class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """
        cnt = collections.Counter(s)
        length = 0
        odd = False
        for k in cnt:
            if cnt[k] % 2:
                length += cnt[k] - 1
                odd = True
            else:
                length += cnt[k]
        return length + 1 if odd else length