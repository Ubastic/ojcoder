class Solution(object):
    def isConvex(self, points):
        """
        :type points: List[List[int]]
        :rtype: bool
        """
        last = temp = 0
        length = len(points)
        for i in range(length):
            p0, p1, p2 = points[i-2], points[i-1], points[i]
            # see CLRS 33.1
            temp = (p1[0] - p0[0]) * (p2[1] - p0[1]) - (p2[0] - p0[0]) * (p1[1] - p0[1])
            if temp:
                if temp * last < 0:
                    return False
                last = temp
        return True