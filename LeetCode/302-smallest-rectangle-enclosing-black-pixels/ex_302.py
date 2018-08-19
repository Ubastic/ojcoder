class Solution(object):
    def minArea(self, image, x, y):
        """
        :type image: List[List[str]]
        :type x: int
        :type y: int
        :rtype: int
        """
        maxx = minx = x
        maxy = miny = y
        
        for x in range(len(image)):
            for y in range(len(image[0])):
                if image[x][y] == '1':
                    maxx = max(x, maxx)
                    maxy = max(y, maxy)
                    minx = min(x, minx)
                    miny = min(y, miny)
        return (maxx - minx + 1) * (maxy - miny + 1)