class Solution(object):
    _memo = {}
    def canWin(self, s):
        """
        :type s: str
        :rtype: bool
        """
        memo = self._memo
        if s not in memo:
            return any(s[i:i+2] == '++' and not self.canWin(s[:i] + '-' + s[i+2:]) for i in range(len(s)))
        return memo[s]