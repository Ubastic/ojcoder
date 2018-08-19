class Solution(object):
    def checkRecord(self, s):
        """
        :type s: str
        :rtype: bool
        """
        a = 0
        for i in range(len(s)):
            if s[i] == 'A':
                a += 1
                if a > 1:
                    return False
            if s[i] == 'L':
                j = i
                count = 0
                while s[j] == 'L' and j >= 0:
                    count += 1
                    j -= 1
                if count > 2:
                    return False
        return True