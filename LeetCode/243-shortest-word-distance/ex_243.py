class Solution(object):
    def shortestDistance(self, words, word1, word2):
        """
        :type words: List[str]
        :type word1: str
        :type word2: str
        :rtype: int
        """
        p1 = -1
        p2 = -1
        distance = sys.maxsize
        for i in xrange(len(words)):
            if word1 == words[i]:
                p1 = i
            if word2 == words[i]:
                p2 = i
            if p1 != -1 and p2 != -1:
                distance = min(distance, abs(p1 - p2))
        return distance
        