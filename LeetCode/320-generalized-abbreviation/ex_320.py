class Solution(object):
    def generateAbbreviations(self, word):
        """
        :type word: str
        :rtype: List[str]
        """
        res = []
        self.helper(res, '', word, True)
        return res
        
    def helper(self, res, pre, word, use_number):
        if not word:
            res.append(pre)    
            return
        self.helper(res, pre + word[0], word[1:], True)
        if use_number:
            for i in xrange(len(word)):
                self.helper(res, pre + str(i+1), word[i+1:], False)
                