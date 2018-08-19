class Solution(object):
    def findBlackPixel(self, picture, N):
        """
        :type picture: List[List[str]]
        :type N: int
        :rtype: int
        """
        if not picture or not picture[0]:   return 0
        row = [i for i in range(len(picture)) if picture[i].count('B') == N]
        col = [i for i in range(len(picture[0])) if [j[i] for j in picture].count('B') == N]
        count = 0
        for r in row:
            for c in col:
                if picture[r][c] == 'B':
                    sub = filter(lambda x: x[c] == 'B', picture)
                    if all(s == picture[r] for s in sub):
                        count += 1
        return count