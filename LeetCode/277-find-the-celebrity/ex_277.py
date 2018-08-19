# The knows API is already defined for you.
# @param a, person a
# @param b, person b
# @return a boolean, whether a knows b
# def knows(a, b):

class Solution(object):
    def findCelebrity(self, n):
        """
        :type n: int
        :rtype: int
        """
        for i in range(n):
            is_celebrity = True
            for j in range(n):
                if i != j and (not knows(j, i) or knows(i, j)): 
                    is_celebrity = False
                    break
            if is_celebrity:
                return i
        return -1