class Solution(object):
    def findLonelyPixel(self, picture):
        """
        :type picture: List[List[str]]
        :rtype: int
        """
        if not picture or not picture[0]:   return 0
        row = [0] * len(picture)
        col = [0] * len(picture[0])
        for i in range(len(picture)):
            for j in range(len(picture[0])):
                if picture[i][j] == 'B':
                    row[i] += 1
                    col[j] += 1
        count = 0
        for i in range(len(picture)):
            if row[i] != 1: continue
            for j in range(len(picture[0])):
                if col[j] != 1: continue
                if picture[i][j] == 'B':
                    count += 1
        return count