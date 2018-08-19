class Solution(object):
    def splitLoopedString(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        strs = map(lambda x: max(x, x[::-1]), strs)
        max_c = max(''.join(strs))
        res = None
        for i in range(len(strs)):
            if max_c in strs[i]:
                for s in [strs[i], strs[i][::-1]]:
                    for j in range(len(s)):
                        if s[j] == max_c:
                            temp = s[j:] + ''.join(strs[i+1:]) + ''.join(strs[:i]) + s[:j]
                            res = max(res, temp)
        return res