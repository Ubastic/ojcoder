class Solution(object):
    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: int
        """
        wordSet = set(wordList)
        queue = collections.deque([[beginWord, 1]])
        while queue:
            word, length = queue.popleft()
            if word == endWord:
                return length
            for i in range(len(word)):
                for c in 'qwertyuiopasdfghjklzxcvbnm':
                    next_word = word[:i] + c + word[i+1:]
                    if next_word in wordSet:
                        wordSet.remove(next_word)
                        queue.append([next_word, length+1])
        return 0