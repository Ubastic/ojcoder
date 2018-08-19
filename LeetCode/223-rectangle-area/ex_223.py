class Solution(object):
    def computeArea(self, A, B, C, D, E, F, G, H):
        """
        :type A: int
        :type B: int
        :type C: int
        :type D: int
        :type E: int
        :type F: int
        :type G: int
        :type H: int
        :rtype: int
        """
        rect1 = (C - A) * (D - B)
        rect2 = (G - E) * (H - F)

        if C > E and D > F and G > A and H > B:
            intersection = (min(C, G) - max(E, A)) * (min(D, H) - max(F, B))
        else:
            intersection = 0
        return rect1 + rect2 - intersection
