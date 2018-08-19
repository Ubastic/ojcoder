class ValidWordAbbr(object):

    def __init__(self, dictionary):
        """
        :type dictionary: List[str]
        """
        self.lookup = {}
        for s in dictionary:
            if len(s) < 3:
                key = s
            else:
                key = s[0] + str(len(s) - 2) + s[-1]
            if key not in self.lookup:
                self.lookup[key] = set()
            self.lookup[key].add(s)
        

    def isUnique(self, word):
        """
        :type word: str
        :rtype: bool
        """
        if len(word) < 3:
            key = word
        else:
            key = word[0] + str(len(word) - 2) + word[-1]
        return key not in self.lookup or (word in self.lookup[key] and len(self.lookup[key]) == 1)


# Your ValidWordAbbr object will be instantiated and called as such:
# obj = ValidWordAbbr(dictionary)
# param_1 = obj.isUnique(word)