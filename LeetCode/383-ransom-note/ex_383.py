class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        dic = {}
        for c in magazine:
            if c in dic:
                dic[c] += 1
            else:
                dic[c] = 1
        for c in ransomNote:
            if c in dic and dic[c] >= 1:
                dic[c] -= 1
            else:
                return False
        return True