class Solution(object):
    def findLongestWord(self, s, d):
        """
        :type s: str
        :type d: List[str]
        :rtype: str
        """
        word = ""
        length = len(s)
        for w in d:
            i = j = 0
            while j <= length:
                if i == len(w):
                    if len(word) < len(w):
                        word = w
                    elif len(word) == len(w):
                        word = min(word, w)
                    break
                if j == length: break
                if w[i] == s[j]:
                    i += 1
                j += 1
        return word