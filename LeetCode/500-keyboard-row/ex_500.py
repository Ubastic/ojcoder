class Solution(object):
    def findWords(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        res = []
        rows = [set('qwertyuiop'), set('asdfghjkl'), set('zxcvbnm')]
        for w in words:
            lw = w.lower()
            for row in rows:
                in_row = True
                for c in lw:
                    if c not in row:
                        in_row = False
                if in_row:
                    res.append(w)
                    break
        return res
        