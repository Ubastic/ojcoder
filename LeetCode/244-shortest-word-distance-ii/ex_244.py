class WordDistance(object):
    def __init__(self, words):
        """
        initialize your data structure here.
        :type words: List[str]
        """
        self.word_dict = {}
        for idx, w in enumerate(words):
            self.word_dict[w] = self.word_dict.get(w, []) + [idx]

    def shortest(self, word1, word2):
        """
        Adds a word into the data structure.
        :type word1: str
        :type word2: str
        :rtype: int
        """
        return min(abs(i - j) for i in self.word_dict[word1] for j in self.word_dict[word2])


# Your WordDistance object will be instantiated and called as such:
# wordDistance = WordDistance(words)
# wordDistance.shortest("word1", "word2")
# wordDistance.shortest("anotherWord1", "anotherWord2")