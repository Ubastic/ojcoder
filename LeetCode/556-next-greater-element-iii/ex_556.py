class Solution(object):
    def nextGreaterElement(self, n):
        """
        :type n: int
        :rtype: int
        """
        s = list(str(n))
        i = len(s) - 1
        while i > 0:
            if s[i-1] < s[i]:
                break
            i -= 1
        if i == 0:  return -1
        p = i - 1
        i = len(s) - 1
        while i > p:
            if s[p] < s[i]:
                s[p], s[i] = s[i], s[p]
                break
            i -= 1
        right = sorted(s[p+1:])
        res = int(''.join(s[:p + 1]) + ''.join(right))
        return res if res <= 0x7fffffff else -1