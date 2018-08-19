class Solution(object):
    def findLongestWord(self, s, d):
        """
        :type s: str
        :type d: List[str]
        :rtype: str
        """
        def isSub(x):
            it = iter(s)
            return all(c in it for c in x)
        return max(sorted(filter(isSub, d) + ['']), key=len)