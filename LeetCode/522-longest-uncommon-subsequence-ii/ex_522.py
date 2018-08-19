class Solution(object):
    def findLUSlength(self, strs):
        """
        :type strs: List[str]
        :rtype: int
        """
        counter = collections.Counter(strs)
        res = -1
        for k in counter:
            if counter[k] == 1:
                count = 0
                for s in strs:
                    if self.isSubsequence(k, s):
                        count += 1
                if count == 1:
                    res = max(res, len(k))
        return res
        
    def isSubsequence(self, s, t):
        len_s = len(s)
        len_t = len(t)
        i = j = 0
        while i < len_s and j < len_t:
            if s[i] == t[j]: i += 1
            j += 1
        return len_s == i