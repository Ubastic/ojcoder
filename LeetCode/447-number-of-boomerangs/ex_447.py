class Solution(object):
    def numberOfBoomerangs(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        res = 0
        for p1 in points:
            table = {}
            for p2 in points:
                dst = self.sqDistance(p1, p2)
                table[dst] = 1 + table.get(dst, 0)
            for k in table:
                res += table[k] * (table[k] - 1)
        return res
        
    def sqDistance(self, p1, p2):
        return (p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2