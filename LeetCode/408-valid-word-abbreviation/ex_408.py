class Solution(object):
    def validWordAbbreviation(self, word, abbr):
        """
        :type word: str
        :type abbr: str
        :rtype: bool
        """
        i = 0
        j = 0
        num = 0
        while i < len(word) and j < len(abbr):
            if abbr[j] in '0123456789':
                if num == 0 and abbr[j] == '0': return False
                num = num * 10 + int(abbr[j])
                j += 1
            elif num > 0:
                i += num
                num = 0
            elif word[i] != abbr[j]:
                return False
            else:
                i += 1
                j += 1
        return i + num == len(word) and j == len(abbr)