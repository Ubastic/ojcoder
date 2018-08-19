class Solution(object):
    def findMinArrowShots(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        if not points:  return 0
        points.sort()
        count = 1
        i, j = points[0][0], points[0][1]
        for p in points:
            if p[0] <= j:
                i = max(p[0], i)
                j = min(p[1], j)
            else:
                count += 1
                i, j = p[0], p[1]
        return count