class Solution(object):
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        if not p or not s:  return []
        
        res = []
        table = collections.Counter(p)
        missing = len(p)
        i = j = 0
        
        while j < len(s):
            if table[s[j]]:   missing -= 1
            table[s[j]] -= 1
            j += 1
            if not missing:     res.append(i)
            if j - i == len(p):
                if table[s[i]] >= 0:  missing += 1
                table[s[i]] += 1
                i += 1
        return res