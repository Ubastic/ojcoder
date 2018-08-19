class Solution(object):
    def shortestWordDistance(self, words, word1, word2):
        """
        :type words: List[str]
        :type word1: str
        :type word2: str
        :rtype: int
        """
        res = sys.maxsize
        i1 = res
        i2 = -res
        same_word = (word1 == word2)
        for i in xrange(len(words)):
            if words[i] == word1:
                i1 = i
                if same_word:    i1, i2 = i2, i1
            elif words[i] == word2:
                i2 = i
            res = min(res, abs(i1 - i2))
        return res