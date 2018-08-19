class Solution(object):
    def fourSumCount(self, A, B, C, D):
        """
        :type A: List[int]
        :type B: List[int]
        :type C: List[int]
        :type D: List[int]
        :rtype: int
        """
        count = 0
        table = {}
        for i in A:
            for j in B:
                if i+j in table:
                    table[i+j] += 1
                else:
                    table[i+j] = 1
        for p in C:
            for q in D:
                if -(p + q) in table:
                    count += table[-(p + q)]
        return count