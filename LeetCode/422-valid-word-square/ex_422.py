class Solution(object):
    def validWordSquare(self, words):
        """
        :type words: List[str]
        :rtype: bool
        """
        for i in xrange(len(words)):
            for j in xrange(len(words[i])):
                if j >= len(words) or i >= len(words[j]) or words[i][j] != words[j][i]:
                    return False
        return True